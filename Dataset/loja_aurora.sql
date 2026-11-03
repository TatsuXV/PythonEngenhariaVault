-- Dump SQL Loja Aurora
CREATE TABLE customers (customer_id INT PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), city VARCHAR(50), created_at TIMESTAMP);
CREATE TABLE products (product_id INT PRIMARY KEY, name VARCHAR(100), category VARCHAR(50), price NUMERIC(10,2));
CREATE TABLE orders (order_id INT PRIMARY KEY, customer_id INT, order_date TIMESTAMP, status VARCHAR(20), total_amount NUMERIC(10,2));
CREATE TABLE order_items (item_id INT PRIMARY KEY, product_id INT, order_id INT, quantity INT, unit_price NUMERIC(10,2));
CREATE TABLE logs (log_id INT PRIMARY KEY, customer_id INT, event_type VARCHAR(20), timestamp TIMESTAMP, user_agent VARCHAR(50));

-- Amostras de dados
