---
tipo: flashcards
trilha: SQL
capitulo: 03
titulo: "Flashcards: Joins e Having"
nivel: 3
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Joins e Having

> [!question] Qual a diferença entre INNER JOIN e LEFT JOIN?
> [!success] Resposta
> `INNER JOIN` retorna apenas linhas com correspondência em ambas as tabelas. `LEFT JOIN` retorna todas as linhas da tabela da esquerda, preenchendo com `NULL` as da direita quando não há correspondência.

> [!question] O MySQL 8.x suporta FULL OUTER JOIN? Como simulá-lo?
> [!success] Resposta
> Não suporta nativamente. Simula-se fazendo um `LEFT JOIN` UNION com um `RIGHT JOIN`.

> [!question] O que acontece se você filtrar uma coluna da tabela da direita no WHERE em um LEFT JOIN?
> [!success] Resposta
> O `LEFT JOIN` é transformado em um `INNER JOIN` acidentalmente, pois o `WHERE` remove as linhas onde a coluna da direita é `NULL`.

> [!question] Para que serve o CROSS JOIN?
> [!success] Resposta
> Para criar um Produto Cartesiano (cada linha de A com cada linha de B). Útil para gerar combinações de testes ou matrizes, mas perigoso em tabelas grandes.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
