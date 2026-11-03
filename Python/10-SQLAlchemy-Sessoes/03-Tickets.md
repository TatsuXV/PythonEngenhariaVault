---
tipo: ticket
trilha: python
capitulo: 10
titulo: "Tickets de SQLAlchemy 2.0"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [ticket, sqlalchemy, orm, performance]
---
# Tickets: SQLAlchemy 2.0

> [!abstract] Capítulo 10 · Tickets de SQLAlchemy 2.0
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/10-SQLAlchemy-Sessoes/02-Lab]] · 📦 Entrega: [[Python/10-SQLAlchemy-Sessoes/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P10-01: O Pesadelo do N+1 (OTIMIZAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O relatório de pedidos está extremamente lento. Para cada pedido (`Order`), o código faz uma nova query no banco para buscar os itens (`OrderItems`). Se houver 1.000 pedidos, o código faz 1.001 queries.
> **Entrada:** Loop que acessa `order.items`.
> **Saída Esperada:** Refatoração para usar `joinedload`.

**✅ Critério de Aceite:**
- [ ] Implementar `joinedload(Order.items)` no statement de seleção.
- [ ] Reduzir o número de queries de $N+1$ para apenas 1 query com JOIN.
- [ ] Validar via logs do SQLAlchemy (`echo=True` no engine) que apenas um SELECT foi disparado.

**💡 Dicas:**
> [!tip] Nível 1
> O `joinedload` força o SQLAlchemy a fazer um LEFT JOIN no banco de dados, trazendo os itens junto com o pedido em uma única viagem ao servidor.
> 
> [!tip] Nível 2
> Importe `from sqlalchemy.orm import joinedload`.

**🧪 Como Verificar:**
Habilitar `create_engine(..., echo=True)` e observar que o log do terminal mostra apenas um comando SQL longo em vez de centenas de comandos curtos.

---

## 🎫 TICKET P10-02: A Transação Fantasma (DEBUG)
**Prioridade:** Média | **Tipo:** Bug/Integridade | **Tempo:** 60min
> **Contexto:** O sistema de pagamento está falhando. Às vezes, o saldo do cliente é debitado, mas o pedido não é criado no banco. Isso acontece porque o programador usou dois `commit()` diferentes.
> **Entrada:** Código com múltiplos commits espalhados.
> **Saída Esperada:** Unificar a operação em uma única transação atômica.

**✅ Critério de Aceite:**
- [ ] Remover commits intermediários.
- [ ] Envolver as duas operações (débito e criação de pedido) em um bloco `try...except`.
- [ ] Implementar `session.rollback()` no bloco `except` para garantir que, se o pedido falhar, o saldo volte ao cliente.

**💡 Dicas:**
> [!tip] Nível 1
> Uma transação deve representar uma "unidade de trabalho". Ou tudo acontece, ou nada acontece.
> 
> [!tip] Nível 2
> Use o contexto `with Session(engine) as session:` para garantir que a sessão seja fechada automaticamente.

**🧪 Como Verificar:**
Simular um erro na criação do pedido e verificar se o saldo do cliente permanece inalterado no banco.

---

## 🎫 TICKET P10-03: Inserção Massiva (ESCREVER)
**Prioridade:** Baixa | **Tipo:** Feature | **Tempo:** 30min
> **Contexto:** Precisamos carregar 100 mil produtos de um arquivo CSV para o banco de dados. Usar `session.add()` em um loop está levando horas.
> **Entrada:** Lista de dicionários com dados de produtos.
> **Saída Esperada:** Implementação de inserção via Core (Bulk Insert).

**✅ Critério de Aceite:**
- [ ] Utilizar `insert(ProductTable)` do SQLAlchemy Core.
- [ ] Passar a lista de dicionários diretamente para o método `execute()`.
- [ ] Reduzir o tempo de carga de minutos para segundos.

**💡 Dicas:**
> [!tip] Nível 1
> O ORM é lento para inserções massivas porque ele cria um objeto Python para cada linha. O Core pula essa etapa e envia o SQL bruto.
> 
> [!tip] Nível 2
> Use `session.execute(insert(Product), lista_de_dicts)`.

**🧪 Como Verificar:**
Comparar o tempo de execução entre `session.add()` em loop vs `session.execute(insert(...))`.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/10-SQLAlchemy-Sessoes/01-Aula]] ou [[Python/10-SQLAlchemy-Sessoes/02-Lab]].
