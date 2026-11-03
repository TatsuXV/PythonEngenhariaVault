---
tipo: gabarito
trilha: SQL
capitulo: 04
titulo: "Resoluções do Capítulo 04"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 04

## 🛠 Lab 04: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
SELECT 
    seller_id, 
    amount,
    RANK() OVER (ORDER BY amount DESC) as sales_rank
FROM 
    lab_sales_wf;
```

### 3. Do Zero
```sql
SELECT 
    sale_date, 
    amount, 
    LAG(amount) OVER (PARTITION BY seller_id ORDER BY sale_date) as previous_sale_amount
FROM 
    lab_sales_wf;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-04-01: Análise de Growth
```sql
SELECT 
    seller_id, 
    sale_date, 
    amount,
    amount - LAG(amount) OVER (PARTITION BY seller_id ORDER BY sale_date) as diff_previous_day
FROM 
    lab_sales_wf
ORDER BY 
    seller_id, sale_date;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
