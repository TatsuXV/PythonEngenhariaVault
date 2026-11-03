---
tipo: gabarito
trilha: python
capitulo: 07
titulo: "Gabarito: Logging e Decoradores"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, logging, decorators]
---
# Gabarito: Logging e Decoradores

## 💡 Solução do Lab (Item 2 - Complete)
```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Verifica se a chave 'user_role' existe e se o valor é 'admin'
        if kwargs.get("user_role") != "admin":
            raise PermissionError("Acesso negado: Apenas administradores.")
        
        return func(*args, **kwargs)
    return wrapper

@require_auth
def delete_database(user_role: str):
    print("Banco de dados deletado!")

# Testes
try:
    delete_database(user_role="user")
except PermissionError as e:
    print(e) # Acesso negado: Apenas administradores.
```
**Raciocínio:** O decorador atua como um middleware de segurança. Ao usar `kwargs.get()`, evitamos um `KeyError` caso o argumento `user_role` não seja passado, tratando a ausência como falta de permissão.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
import logging
import time
import sys
from functools import wraps

# Configuração
logging.basicConfig(level=logging.INFO, filename="performance.log", 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PerformanceMonitor")

def measure_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        
        # Medindo tamanho da saída
        size = sys.getsizeof(result)
        duration = end_time - start_time
        
        logger.info(f"{func.__name__} | Tempo: {duration:.4f}s | Tamanho Saída: {size} Bytes")
        return result
    return wrapper

@measure_performance
def transform_data(data: list):
    return [float(x) for x in data]

# Teste
transform_data(["1.0", "2.0", "3.0"])
```

## 🎫 Soluções dos Tickets

### P07-01: A Morte dos Prints
**Substituição Sugerida:**
- `print("Iniciando...")` $\rightarrow$ `logger.info("Iniciando a extração de dados.")`
- `print("Erro: " + str(e))` $\rightarrow$ `logger.exception("Falha crítica na extração")`

**Por que `logger.exception`?** Diferente do `logger.error`, o `exception` anexa automaticamente todo o Stack Trace ao log, permitindo saber exatamente em qual linha o erro ocorreu sem precisar reproduzir o bug manualmente.

### P07-02: O Decorador de Resiliência
```python
import time
import logging
from functools import wraps

logger = logging.getLogger("RetrySystem")

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        logger.error(f"Falha final após {max_attempts} tentativas: {e}")
                        raise e
                    logger.warning(f"Tentativa {attempt} falhou: {e}. Tentando novamente em {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def call_api():
    # Simulação de falha
    import random
    if random.random() < 0.7:
        raise ConnectionError("Timeout de rede")
    return "Sucesso!"
```

### P07-03: Auditoria de Performance
**Erros identificados:**
1. **Perda de Retorno:** A função `wrapper` executa a função original mas não retorna o seu resultado. Qualquer código que dependesse do valor de retorno de `func` receberia `None`.
2. **Perda de Identidade:** Sem `@wraps(func)`, a função perde o nome original e a docstring, o que quebra ferramentas de inspeção e logs.

---
← [[Python/07-Logging-Decoradores/03-Tickets]] · [[MOC-Python]] · [[Python/08-OOP-Encapsulamento/01-Aula]] →
