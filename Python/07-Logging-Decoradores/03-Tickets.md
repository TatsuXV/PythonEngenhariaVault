---
tipo: ticket
trilha: python
capitulo: 07
titulo: "Tickets de Logging e Decoradores"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, logging, decorators]
---
# Tickets: Logging e Decoradores

> [!abstract] Capítulo 07 · Tickets de Logging e Decoradores
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/07-Logging-Decoradores/02-Lab]] · 📦 Entrega: [[Python/07-Logging-Decoradores/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P07-01: A Morte dos Prints (CONSERTAR)
**Prioridade:** Alta | **Tipo:** Refatoração | **Tempo:** 60min
> **Contexto:** O script de extração de dados está repleto de `print("Iniciando...")` e `print("Erro: " + str(e))`. Isso torna impossível filtrar mensagens por nível ou salvar em arquivo.
> **Entrada:** Código com 20+ chamadas de `print()`.
> **Saída Esperada:** Código utilizando `logging.getLogger()` com níveis apropriados (`INFO`, `ERROR`, `DEBUG`).

**✅ Critério de Aceite:** 
- [ ] Zero ocorrências de `print()` no código final.
- [ ] Configuração de `basicConfig` para salvar logs em `pipeline.log`.
- [ ] Mensagens de erro devem usar `logger.exception()` para capturar o traceback completo.

**💡 Dicas:**
> [!tip] Nível 1
> Substitua `print("Erro")` por `logger.error("Erro")`.
> 
> [!tip] Nível 2
> Use `logger.exception()` dentro de blocos `except` para que o Python anexe automaticamente a pilha de erro (stack trace).

**🧪 Como Verificar:** 
Verificar se o arquivo `pipeline.log` foi criado e contém as mensagens com timestamps.

---

## 🎫 TICKET P07-02: O Decorador de Resiliência (ESCREVER)
**Prioridade:** Alta | **Tipo:** Feature | **Tempo:** 90min
> **Contexto:** A função de chamada de API da Loja Aurora falha ocasionalmente por instabilidade de rede. Precisamos de um decorador `@retry` que tente executar a função até 3 vezes antes de desistir.
> **Entrada:** Uma função que falha aleatoriamente.
> **Saída Esperada:** Decorador que implementa a lógica de tentativa e erro.

**✅ Critério de Aceite:** 
- [ ] O decorador deve tentar a função exatamente 3 vezes.
- [ ] Deve haver um pequeno delay (`time.sleep`) entre as tentativas.
- [ ] Logar cada tentativa falha como `WARNING` e a falha final como `ERROR`.

**💡 Dicas:**
> [!tip] Nível 1
> Use um loop `for i in range(3):` dentro do wrapper.
> 
> [!tip] Nível 2
> Se a função for bem sucedida, use `return` imediatamente para sair do loop de retry.

**🧪 Como Verificar:** 
Criar uma função que lança `ConnectionError` nas duas primeiras vezes e funciona na terceira. O script deve terminar com sucesso.

---

## 🎫 TICKET P07-03: Auditoria de Performance (REVISAR)
**Prioridade:** Média | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou um decorador de tempo, mas ele não funciona para funções que retornam valores.
> **Código:**
> ```python
> def timer(func):
>     def wrapper(*args, **kwargs):
>         start = time.time()
>         func(*args, **kwargs)
>         print(f"Tempo: {time.time() - start}")
>     return wrapper
> ```

**✅ Critério de Aceite:** 
- [ ] Identificar que a função `wrapper` não retorna o resultado de `func`.
- [ ] Sugerir a adição de `result = func(*args, **kwargs)` seguido de `return result`.
- [ ] Identificar a falta de `@wraps(func)`.

**💡 Dicas:**
> [!tip] Nível 1
> Se a função original retornava `10`, a versão decorada agora retorna `None`.
> 
> [!tip] Nível 2
> Olhe para o final da função `wrapper`.

**🧪 Como Verificar:** 
Relatório de review com a correção do retorno e a adição do `@wraps`.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/07-Logging-Decoradores/01-Aula]] ou [[Python/07-Logging-Decoradores/02-Lab]].
