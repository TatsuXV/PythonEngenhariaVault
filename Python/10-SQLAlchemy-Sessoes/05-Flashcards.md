---
tipo: flashcard
trilha: python
capitulo: 10
titulo: "Flashcards: SQLAlchemy 2.0"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [flashcards, sqlalchemy, orm]
---
# Flashcards: SQLAlchemy 2.0

## 🧠 Conceitos
Qual a diferença principal entre o SQLAlchemy Core e o SQLAlchemy ORM?::O Core trabalha com esquemas e SQL puro (Tabelas), enquanto o ORM mapeia tabelas do banco para classes Python (Objetos).
O que é o problema do "N+1 Queries"?::Ocorre quando o código faz uma query para obter uma lista de objetos e depois faz mais N queries (uma para cada objeto) para carregar seus relacionamentos, degradando a performance.
Qual a função do `session.commit()`?::Finaliza a transação atual, gravando permanentemente todas as alterações pendentes no banco de dados.
Para que serve o `session.rollback()`?::Cancela todas as alterações feitas na sessão atual, retornando o banco ao estado anterior ao início da transação.

## ⌨️ Código & Sintaxe
Como definir uma coluna como chave primária no SQLAlchemy 2.0?::`col_name: Mapped[int] = mapped_column(primary_key=True)`
Como realizar um JOIN entre duas tabelas usando o estilo moderno do SQLAlchemy?::`select(Product).join(Category).where(Category.name == 'Eletrônicos')`
Qual a forma correta de carregar relacionamentos antecipadamente para evitar o N+1?::Usando a opção `joinedload()`, ex: `select(Order).options(joinedload(Order.items))`.

## ⚠️ Erros e Correções
Erro: `DetachedInstanceError`. Causa?::Tentativa de acessar um atributo de um objeto (geralmente um relacionamento) após a sessão que o criou ter sido fechada. Correção: Usar `joinedload` ou re-anexar o objeto à sessão.
Erro: `IntegrityError`. Causa?::Violação de restrições do banco, como tentar inserir um valor duplicado em uma coluna `unique=True` ou violar uma `ForeignKey`. Correção: Validar os dados antes da inserção ou tratar a exceção.
Erro: `InvalidRequestError` ao fazer commit em sessão fechada. Causa?::Chamada de `session.commit()` após `session.close()`. Correção: Garantir que o commit ocorra dentro do contexto da sessão.

## 🧩 Cloze (Preencher)
O ==Unit of Work== é o padrão de design utilizado pela Session do SQLAlchemy para rastrear todas as mudanças nos objetos e sincronizá-las com o banco de dados em uma única transação?
resposta: Unit of Work
