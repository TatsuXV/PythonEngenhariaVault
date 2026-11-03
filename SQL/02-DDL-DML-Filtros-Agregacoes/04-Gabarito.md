---
tipo: gabarito
trilha: SQL
capitulo: 02
titulo: "Resoluções do Capítulo 02"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 02

## 🛠 Lab 02: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
-- Parte A: Update
UPDATE lab_sales 
SET amount = 175.00
WHERE sale_id = 3;

-- Parte B: Delete
DELETE FROM lab_sales 
WHERE amount < 60.00;
```

### 3. Do Zero
```sql
CREATE TABLE lab_products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

INSERT INTO lab_products (product_name, category, price) VALUES
('Notebook', 'Eletrônicos', 3500.00),
('Cadeira Gamer', 'Móveis', 1200.00),
('Mouse Wireless', 'Eletrônicos', 150.00);
```

## 🎫 Tickets: Resoluções

### Ticket SQL-02-01: Consolidação de Vendas
```sql
SELECT product_id, SUM(amount) AS total_sales
FROM lab_sales
GROUP BY product_id
HAVING total_sales > 200.00;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
