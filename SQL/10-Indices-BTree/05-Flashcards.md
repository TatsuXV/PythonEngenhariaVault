---
tipo: flashcards
trilha: SQL
capitulo: 10
titulo: "Flashcards: Índices B-Tree"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Índices B-Tree

> [!question] O que é um Clustered Index no MySQL (InnoDB)?
> [!success] Resposta
> É o índice onde a própria tabela é organizada fisicamente pela chave primária. Só existe um por tabela e garante o acesso mais rápido possível aos dados.

> [!question] Qual a regra do "Left-most Prefix" em índices compostos?
> [!success] Resposta
> Um índice em `(A, B, C)` só será utilizado se a query filtrar por `A`, ou por `A e B`, ou por `A, B e C`. Se filtrar apenas por `B`, o índice é ignorado.

> [!question] Por que índices em colunas de baixa cardinalidade (ex: Sexo) são ineficientes?
> [!success] Resposta
> Porque o otimizador percebe que terá que ler metade da tabela de qualquer maneira, tornando o custo de ler o índice + a tabela maior do que fazer um Full Table Scan direto.

> [!question] O que é um Covering Index?
> [!success] Resposta
> É quando todas as colunas solicitadas no `SELECT` e `WHERE` fazem parte do índice. O MySQL retorna o resultado direto do índice sem precisar acessar a tabela principal (evita o Bookmark Lookup).

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
