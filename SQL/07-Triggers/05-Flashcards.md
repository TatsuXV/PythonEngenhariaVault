---
tipo: flashcards
trilha: SQL
capitulo: 07
titulo: "Flashcards: Triggers"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Triggers

> [!question] Qual a diferença entre triggers BEFORE e AFTER?
> [!success] Resposta
> `BEFORE` executa antes da alteração no disco, permitindo validar ou mudar os dados (`SET NEW.col = val`). `AFTER` executa depois, sendo ideal para auditoria e sincronização de outras tabelas.

> [!question] O que representam as palavras OLD e NEW em um trigger?
> [!success] Resposta
> `OLD` representa o valor da linha antes da operação (disponível em UPDATE e DELETE). `NEW` representa o valor da linha após a operação (disponível em INSERT e UPDATE).

> [!question] Um trigger pode atualizar a mesma tabela que o disparou?
> [!success] Resposta
> Não diretamente (causaria loop infinito). No entanto, em triggers `BEFORE`, você pode alterar valores da linha atual usando `SET NEW.coluna = valor`.

> [!question] Triggers são disparados durante um comando TRUNCATE?
> [!success] Resposta
> Não. O `TRUNCATE` é uma operação DDL que remove a tabela e a recria, não disparando triggers de linha (`FOR EACH ROW`).

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
