---
tipo: entrega
trilha: python
capitulo: 10
titulo: "Entrega: Camada de Dados Aurora"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-05
tags: [entrega, projeto, sqlalchemy, database]
---
# Entrega: Camada de Dados Aurora

> [!abstract] Capítulo 10 · Projeto de Persistência de Dados
> ⏱ 6h · 🎯 Nível 4/5 · 📦 Objetivo: Implementar o sistema de persistência completo da Loja Aurora. · ✅ Verificado

## 🎯 Objetivo do Projeto
Construir a camada de acesso a dados (DAL - Data Access Layer) do ecossistema Aurora. Você deve implementar a modelagem do banco de dados, a gestão de sessões e as operações de CRUD, garantindo a integridade referencial e a performance de consultas.

## 🛠 Requisitos Técnicos

### 1. Modelagem do Banco (ORM)
Implementar as seguintes entidades usando o padrão SQLAlchemy 2.0:
- **Customer:** `customer_id` (PK), `name`, `email` (Unique).
- **Category:** `category_id` (PK), `name`.
- **Product:** `product_id` (PK), `name`, `price`, `category_id` (FK $\rightarrow$ Category).
- **Order:** `order_id` (PK), `customer_id` (FK $\rightarrow$ Customer), `date`, `total_amount`.
- **OrderItem:** `item_id` (PK), `order_id` (FK $\rightarrow$ Order), `product_id` (FK $\rightarrow$ Product), `quantity`.

### 2. Repositórios de Dados
Criar funções de serviço para as seguintes operações:
- `create_customer(name, email)`: Cria e comita um novo cliente.
- `get_customer_orders(customer_id)`: Retorna todos os pedidos de um cliente, carregando os `OrderItems` e `Products` via `joinedload` para evitar o problema N+1.
- `bulk_insert_products(product_list)`: Insere uma lista de produtos usando a API de Core do SQLAlchemy para máxima performance.

### 3. Gestão de Transações
Implementar um fluxo de "Fechamento de Pedido" que:
1. Valida se o cliente tem saldo/crédito.
2. Cria o registro de `Order`.
3. Cria os registros de `OrderItem`.
4. Atualiza o estoque dos produtos.
**Requisito:** Toda a operação deve estar em uma única transação. Se qualquer passo falhar, deve ocorrer um `rollback` completo.

## ✅ Critérios de Aceite
- [ ] Código validado pelo `mypy` com tipagem `Mapped`.
- [ ] Ausência de `DetachedInstanceError` ao acessar relacionamentos.
- [ ] O log do banco (`echo=True`) deve mostrar que a busca de pedidos e itens ocorre em uma única query (JOIN).
- [ ] A inserção de 10k produtos deve levar menos de 5 segundos.

## 🧪 Cenário de Teste
- Inserir 1 cliente e 5 produtos.
- Criar um pedido com 3 itens.
- Simular um erro no último item do pedido e verificar se a `Order` e os itens anteriores foram removidos do banco (Rollback).

## 🏁 Entrega
Submeta o arquivo `database.py` (com modelos e engine) e `services.py` (com as funções de CRUD e transações), junto com um script de teste `test_db.py`.

---
← [[Python/10-SQLAlchemy-Sessoes/06-Revisao]] · [[MOC-Python]] · [[Python/11-APIs-REST-CRUD/01-Aula]] →
