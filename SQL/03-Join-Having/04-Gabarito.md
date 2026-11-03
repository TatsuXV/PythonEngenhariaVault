---
tipo: gabarito
trilha: SQL
capitulo: 03
titulo: "Resoluções do Capítulo 03"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 03

## 🛠 Lab 03: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
SELECT 
    c.customer_name, 
    SUM(o.total_amount) AS total_spent
FROM 
    lab_customers_j c
INNER JOIN lab_orders_j o ON c.customer_id = o.customer_id
GROUP BY 
    c.customer_name
HAVING 
    total_spent > 400.00;
```

### 3. Do Zero
```sql
SELECT c.customer_name
FROM lab_customers_j c
LEFT JOIN lab_orders_j o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-03-01: Análise de Churn
```sql
SELECT c.customer_name, c.city
FROM lab_customers_j c
LEFT JOIN lab_orders_j o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
