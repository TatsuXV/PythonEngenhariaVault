---
tipo: flashcards
trilha: SQL
capitulo: 01
titulo: "Flashcards: Ambiente e SELECT"
nivel: 1
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Ambiente e SELECT

> [!question] Qual a ordem lógica de processamento de uma query SQL básica (FROM, WHERE, SELECT)?
> [!success] Resposta
> 1. `FROM` (Localiza a tabela) $\rightarrow$ 2. `WHERE` (Filtra as linhas) $\rightarrow$ 3. `SELECT` (Escolhe as colunas).

> [!question] No MySQL, é possível usar um Alias criado no SELECT dentro da cláusula WHERE?
> [!success] Resposta
> Não. O `WHERE` é processado antes do `SELECT`. Para filtrar por um cálculo, você deve repetir a expressão no `WHERE` ou usar uma Subquery/CTE.

> [!question] Qual a diferença entre aspas simples (') e aspas duplas (") no MySQL em relação ao padrão ANSI?
> [!success] Resposta
> O padrão ANSI usa aspas simples para strings. O MySQL permite aspas duplas, mas para máxima portabilidade entre bancos (como Postgres), deve-se usar aspas simples.

> [!question] Para que serve o operador `DISTINCT`?
> [!success] Resposta
> Ele remove linhas duplicadas do resultado final, retornando apenas valores únicos.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
