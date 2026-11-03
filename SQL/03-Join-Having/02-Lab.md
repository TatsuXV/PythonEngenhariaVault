---
tipo: lab
trilha: SQL
capitulo: 03
titulo: "Prática de Junções e Filtros de Grupo"
nivel: 3
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, joins, lab]
---
# Lab: Prática de Junções e Filtros de Grupo

> [!abstract] Capítulo 03 · Prática de Junções e Filtros de Grupo
> ⏱ 4h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
-- Tabela de Clientes
CREATE TABLE IF NOT EXISTS lab_customers_j (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);

-- Tabela de Pedidos
CREATE TABLE IF NOT EXISTS lab_orders_j (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

INSERT INTO lab_customers_j (customer_id, customer_name, city) VALUES
(1, 'Ana Silva', 'São Paulo'),
(2, 'Bruno Costa', 'Rio de Janeiro'),
(3, 'Carla Dias', 'Belo Horizonte'),
(4, 'Daniel Oliveira', 'Curitiba'),
(5, 'Eduarda Lima', 'São Paulo');

INSERT INTO lab_orders_j (order_id, customer_id, order_date, total_amount) VALUES
(101, 1, '2023-01-10', 250.00),
(102, 1, '2023-02-15', 100.00),
(103, 2, '2023-03-01', 500.00),
(104, 3, '2023-03-10', 150.00),
(105, 1, '2023-04-05', 300.00);
-- Note que Daniel(4) e Eduarda(5) não possuem pedidos.
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Retornará todos os clientes, independentemente de terem feito pedidos. 
> > Ana, Bruno, Carla aparecerão com seus pedidos. Daniel e Eduarda aparecerão com `NULL` nas colunas do pedido.
> > **Explicação:** O `LEFT JOIN` preserva a tabela da esquerda.

```sql
SELECT c.customer_name, o.order_id
FROM lab_customers_j c
LEFT JOIN lab_orders_j o ON c.customer_id = o.customer_id;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Retornar o nome do cliente e o valor total gasto, mas apenas para clientes que gastaram mais de 400.00 no total.

```sql
SELECT 
    c.customer_name, 
    SUM(o.total_amount) AS total_spent
FROM 
    lab_customers_j c
# TODO: Use INNER JOIN para pegar apenas quem tem pedidos
JOIN lab_orders_j o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_name
# TODO: Use HAVING para filtrar a soma total
total_spent > 400.00;
```

## 🚀 3. Do Zero
**Enunciado:** Escreva uma query que retorne a lista de clientes (nome) que **NUNCA** fizeram um pedido.
**Critério de Aceite:** 
1. Usar `LEFT JOIN`.
2. Filtrar no `WHERE` onde a chave da tabela da direita seja `NULL`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. `SELECT c.customer_name, o.total_amount FROM lab_customers_j c LEFT JOIN lab_orders_j o ON c.customer_id = o.customer_id WHERE o.total_amount > 200;` $\rightarrow$ Resultado: Perdeu os clientes sem pedidos. Explique por que o `WHERE` matou o `LEFT JOIN`.
2. `SELECT * FROM lab_customers_j CROSS JOIN lab_orders_j;` $\rightarrow$ Resultado: 5 clientes * 5 pedidos = 25 linhas. Explique a periculosidade disso em tabelas de 1 milhão de linhas.
3. `SELECT c.customer_name FROM lab_customers_j c JOIN lab_orders_j o ON c.customer_id = o.customer_id;` $\rightarrow$ Teste se `JOIN` funciona como `INNER JOIN`.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
