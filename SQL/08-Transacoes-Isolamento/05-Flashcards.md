---
tipo: flashcards
trilha: SQL
capitulo: 08
titulo: "Flashcards: Transações e Isolamento"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Transações e Isolamento

> [!question] O que significa a propriedade de "Atomicidade" no ACID?
> [!success] Resposta
> Significa que a transação é tratada como uma unidade única e indivisível: ou todas as operações são confirmadas (`COMMIT`) ou todas são descartadas (`ROLLBACK`) em caso de falha.

> [!question] Qual a diferença entre READ COMMITTED e REPEATABLE READ?
> [!success] Resposta
> `READ COMMITTED` garante que você não leia dados não confirmados (Dirty Reads). `REPEATABLE READ` (padrão do MySQL) garante que se você ler a mesma linha duas vezes na mesma transação, verá o mesmo valor, mesmo que outra transação a tenha alterado e commitado entre as leituras.

> [!//question] Por que não devemos usar TRUNCATE dentro de uma transação que exige ROLLBACK?
> [!success] Resposta
> Porque o `TRUNCATE` é um comando DDL (Data Definition Language). No MySQL, comandos DDL causam um "Implicit Commit", confirmando todas as alterações pendentes e tornando impossível o rollback da operação.

> [!question] O que é um Deadlock?
> [!success] Resposta
> Ocorre quando duas ou mais transações ficam esperando mutuamente a liberação de locks em recursos que a outra detém. O MySQL resolve isso derrubando a transação com a menor quantidade de alterações.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
