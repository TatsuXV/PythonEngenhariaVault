---
tipo: gabarito
trilha: SQL
capitulo: 12
titulo: "Resoluções do Capítulo 12"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 12

## 🛠 Lab 12: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
-- Dimensão Produto
CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    product_category VARCHAR(50)
);

-- Tabela de Fato
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    customer_key INT,
    product_key INT,
    amount DECIMAL(10,2),
    sale_date DATE,
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key)
);
```

### 3. Do Zero (ETL de Normalização)
```sql
-- 1. Popula Clientes
INSERT INTO customers (name, email)
SELECT DISTINCT customer_name, customer_email FROM lab_sales_raw;

-- 2. Popula Produtos
INSERT INTO products (name, category, price)
SELECT DISTINCT product_name, product_category, product_price FROM lab_sales_raw;

-- 3. Popula Vendas (Relacionando IDs)
INSERT INTO sales (sale_id, customer_id, product_id, sale_date, amount)
SELECT r.sale_id, c.customer_id, p.product_id, r.sale_date, r.amount
FROM lab_sales_raw r
JOIN customers c ON r.customer_email = c.email
JOIN products p ON r.product_name = p.name;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-12-01: Migração para Star Schema
```sql
-- 1. Criação das Dimensões
CREATE TABLE dim_customer (cust_key INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100));
CREATE TABLE dim_product (prod_key INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100), category VARCHAR(50));

-- 2. Migração de Dados (Desduplicação)
INSERT INTO dim_customer (name, email) SELECT DISTINCT customer_name, customer_email FROM billing_flat;
INSERT INTO dim_product (name, category) SELECT DISTINCT product_name, product_category FROM billing_flat;

-- 3. Popular Fato
CREATE TABLE fact_billing (bill_id INT PRIMARY KEY, cust_key INT, prod_key INT, amount DECIMAL(10,2), bill_date DATE);

INSERT INTO fact_billing (bill_id, cust_key, prod_key, amount, bill_date)
SELECT b.bill_id, c.cust_key, p.prod_key, b.amount, b.bill_date
FROM billing_flat b
JOIN dim_customer c ON b.customer_email = c.email
JOIN dim_product p ON b.product_name = p.name;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
