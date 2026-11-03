---
tipo: revisao
trilha: python
capitulo: 07
titulo: "Revisão: Logging e Decoradores"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, logging, decorators]
---
# Revisão: Logging e Decoradores

## ⚪ Folha em Branco
**Desafio:** Escreva, sem consultar, um decorador chamado `@audit_log` que:
1. Logue o início da função com nível `INFO`.
2. Se a função falhar, logue o erro com `logger.exception`.
3. Se a função tiver sucesso, logue o tempo de execução total.
4. Use `@wraps` para manter a identidade da função.

> [!success] Comparação
> ```python
> import logging, time
> from functools import wraps
> 
> logger = logging.getLogger("Audit")
> 
> def audit_log(func):
>     @wraps(func)
>     def wrapper(*args, **kwargs):
>         logger.info(f"Iniciando: {func.__name__}")
>         start = time.perf_counter()
>         try:
>             res = func(*args, **kwargs)
>             end = time.perf_counter()
>             logger.info(f"Sucesso: {func.__name__} em {end-start:.4f}s")
>             return res
>         except Exception:
>             logger.exception(f"Erro em {func.__name__}")
>             raise
>     return wrapper
> ```

## 🗣 Explique ao Júnior
Por que não devemos usar `logger.debug()` para tudo e deixar o nível global em `DEBUG` em produção?
> [!tip] Resposta Sugerida
> "Logs de DEBUG são extremamente detalhados (ex: imprimindo cada linha de um arquivo de 1GB). Se deixarmos isso ativo em produção, o arquivo de log crescerá gigabytes em poucos minutos, consumindo todo o espaço em disco do servidor e degradando a performance do sistema devido ao excesso de operações de escrita (I/O)."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/07-Logging-Decoradores/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/07-Logging-Decoradores/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/07-Logging-Decoradores/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Arquivos:** Qual a diferença entre `json.load()` e `json.loads()`?
2. **Coleções:** Quando usar um `set` em vez de uma `list` para filtrar duplicatas?
3. **Funções:** O que acontece se você usar um default mutável (`data=[]`) em uma função?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (crio decoradores de retry e monitoramento sem olhar guia).
- [ ] 3: Consegui implementar uma estratégia de logging estruturado para um projeto.

## 📓 Registro de Erros
Sintoma: `AttributeError: 'function' object has no attribute '____'` após decorar uma função.
Causa: Esquecimento do `@wraps(func)` no decorador.
Regra: Todo decorador DEVE usar `@wraps` para preservar os metadados da função original.
Tag: #erro/decorators
