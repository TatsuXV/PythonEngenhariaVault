from .models import DAG
from .scheduler import AuroraScheduler
from .tasks import PythonTask, SQLTask
import time

def dummy_processing_func(data):
    print(f"Processing data: {data}")
    return True

def test_full_pipeline():
    print("\n--- 🚀 STARTING FULL AURORA PIPELINE TEST ---\n")

    # 1. Definição da DAG
    dag = DAG("Aurora-Production-Pipeline")

    # 2. Criação de Tarefas
    # Extração (SQL)
    t1 = SQLTask("extract_users", "SELECT * FROM users", "postgres://prod_db")
    t2 = SQLTask("extract_orders", "SELECT * FROM orders", "postgres://prod_db")

    # Transformação (Python)
    t3 = PythonTask("transform_users", dummy_processing_func, "User Data")
    t4 = PythonTask("transform_orders", dummy_processing_func, "Order Data")

    # Carga (SQL)
    t5 = SQLTask("load_fact_sales", "INSERT INTO fact_sales...", "dw://warehouse")

    # Adicionando à DAG
    for t in [t1, t2, t3, t4, t5]:
        dag.add_task(t)

    # 3. Definição de Dependências
    # A extração deve acontecer primeiro
    dag.add_dependency("extract_users", "transform_users")
    dag.add_dependency("extract_orders", "transform_orders")

    # A carga final depende das duas transformações
    dag.add_dependency("transform_users", "load_fact_sales")
    dag.add_dependency("transform_orders", "load_fact_sales")

    # 4. Execução
    scheduler = AuroraScheduler(dag, max_workers=4)
    scheduler.run()

    print("\n--- 🏁 PIPELINE TEST FINISHED ---\n")

if __name__ == "__main__":
    test_full_pipeline()
