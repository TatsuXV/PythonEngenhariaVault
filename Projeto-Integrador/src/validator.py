from typing import Dict, List, Set
from .models import DAG

class CircularDependencyError(Exception):
    """Exceção lançada quando um ciclo é detectado na DAG."""
    def __init__(self, cycle: List[str]):
        self.cycle = cycle
        super().__init__(f"Circular Dependency Detected: {' -> '.join(cycle)}")

class CycleDetector:
    """
    Implementação de detecção de ciclos usando DFS com marcação de cores.
    Cores:
    0: BRANCO - Não visitado
    1: CINZA  - Visitando (está na pilha de recursão atual)
    2: PRETO  - Visitado (todos os descendentes foram explorados)
    """
    def __init__(self, dag: DAG):
        self.dag = dag
        self.colors: Dict[str, int] = {node: 0 for node in dag.nodes}
        self.path: List[str] = []

    def validate(self) -> bool:
        """Valida se a DAG é realmente acíclica. Lança CircularDependencyError se houver ciclo."""
        for node in self.dag.nodes:
            if self.colors[node] == 0:
                if self._dfs(node):
                    return False # Ciclo encontrado
        return True # É um DAG

    def _dfs(self, node: str) -> bool:
        # Marcar como visitando (Cinza)
        self.colors[node] = 1
        self.path.append(node)

        for child in self.dag.get_children(node):
            if self.colors[child] == 1:
                # Ciclo detectado!
                # Extraímos apenas a parte do caminho que compõe o ciclo
                cycle_start_idx = self.path.index(child)
                cycle_path = self.path[cycle_start_idx:] + [child]
                raise CircularDependencyError(cycle_path)

            if self.colors[child] == 0:
                if self._dfs(child):
                    return True

        # Marcar como visitado (Preto) e remover da pilha de caminho
        self.colors[node] = 2
        self.path.pop()
        return False
