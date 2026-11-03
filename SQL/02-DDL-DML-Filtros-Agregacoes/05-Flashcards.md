---
tipo: flashcards
trilha: SQL
capitulo: 02
titulo: "Flashcards: DDL, DML e Agregados"
nivel: 2
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: DDL, DML e Agregados

> [!question] Qual a diferença fundamental entre DELETE e TRUNCATE?
> [!success] Resposta
> `DELETE` é DML, remove linhas (pode usar WHERE) e é mais lento. `TRUNCATE` é DDL, esvazia a tabela inteira rapidamente, reseta o AUTO_INCREMENT e não aceita WHERE.

> [!question] Para que serve a cláusula HAVING?
> [!success] Resposta
> Serve para filtrar resultados de funções de agregação. O `WHERE` filtra linhas individuais; o `HAVING` filtra os grupos criados pelo `GROUP BY`.

> [!question] Como o MySQL 8.x trata o tipo BOOLEAN?
> [!success] Resposta
> Ele o trata como um apelido (alias) para `TINYINT(1)`, onde 0 é False e 1 é True.

> [!question] O que é a restrição (constraint) PRIMARY KEY?
> [!success] Resposta
> É a combinação de NOT NULL e UNIQUE. Garante que cada linha da tabela seja identificável de forma única e que a coluna nunca esteja vazia.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
