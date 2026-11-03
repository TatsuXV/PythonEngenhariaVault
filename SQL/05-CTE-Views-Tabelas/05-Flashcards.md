---
tipo: flashcards
trilha: SQL
capitulo: 05
titulo: "Flashcards: CTEs, Views e Tabelas Temporárias"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: CTEs, Views e Tabelas Temporárias

> [!question] Qual a diferença entre uma CTE e uma View?
> [!success] Resposta
> A CTE é temporária e existe apenas durante a execução de UMA única query. A View é um objeto salvo no banco de dados que pode ser consultada a qualquer momento por qualquer usuário com permissão.

> [!question] Quando devemos preferir uma Tabela Temporária em vez de uma CTE?
> [!success] Resposta
> Quando precisamos usar o mesmo conjunto de dados processados em várias queries diferentes dentro da mesma sessão, evitando que o banco de dados tenha que reprocessar a CTE a cada nova query.

> [!question] O MySQL 8.x suporta Materialized Views nativamente?
> [!success] Resposta
> Não. No MySQL, para ter o efeito de uma Materialized View (armazenar o resultado fisicamente para performance), deve-se criar uma tabela real e atualizá-la periodicamente via scripts ou triggers.

> [!question] O que é uma CTE Recursiva?
> [!//success] Resposta
> É uma CTE que faz referência a si mesma. É a única forma eficiente de percorrer estruturas hierárquicas (como organogramas de empresa ou categorias de produtos pai/filho) no SQL.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
