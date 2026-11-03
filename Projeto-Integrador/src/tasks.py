import logging
import time
import random
from .models import Task, TaskStatus

logger = logging.getLogger("AuroraEngine")

class PythonTask(Task):
    """Tarefa que executa uma função Python configurável."""
    def __init__(self, name: str, func, *args, **kwargs):
        super().__init__(name)
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def execute(self) -> bool:
        # Lógica de Retry implementada aqui no runtime
        attempt = 0
        while attempt <= self.max_retries:
            try:
                logger.info(f"[{self.name}] Execution attempt {attempt + 1}/{self.max_retries + 1}")
                result = self.func(*self.args, **self.kwargs)
                return True if result else False
            except Exception as e:
                attempt += 1
                logger.warning(f"[{self.name}] Attempt {attempt} failed: {e}")
                if attempt <= self.max_retries:
                    wait_time = 2 ** attempt # Exponential backoff
                    logger.info(f"[{self.name}] Retrying in {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    logger.error(f"[{self.name}] Max retries reached. Task failed.")
                    return False
        return False

class SQLTask(Task):
    """
    Tarefa que simula a execução de um comando SQL.
    Em um ambiente real, aqui usaria SQLAlchemy ou psycopg2.
    """
    def __init__(self, name: str, sql_command: str, connection_string: str):
        super().__init__(name)
        self.sql_command = sql_command
        self.connection_string = connection_string

    def execute(self) -> bool:
        attempt = 0
        while attempt <= self.max_retries:
            try:
                logger.info(f"[{self.name}] Executing SQL on {self.connection_string}: {self.sql_command}")

                # Simulação de falha intermitente de conexão (10% de chance)
                if random.random() < 0.1:
                    raise ConnectionError("Database connection timeout!")

                # Simulação de execução do comando
                time.sleep(0.5)
                return True
            except Exception as e:
                attempt += 1
                logger.warning(f"[{self.name}] SQL Error: {e}. Attempt {attempt}/{self.max_retries + 1}")
                if attempt <= self.max_retries:
                    time.sleep(1)
                else:
                    return False
        return False
