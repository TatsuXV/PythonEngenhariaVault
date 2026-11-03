---
tipo: flashcard
trilha: python
capitulo: 07
titulo: "Flashcards: Logging e Decoradores"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, logging, decorators]
---
# Flashcards: Logging e Decoradores

## 🧠 Conceitos
Qual a diferença entre `logger.error()` e `logger.exception()`?::`logger.error()` apenas grava a mensagem de erro. `logger.exception()` grava a mensagem e anexa automaticamente todo o Stack Trace (rastreio da pilha), essencial para depurar a linha exata da falha.
O que é a função do `@wraps` do módulo `functools` em um decorador?::Ela copia os metadados da função original (nome, docstring, anotações) para a função `wrapper`, evitando que a função decorada perca sua identidade.
Qual a ordem de severidade dos logs do Python (do mais baixo ao mais alto)?::`DEBUG` $\rightarrow$ `INFO` $\rightarrow$ `WARNING` $\rightarrow$ `ERROR` $\rightarrow$ `CRITICAL`.

## ⌨️ Código & Sintaxe
Como configurar o logging para salvar em arquivo com modo append?::`logging.basicConfig(filename='app.log', filemode='a')`
Qual a sintaxe básica de um decorador que não recebe argumentos?::
```python
def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # lógica antes
        res = func(*args, **kwargs)
        # lógica depois
        return res
    return wrapper
```
Como disparar um log de nível `CRITICAL`?::`logger.critical("Mensagem de falha catastrófica")`

## ⚠️ Erros e Correções
Erro: O decorador está sendo executado, mas a função original retorna `None` em vez do valor esperado. Causa?::O `wrapper` dentro do decorador esqueceu de dar `return` no resultado da chamada `func(*args, **kwargs)`.
Erro: `logs` não aparecem no console mesmo após `logger.info()`. Causa?::O nível global de log (`basicConfig`) está configurado como `WARNING` ou superior. Correção: Alterar para `level=logging.INFO`.

## 🧩 Cloze (Preencher)
Decoradores são uma implementação do padrão de projeto ==Wrapper==, permitindo adicionar comportamentos a funções sem alterar seu código interno?
resposta: Wrapper
