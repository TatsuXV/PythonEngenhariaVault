---
tipo: flashcards
trilha: SQL
capitulo: 04
titulo: "Flashcards: Window Functions"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Window Functions

> [!question] Qual a diferença entre RANK(), DENSE_RANK() e ROW_NUMBER()?
> [!success] Resposta
> `ROW_NUMBER()`: Sequência única (1,2,3,4). `RANK()`: Pula números em empates (1,2,2,4). `DENSE_RANK()`: Não pula números em empates (1,2,2,3).

> [!question] Para que serve a cláusula PARTITION BY em uma Window Function?
> [!success] Resposta
> Ela define a "janela" de cálculo. O cálculo é reiniciado sempre que o valor da coluna de partição muda.

> [!question] O que a função LAG() faz e qual sua utilidade principal?
> [!success] Resposta
> Ela acessa o valor de uma linha anterior. É a ferramenta principal para calcular variação temporal (Growth) ou comparar a linha atual com a anterior.

> [!question] É possível usar Window Functions no MySQL 5.7?
> [!success] Resposta
> Não. Window Functions foram introduzidas apenas no MySQL 8.0. Em versões anteriores, é necessário usar subqueries ou variáveis de sessão.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
