---
tipo: flashcards
trilha: SQL
capitulo: 09
titulo: "Flashcards: Ordem de Execução e EXPLAIN"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Ordem de Execução e EXPLAIN

> [!question] Qual a ordem lógica de execução de uma query SQL (do início ao fim)?
> [!success] Resposta
> `FROM` $\rightarrow$ `ON` $\rightarrow$ `JOIN` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `DISTINCT` $\rightarrow$ `ORDER BY` $\rightarrow$ `LIMIT`.

> [!question] O que significa `type: ALL` no resultado do EXPLAIN?
> [!success] Resposta
> Significa que o MySQL realizou um **Full Table Scan**, lendo todas as linhas da tabela. É o cenário de pior performance e deve ser evitado em tabelas grandes.

> [!question] O que é uma query "SARGable" (Search ARGumentable)?
> [!//success] Resposta
> É uma query escrita de forma que o otimizador do banco consiga utilizar os índices disponíveis. Exemplo: evitar funções em colunas no `WHERE` (usar `col >= 'data'` em vez de `YEAR(col) = 2023`).

> [!//question] Qual a diferença entre `Using filesort` e `Using index` na coluna Extra do EXPLAIN?
> [!success] Resposta
> `Using index`: O MySQL resolveu a query usando apenas o índice (muito rápido). `Using filesort`: O MySQL teve que ordenar os dados em memória ou disco após a leitura (lento).

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
