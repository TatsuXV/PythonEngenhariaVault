---
tipo: gabarito
trilha: SQL
capitulo: 09
titulo: "Resoluções do Capítulo 09"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 09

## 🛠 Lab 09: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
-- Parte A: Forma ERRADA (Não SARGável)
EXPLAIN SELECT * FROM lab_big_orders 
WHERE YEAR(order_date) = 2023;

-- Parte B: Forma CORRETA (SARGável)
EXPLAIN SELECT * FROM lab_big_orders 
WHERE order_date >= '2023-01-01' AND order_date <= '2023-12-31';
```

### 3. Do Zero
```sql
-- Query original
EXPLAIN SELECT * FROM lab_big_orders WHERE customer_id = 10 ORDER BY order_date;
-- Resultado: 'Using filesort' no Extra.

-- Solução: Criar índice composto
CREATE INDEX idx_cust_date ON lab_big_orders(customer_id, order_date);

-- Nova verificação
EXPLAIN SELECT * FROM lab_big_orders WHERE customer_id = 10 ORDER BY order_date;
-- Resultado: 'Using index' ou desaparece o 'Using filesort'.
```

## 🎫 Tickets: Resoluções

### Ticket SQL-09-01: Otimização de Relatório
```sql
-- Query Refatorada
EXPLAIN SELECT order_id, total_amount 
FROM fact_sales 
WHERE order_date >= '2023-05-01' AND order_date <= '2023-05-31'
ORDER BY order_date;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
