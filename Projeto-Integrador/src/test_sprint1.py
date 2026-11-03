from .models import DAG, Task, TaskStatus
from .validator import CycleDetector, CircularDependencyError

class MockTask(Task):
    """Tarefa simplificada para testes de infraestrutura."""
    def __init__(self, name: str, duration: float = 0.1):
        super().__init__(name)
        self.duration = duration

    def execute(self) -> bool:
        import time
        print(f"Executing {self.name}...")
        time.sleep(self.duration)
        return True

def test_dag_validation():
    print("--- Testing DAG Validation ---")

    # Teste 1: DAG Válida
    dag_valid = DAG("Valid-DAG")
    dag_valid.add_task(MockTask("A"))
    dag_valid.add_task(MockTask("B"))
    dag_valid.add_task(MockTask("C"))
    dag_valid.add_dependency("A", "B")
    dag_valid.add_dependency("B", "C")

    try:
        CycleDetector(dag_valid).validate()
        print("✅ Test 1 Passed: Valid DAG accepted.")
    except CircularDependencyError as e:
        print(f"❌ Test 1 Failed: {e}")

    # Teste 2: DAG com Ciclo
    dag_cycle = DAG("Cycle-DAG")
    dag_cycle.add_task(MockTask("A"))
    dag_cycle.add_task(MockTask("B"))
    dag_cycle.add_task(MockTask("C"))
    dag_cycle.add_dependency("A", "B")
    dag_cycle.add_dependency("B", "C")
    dag_cycle.add_dependency("C", "A") # Ciclo C -> A

    try:
        CycleDetector(dag_cycle).validate()
        print("❌ Test 2 Failed: Cycle was not detected.")
    except CircularDependencyError as e:
        print(f"✅ Test 2 Passed: Cycle detected correctly: {e}")

if __name__ == "__main__":
    test_dag_validation()
