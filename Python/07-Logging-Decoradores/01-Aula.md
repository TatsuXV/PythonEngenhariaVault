---
tipo: aula
trilha: python
capitulo: 07
titulo: "Logging e Decoradores: Observabilidade e Meta-programação"
nivel: 3
tempo_estimado_h: 5
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [logging, decorators, observabilidade]
---
# Logging e Decoradores: Observabilidade e Meta-programação

> [!abstract] Capítulo 07 · Logging e Decoradores: Observabilidade e Meta-programação
> ⏱ 5h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/01-Aula]] · 📦 Entrega: [[Python/07-Logging-Decoradores/07-Entrega-Projeto|Sistema de Monitoramento de Pipeline]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Por que usar a biblioteca `logging` é superior ao uso de `print()` em pipelines de produção?
> ?
> [!question] O que é um decorador em Python e como ele altera o comportamento de uma função?
> ?
> [!question] Qual a diferença entre os níveis de log `INFO`, `WARNING`, `ERROR` e `CRITICAL`?
> ?

## 🎯 Objetivo
> [!goal]
> Implementar a observabilidade no pipeline de dados, substituindo a saída de console por logs estruturados e utilizando decoradores para adicionar funcionalidades transversais (cross-cutting concerns), como medição de tempo e retry de funções.

## ⚙️ No Pipeline
> [!pipeline]
> Imagine um pipeline que roda às 3h da manhã em um servidor remoto. Se ele falhar, um `print()` é inútil porque ninguém está olhando o console. O `logging` salva a saída em arquivos com carimbo de data/hora (timestamps), permitindo que o engenheiro faça a "autópsia" do erro no dia seguinte. Decoradores, por sua vez, permitem adicionar logs de tempo a todas as funções de transformação sem ter que escrever `start_time = time.time()` dentro de cada uma delas.

## 📚 Teoria

### 1. Logging Profissional (`logging` stdlib)
O `logging` permite configurar a saída (console, arquivo, socket) e o nível de severidade.

**Configuração Básica:**
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='pipeline.log',
    filemode='a' # append
)

logger = logging.getLogger("Ingestor")
logger.info("Iniciando a ingestão de dados...")
logger.error("Falha ao conectar no banco de dados!")
```

**Níveis de Log:**
- `DEBUG`: Detalhes técnicos (ex: query SQL gerada).
- `INFO`: Fluxo normal (ex: "Processou 1000 linhas").
- `WARNING`: Algo estranho, mas o pipeline continua.
- `ERROR`: Erro em um registro, mas o pipeline segue.
- `CRITICAL`: Falha catastrófica, interrompe o processo.

### 2. Decoradores (Decorators)
Um decorador é uma função que recebe outra função, adiciona alguma lógica e a retorna. É a implementação do padrão *Wrapper*.

**Exemplo: Medidor de Tempo**
```python
import time
from functools import wraps

def timer(func):
    @wraps(func) # Preserva os metadados da função original
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Função {func.__name__} levou {end-start:.4f}s")
        return result
    return wrapper

@timer
def process_data():
    time.sleep(1)

process_data() # Saída: Função process_data levou 1.00xx s
```

### 3. Loguru: A Alternativa Moderna
Embora a stdlib seja o padrão, a biblioteca `loguru` é amplamente usada em DE por ser mais concisa e possuir rotação de logs automática.
- `from loguru import logger`
- `logger.info("Mensagem")` (sem necessidade de `basicConfig`).

## ⚠️ Armadilhas e Erros Comuns
- **Logar Dados Sensíveis:** Jamar logar senhas, tokens ou CPFs de clientes no arquivo de log.
- **Nível de Log em Produção:** Deixar o log em `DEBUG` em produção gera arquivos gigantescos e degrada a performance. Use `INFO` ou `WARNING`.
- **Esquecer o `@wraps`:** Sem o `@wraps(func)`, a função decorada perde seu nome original e sua docstring, quebrando ferramentas de debug e documentação.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `print()` para debugar erros rapidamente em produção."
> **Por que está errado:** Prints não possuem timestamps, não podem ser filtrados por nível e são perdidos ao reiniciar o console.
> **Correto:** Use `logger.debug()` para rastreamento e `logger.error()` para falhas.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Retry Decorators:** Em engenharia de dados, falhas de rede são comuns. Usar decoradores de retry (como a biblioteca `tenacity`) permite que a função tente novamente 3 vezes antes de falhar, tornando o pipeline resiliente.

## 📖 Fonte
Fonte: [Python Docs - Logging](https://docs.python.org/3/library/logging.html) (Versão 3.12)

---
← [[Python/06-Arquivos-Pathlib/01-Aula]] · [[MOC-Python]] · [[Python/08-OOP-Encapsulamento/01-Aula]] →
