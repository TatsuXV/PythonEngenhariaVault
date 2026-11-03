from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Dict, List, Set, Optional
import logging

class TaskStatus(Enum):
    PENDING = auto()
    RUNNING = auto()
    SUCCESS = auto()
    FAILED = auto()

class Task(ABC):
    """Interface base para todas as tarefas do Aurora Engine."""
    def __init__(self, name: str, max_retries: int = 3):
        self.name = name
        self.max_retries = max_retries
        self.retry_count = 0
        self.status = TaskStatus.PENDING

    @abstractmethod
    def execute(self) -> bool:
        """Implementação da lógica da tarefa. Retorna True se sucesso."""
        pass

    def __repr__(self):
        return f"<Task {self.name} status={self.status.name}>"

class DAG:
    """Representação do Grafo Acíclico Direcionado (DAG) de tarefas."""
    def __init__(self, name: str):
        self.name = name
        self.nodes: Dict[str, Task] = {}
        self.edges: Dict[str, List[str]] = {} # Lista de Adjacência: Pai -> Lista de Filhos

    def add_task(self, task: Task):
        """Adiciona um nó ao grafo."""
        self.nodes[task.name] = task
        if task.name not in self.edges:
            self.edges[task.name] = []

    def add_dependency(self, parent_name: str, child_name: str):
        """Cria uma aresta direcionada: Parent -> Child."""
        if parent_name not in self.nodes or child_name not in self.nodes:
            raise ValueError(f"Ambas as tarefas {parent_name} e {child_name} devem existir na DAG.")

        self.edges[parent_name].append(child_name)

    def get_children(self, node: str) -> List[str]:
        return self.edges.get(node, [])

    def __repr__(self):
        return f"<DAG {self.name} with {len(self.nodes)} tasks>"
