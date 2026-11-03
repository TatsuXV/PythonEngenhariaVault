---
tipo: lab
trilha: python
capitulo: 07
titulo: "Lab: Observabilidade e Meta-programação"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, logging, decorators]
---
# Lab: Observabilidade e Meta-programação

> [!abstract] Capítulo 07 · Lab: Observabilidade e Meta-programação
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/07-Logging-Decoradores/01-Aula]] · 📦 Entrega: [[Python/07-Logging-Decoradores/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontecerá se eu definir o nível de log como `logging.ERROR` e depois chamar `logger.info("Processando...")`?
> > [!success] Resposta
> > Nada será impresso ou gravado no arquivo.
> > **Explicação:** O logger ignora todas as mensagens com nível de severidade inferior ao nível configurado.

```python
import logging
import time
from functools import wraps

# Configuração do Logger
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("DataPipeline")

def log_execution(func):
    """Decorador que loga o início e fim de uma função."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"🚀 Iniciando execução: {func.__name__}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"✅ Finalizado com sucesso: {func.__name__}")
            return result
        except Exception as e:
            logger.error(f"❌ Erro em {func.__name__}: {str(e)}")
            raise e
    return wrapper

@log_execution
def load_csv(file_path: str):
    logger.debug(f"Lendo arquivo {file_path}")
    time.sleep(0.5) # Simula leitura
    return ["row1", "row2"]

load_csv("sales.csv")
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente um decorador chamado `@require_auth` que verifica se um argumento chamado `user_role` é igual a `"admin"`. Se não for, deve levantar um `PermissionError`.

```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Verificar se 'user_role' está em kwargs e se é 'admin'
        # TODO: complete aqui
        if kwargs.get("user_role") != "admin":
            raise PermissionError("Acesso negado: Apenas administradores.")
        
        return func(*args, **kwargs)
    return wrapper

@require_auth
def delete_database(user_role: str):
    print("Banco de dados deletado!")

# Testes
# delete_database(user_role="admin") # Deve funcionar
# delete_database(user_role="user") # Deve levantar PermissionError
```

## 🚀 3. Do Zero
**Enunciado:** Crie um "Monitor de Performance de Pipeline".
1. Implemente um decorador `@measure_performance` que calcule o tempo de execução e a quantidade de memória usada (use `sys.getsizeof` para a saída da função).
2. O resultado deve ser gravado em um arquivo de log `performance.log` usando o nível `INFO`.
3. a função decorada deve ser uma simulação de transformação de dados (ex: converter uma lista de strings para floats).

**Critério de Aceite:** 
- O log deve conter: `Nome da Função | Tempo: X.Xs | Tamanho Saída: Y Bytes`.
- Uso obrigatório de `@wraps`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Remova o `@wraps(func)` do decorador e tente imprimir `load_csv.__name__`** $\rightarrow$ Erro esperado: O nome impresso será `wrapper` e não `load_csv`.
2. **Tente logar uma mensagem `logger.debug()` com o nível global configurado como `logging.INFO`** $\rightarrow$ Comportamento: A mensagem é ignorada.
3. **Crie um loop infinito dentro de uma função decorada com `@timer`** $\rightarrow$ Comportamento: O log de finalização nunca será disparado.

---
← [[Python/07-Logging-Decoradores/01-Aula]] · [[MOC-Python]] · [[Python/07-Logging-Decoradores/03-Tickets]] →
