---
tipo: revisao
trilha: python
capitulo: 10
titulo: "Revisão: SQLAlchemy 2.0"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [revisao, sqlalchemy, orm]
---
# Revisão: SQLAlchemy 2.0

> [!abstract] Capítulo 10 · Revisão de Persistência de Dados
> ⏱ 1h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/10-SQLAlchemy-Sessoes/01-Aula]] · 📦 Entrega: [[Python/10-SQLAlchemy-Sessoes/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **Modelagem:** Sei definir classes usando `Mapped` e `mapped_column` no padrão 2.0?
- [ ] **Sessões:** Entendo a diferença entre `add()`, `commit()` e `rollback()`?
- [ ] **Queries:** Consigo escrever selects modernos usando `select().where()`?
- [ ] **Performance:** Sei identificar o problema N+1 e resolvê-lo com `joinedload`?
- [ ] **Escala:** Sei quando usar o ORM vs o Core para inserções massivas (Bulk Inserts)?

## 🧠 Mapa Mental de Conceitos

**SQLAlchemy $\rightarrow$**
- **Definição $\rightarrow$** `DeclarativeBase` $\rightarrow$ `Mapped` $\rightarrow$ `mapped_column`.
- **Operação $\rightarrow$** `Engine` (Conexão) $\rightarrow$ `Session` (Transação) $\rightarrow$ `Commit`.
- **Consultas $\rightarrow$** `select()` $\rightarrow$ `where()` $\rightarrow$ `scalars()`.
- **Relacionamentos $\rightarrow$** `ForeignKey` $\rightarrow$ `relationship()` $\rightarrow$ `joinedload()`.

**Transações $\rightarrow$**
- **Atomicidade $\rightarrow$** Ou tudo ou nada.
- **Isolamento $\rightarrow$** Proteção contra leituras sujas.

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você precisa atualizar o status de 10.000 pedidos para "Enviado". Se você fizer um loop com `session.get()` e `pedido.status = 'Enviado'`, o processo será lento.

**Qual a alternativa performática?**
1. Usar um `update()` do SQLAlchemy Core.
2. `stmt = update(Order).where(Order.status == 'Processando').values(status='Enviado')`.
3. `session.execute(stmt)`.
**Vantagem:** Uma única instrução SQL é enviada ao banco, em vez de 10.000 updates individuais.

## 🔗 Links Rápidos
- Aula Teórica: [[Python/10-SQLAlchemy-Sessoes/01-Aula]]
- Lab Prático: [[Python/10-SQLAlchemy-Sessoes/02-Lab]]
- Tickets de Performance: [[Python/10-SQLAlchemy-Sessoes/03-Tickets]]

---
← [[Python/10-SQLAlchemy-Sessoes/05-Flashcards]] · [[MOC-Python]] · [[Python/10-SQLAlchemy-Sessoes/07-Entrega-Projeto]] →
