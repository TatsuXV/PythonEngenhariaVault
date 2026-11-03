---
tipo: aula
trilha: python
capitulo: 10
titulo: "SQLAlchemy 2.0 & Sessões: Persistência Profissional"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [sqlalchemy, orm, database, python-sql]
---
# SQLAlchemy 2.0 & Sessões: Persistência Profissional

> [!abstract] Capítulo 10 · SQLAlchemy 2.0 & Sessões
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/08-OOP-Encapsulamento/01-Aula]] e [[SQL/02-DDL-DML-Filtros-Agregacoes/01-Aula]] · 📦 Entrega: [[Python/10-SQLAlchemy-Sessoes/07-Entrega-Projeto|Camada de Dados Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença entre o Core do SQLAlchemy e o ORM?
> ?
> [!question] O que é o "Unit of Work" (Unidade de Trabalho) no contexto de sessões (`Session`)?
> ?
> [!question] Por que a versão 2.0 do SQLAlchemy mudou a forma de escrever queries (estilo `select()` vs `.query()`)?
> ?

## 🎯 Objetivo
> [!goal]
> Implementar a persistência de dados utilizando o SQLAlchemy 2.0, transitando entre a manipulação de objetos Python e tabelas SQL, com foco em gestão de sessões, transações e performance de inserção.

## ⚙️ No Pipeline
> [!pipeline]
> Em pipelines de dados, você não quer escrever strings de SQL manualmente dentro do Python (isso é propenso a erros e SQL Injection). O SQLAlchemy atua como a ponte: ele permite que você defina a estrutura do banco como classes Python e execute queries tipadas. A gestão correta da `Session` garante que sua transação seja atômica: ou tudo é gravado no banco, ou nada é (Rollback), evitando dados corrompidos.

## 📚 Teoria

### 1. Core vs ORM
- **Core:** Focado em SQL. Você trabalha com tabelas e esquemas. É mais rápido e próximo do banco.
- **ORM (Object-Relational Mapper):** Focado em Objetos. Você trabalha com classes. É mais produtivo e mantém a consistência do domínio.

### 2. Declarative Mapping (O Novo Padrão 2.0)
No SQLAlchemy 2.0, utilizamos `Mapped` e `mapped_column` para tipagem rigorosa.

```python
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customers"
    
    customer_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
```

### 3. A Gestão da Sessão (`Session`)
A `Session` é o espaço de trabalho. Ela rastreia as mudanças nos objetos.

**Fluxo de Trabalho:**
1. **Criar Engine:** `create_engine("postgresql://...")`
2. **Abrir Sessão:** `Session(engine)`
3. **Operações:** `session.add(obj)`, `session.execute(select(...))`
4. **Commit:** `session.commit()` (Grava no banco) ou `session.rollback()` (Cancela tudo).

### 4. Queries no Estilo 2.0
O estilo `.query(User).filter(...)` foi depreciado em favor do `select()`.

```python
from sqlalchemy import select

# Forma moderna (2.0)
stmt = select(Customer).where(Customer.name == "Alice")
result = session.execute(stmt).scalars().all()
```

## ⚠️ Armadilhas e Erros Comuns
- **Sessões Esquecidas:** Abrir sessões e não fechá-las (`session.close()`), esgotando o pool de conexões do banco.
- **Lazy Loading:** Tentar acessar um relacionamento (ex: `order.items`) depois que a sessão foi fechada $\rightarrow$ `DetachedInstanceError`. Use `joinedload` para carregar dados antecipadamente.
- **N+1 Problem:** Executar uma query para cada item de uma lista. Solução: Usar `JOIN` via SQLAlchemy para trazer tudo em uma única chamada.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `session.add_all()` para inserir 1 milhão de registros."
> **Por que está errado:** O ORM rastreia cada objeto na memória, tornando a inserção massiva extremamente lenta.
> **Correto:** Para bulk inserts (milhares de linhas), use o **Core** (`insert(Table).values([...])`) ou a API de `bulk_insert_mappings` do ORM.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Migrations com Alembic:** Em projetos reais, você não usa `Base.metadata.create_all()`. Você usa o **Alembic** para versionar as mudanças no schema do banco (estilo Git para o banco de dados).

## 📖 Fonte
Fonte: [SQLAlchemy 2.0 Documentation](https://docs.sqlalchemy.org/en/20/)

---
← [[Python/09-Pandas-Parquet/01-Aula]] · [[MOC-Python]] · [[Python/10-SQLAlchemy-Sessoes/02-Lab]] →
