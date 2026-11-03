from typing import List, Dict, Set
from collections import deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from .models import DAG, Task, TaskStatus
from .validator import CycleDetector, CircularDependencyError
from .metrics import PipelineSummary, TaskMetrics
import logging
import time

# Configuração básica de logging para o projeto
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger("AuroraEngine")

class AuroraScheduler:
    """
    O coração do Aurora Engine. Responsável por planejar e disparar a
    execução das tarefas seguindo a ordem topológica.
    """
    def __init__(self, dag: DAG, max_workers: int = 4):
        self.dag = dag
        self.max_workers = max_workers
        self.in_degree: Dict[str, int] = {}
        self.summary = PipelineSummary(dag.name)

    def _compute_in_degrees(self):
        """Calcula quantas dependências cada nó possui."""
        # Inicializa todos com 0
        self.in_degree = {node: 0 for node in self.dag.nodes}

        # Percorre todas as arestas: cada filho aumenta seu in-degree em 1
        for parent in self.dag.edges:
            for child in self.dag.edges[parent]:
                self.in_degree[child] += 1

    def run(self):
        """
        Executa a DAG utilizando o Algoritmo de Kahn para orquestração
        em tempo real com paralelismo.
        """
        logger.info(f"Starting execution of DAG: {self.dag.name}")

        # 1. Validação de Ciclos (Guard)
        try:
            CycleDetector(self.dag).validate()
        except CircularDependencyError as e:
            logger.error(f"Pipeline validation failed: {e}")
            raise

        # 2. Preparação do Grafo
        self._compute_in_degrees()

        # Queue de tarefas prontas (in-degree == 0)
        ready_queue = deque([node for node, degree in self.in_degree.items() if degree == 0])

        completed_tasks = 0
        total_tasks = len(self.dag.nodes)

        # Pool de threads para execução paralela de tarefas independentes
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            # Dicionário para rastrear futures: {future: task_name}
            futures = {}

            while completed_tasks < total_tasks:
                # 3. Dispara todas as tarefas prontas
                while ready_queue:
                    task_name = ready_queue.popleft()
                    task = self.dag.nodes[task_name]
                    task.status = TaskStatus.RUNNING

                    logger.info(f"🚀 Dispatching Task: {task_name}")
                    # Passamos o tempo de início para métricas
                    start_time = time.time()
                    future = executor.submit(self._execute_task, task, start_time)
                    futures[future] = task_name

                if not futures:
                    # Se não há tarefas prontas nem em execução, mas não terminamos, algo deu errado
                    logger.error("Deadlock detected or insufficient tasks to complete DAG.")
                    break

                # 4. Aguarda a conclusão de QUALQUER tarefa para liberar dependentes
                done_futures = as_completed(futures)
                # Pegamos apenas o primeiro que terminar para atualizar a fila rapidamente
                for future in done_futures:
                    task_name = futures.pop(future)
                    try:
                        # O result() agora retorna (success, start_time, attempts)
                        success, start_time, attempts = future.result()

                        # Registra métricas
                        self.summary.add_metric(TaskMetrics(
                            name=task_name,
                            start_time=start_time,
                            end_time=time.time(),
                            status="SUCCESS" if success else "FAILED",
                            attempts=attempts
                        ))

                        if success:
                            logger.info(f"✅ Task Completed: {task_name}")
                            completed_tasks += 1

                            # Decrementa in-degree dos filhos
                            for child in self.dag.get_children(task_name):
                                self.in_degree[child] -= 1
                                if self.in_degree[child] == 0:
                                    ready_queue.append(child)
                        else:
                            logger.error(f"❌ Task Failed: {task_name}")
                            self._mark_downstream_as_failed(task_name)
                            completed_tasks += 1

                    except Exception as e:
                        logger.exception(f"💥 Critical error executing {task_name}: {e}")
                        completed_tasks += 1

                    break

        logger.info(f"Execution finished. Total tasks processed: {completed_tasks}/{total_// la l'idée est de "empurrer" la fenêtre de l'esquerda seulement le nécessaire.
        print(self.summary.generate_report())

    def _execute_task(self, task: Task, start_time: float) -> tuple:
        """Wrapper para executar a tarefa e retornar métricas."""
        attempts = task.retry_count + 1
        try:
            result = task.execute()
            task.status = TaskStatus.SUCCESS if result else TaskStatus.FAILED
            return result, start_time, attempts
        except Exception:
            task.status = TaskStatus.FAILED
            return False, start_time, attempts

    def _mark_downstream_as_failed(self, failed_node: str):
        """Marca recursivamente todos os descendentes como falhos."""
        stack = [failed_node]
        visited = set()

        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                for child in self.dag.get_children(curr):
                    self.dag.nodes[child].status = TaskStatus.FAILED
                    stack.append(child)
