---
tipo: lab
trilha: python
capitulo: 10
titulo: "Lab: Persistência com SQLAlchemy 2.0"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [lab, sqlalchemy, orm, database]
---
# Lab: Persistência com SQLAlchemy 2.0

> [!abstract] Capítulo 10 · Lab: Persistência com SQLAlchemy 2.0
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/10-SQLAlchemy-Sessoes/01-Aula]] · 📦 Entrega: [[Python/10-SQLAlchemy-Sessoes/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontece se você adicionar um objeto à sessão com `session.add(user)`, mas o programa cair antes de chamar `session.commit()`?
> > [!success] Resposta
> > Os dados **não serão gravados** no banco de dados.
> > **Explicação:** O SQLAlchemy utiliza transações. O `add()` apenas marca o objeto para ser inserido. A gravação real só ocorre no `commit()`. Se a conexão cair ou houver um erro, o banco faz o rollback automático.

```python
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import Customer # Classe definida no material

engine = create_engine("sqlite:///:memory:") # Banco em memória para teste
Customer.__table__.create() # Cria a tabela

with Session(engine) as session:
    alice = Customer(name="Alice", email="alice@email.com")
    session.add(alice)
    session.commit() 
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a consulta para buscar todos os clientes cujo e-mail termina com `@aurora.com`, utilizando a sintaxe moderna do SQLAlchemy 2.0.

```python
from sqlalchemy import select
from sqlalchemy.orm import Session

# Supomos que a sessão já está aberta
def get_aurora_customers(session: Session):
    # TODO: Criar o statement de select para a classe Customer
    # TODO: Filtrar onde Customer.email termine com '@aurora.com'
    # Dica: Use .where() e .like('%@aurora.com')
    
    # TODO: complete aqui
    stmt = select(Customer).where(Customer.email.like('%@aurora.com'))
    
    # TODO: Executar o statement e retornar os resultados como scalars
    # TODO: complete aqui
    return session.execute(stmt).scalars().all()
```

## 🚀 3. Do Zero
**Enunciado:** Crie um pequeno sistema de persistência para a Loja Aurora.
1. Defina duas classes: `Product` e `Category`.
2. Estabeleça um relacionamento **One-to-Many** (Uma categoria tem muitos produtos).
3. Implemente uma função `seed_database()` que:
    - Crie a categoria "Eletrônicos".
    - Adicione três produtos a essa categoria.
    - Comite a transação.
4. Implemente uma função `get_products_by_category(cat_name)` que retorne todos os produtos de uma categoria específica.

**Critério de Aceite:**
- Uso correto de `Mapped` e `mapped_column`.
- Uso de `relationship` para ligar as classes.
- A função de busca deve retornar instâncias de `Product`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente salvar dois clientes com o mesmo e-mail em uma coluna marcada como `unique=True`** $\rightarrow$ Erro esperado: `IntegrityError`.
2. **Tente acessar um atributo de relacionamento após fechar a sessão** $\rightarrow$ Erro esperado: `DetachedInstanceError`.
3. **Tente fazer um commit de uma sessão que já foi fechada** $\rightarrow$ Erro esperado: `InvalidRequestError`.

---
← [[Python/10-SQLAlchemy-Sessoes/01-Aula]] · [[MOC-Python]] · [[Python/10-SQLAlchemy-Sessoes/03-Tickets]] →
