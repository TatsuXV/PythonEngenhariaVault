---
tipo: gabarito
trilha: python
capitulo: 10
titulo: "Gabarito: SQLAlchemy 2.0"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [gabarito, sqlalchemy, orm]
---
# Gabarito: SQLAlchemy 2.0

## 💡 Solução do Lab (Item 2 - Complete)
```python
from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Customer

def get_aurora_customers(session: Session):
    # Statement moderno 2.0
    stmt = select(Customer).where(Customer.email.like('%@aurora.com'))
    
    # Execução e conversão para scalars (objetos Customer)
    return session.execute(stmt).scalars().all()
```
**Raciocínio:** No SQLAlchemy 2.0, o `select()` cria um objeto de query independente da sessão. A sessão então executa esse objeto. O `.scalars()` é necessário porque o `execute()` retorna linhas (Row), e queremos os objetos da classe.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
from sqlalchemy import ForeignKey, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import List

class Base(DeclarativeBase):
    pass

class Category(Base):
    __tablename__ = "categories"
    cat_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    products: Mapped[List["Product"]] = relationship(back_populates="category")

class Product(Base):
    __tablename__ = "products"
    prod_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    cat_id: Mapped[int] = mapped_column(ForeignKey("categories.cat_id"))
    category: Mapped["Category"] = relationship(back_populates="products")

engine = create_engine("sqlite:///:memory:")
Base.metadata.create_all(engine)

def seed_database():
    with Session(engine) as session:
        cat = Category(name="Eletrônicos")
        p1 = Product(name="Teclado", category=cat)
        p2 = Product(name="Mouse", category=cat)
        p3 = Product(name="Monitor", category=cat)
        session.add(cat)
        session.commit()

def get_products_by_category(cat_name: str):
    with Session(engine) as session:
        stmt = select(Product).join(Category).where(Category.name == cat_name)
        return session.execute(stmt).scalars().all()

seed_database()
print(get_products_by_category("Eletrônicos"))
```
**Raciocínio:** O uso de `relationship` permite navegar entre tabelas como se fossem atributos de objetos Python, enquanto o `ForeignKey` garante a integridade referencial no banco de dados.

## 🎫 Soluções dos Tickets

### P10-01: O Pesadelo do N+1
```python
from sqlalchemy.orm import joinedload

# ABORDAGEM RUIM (N+1)
# orders = session.execute(select(Order)).scalars().all()
# for o in orders: print(o.items) # Dispara 1 query por order

# ABORDAGEM BOA (JOINED LOAD)
stmt = select(Order).options(joinedload(Order.items))
orders = session.execute(stmt).scalars().all()
# Agora o acesso a o.items não dispara novas queries!
```

### P10-02: A Transação Fantasma
```python
with Session(engine) as session:
    try:
        # Operação 1: Débito
        customer = session.get(Customer, 1)
        customer.balance -= 100.0
        
        # Operação 2: Pedido
        new_order = Order(customer_id=1, total=100.0)
        session.add(new_order)
        
        # ÚNICO COMMIT para ambas as operações
        session.commit()
    except Exception as e:
        session.rollback() # Desfaz o débito se o pedido falhar
        print(f"Erro na transação: {e}")
```

### P10-03: Inserção Massiva
```python
from sqlalchemy import insert

# Lista de dicionários vinda de um CSV
data = [{"name": f"Prod {i}", "cat_id": 1} for i in range(100000)]

with Session(engine) as session:
    # Inserção via Core (Bulk)
    session.execute(insert(Product), data)
    session.commit()
```
**Raciocínio:** Ao passar a lista de dicionários para o `insert()`, o SQLAlchemy gera um único comando `INSERT INTO ... VALUES (...), (...), ...`, que é ordens de magnitude mais rápido que criar 100k objetos Python.

---
← [[Python/10-SQLAlchemy-Sessoes/03-Tickets]] · [[MOC-Python]] · [[Python/11-APIs-REST-CRUD/01-Aula]] →
