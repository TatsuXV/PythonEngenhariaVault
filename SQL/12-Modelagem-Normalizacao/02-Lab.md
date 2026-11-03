---
tipo: lab
trilha: SQL
capitulo: 12
titulo: "Prática de Normalização e Design Dimensional"
nivel: 5
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, modeling, normalization, star-schema, lab]
---
# Lab: Prática de Normalização e Design Dimensional

> [!abstract] Capítulo 12 · Prática de Normalização e Design Dimensional
> ⏱ 5h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
-- Tabela Desnormalizada (O "Caos")
CREATE TABLE IF NOT EXISTS lab_sales_raw (
    sale_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    customer_email VARCHAR(100),
    product_name VARCHAR(100),
    product_category VARCHAR(50),
    product_price DECIMAL(10,2),
    sale_date DATE,
    amount DECIMAL(10,2)
);

INSERT INTO lab_sales_raw VALUES 
(1, 'Ana Silva', 'ana@email.com', 'Mouse', 'Periféricos', 50.00, '2023-01-01', 50.00),
(2, 'Ana Silva', 'ana@email.com', 'Teclado', 'Periféricos', 150.00, '2023-01-02', 150.00),
(3, 'Bruno Costa', 'bruno@email.com', 'Monitor', 'Telas', 800.00, '2023-01-03', 800.00),
(4, 'Carla Dias', 'carla@email.com', 'Mouse', 'Periféricos', 50.00, '2023-01-04', 50.00);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado da Normalização
> > [!success] Resposta
> > a tabela `lab_sales_raw` será dividida em: `customers`, `products` e `sales`.
> > O nome "Ana Silva" aparecerá apenas UMA vez na tabela de clientes, e não duas vezes na tabela de vendas.
> > **Explicação:** Isso elimina a redundância (1NF $\rightarrow$ 3NF).

```sql
-- Exemplo de criação de tabela normalizada
CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));
CREATE TABLE products (product_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), category VARCHAR(50), price DECIMAL(10,2));
CREATE TABLE sales (sale_id INT PRIMARY KEY, customer_id INT, product_id INT, sale_date DATE, amount DECIMAL(10,2), FOREIGN KEY (customer_id) REFERENCES customers(customer_id), FOREIGN KEY (product_id) REFERENCES products(product_id));
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar um modelo **Star Schema** simplificado. Você deve criar uma tabela de Fato (`fact_sales`) e duas dimensões (`dim_customer`, `dim_product`).

```sql
-- Dimensão Cliente
CREATE TABLE dim_customer (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100),
    name VARCHAR(100)
);

-- Dimensão Produto
CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    # TODO: Adicione as colunas name e category
);

-- Tabela de Fato
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_key INT,
    product_key INT,
    amount DECIMAL(10,2),
    # TODO: Adicione a coluna sale_date
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);
```

## 🚀 3. Do Zero
**Enunciado:** Olhando para a tabela `lab_sales_raw`, escreva a query de migração (ETL) que popula as tabelas normalizadas. Você deve garantir que não haja clientes duplicados ao inserir na tabela `customers`.
**Critério de Aceite:** 
1. Uso de `INSERT INTO ... SELECT DISTINCT`.
2. Integridade referencial mantida (IDs corretos entre as tabelas).

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Tente deletar um cliente que possui vendas na tabela `sales` (com FK ativa) $\rightarrow$ Erro esperado: **Cannot delete or update a parent row**. Explique a importância da Integridade Referencial.
2. Crie uma tabela com a mesma coluna de ID mas sem Primary Key e tente fazer um JOIN $\rightarrow$ Observe a lentidão e a possibilidade de duplicatas.
3. Tente criar um relacionamento 1:N onde a FK é maior que a PK $\rightarrow$ Verifique se o MySQL aceita ou se gera erro de tipo.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
