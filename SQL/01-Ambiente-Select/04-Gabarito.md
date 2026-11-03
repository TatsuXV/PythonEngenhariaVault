---
tipo: gabarito
trilha: SQL
capitulo: 01
titulo: "Resoluções do Capítulo 01"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 01

## 🛠 Lab 01: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
SELECT 
    email, 
    CONCAT(first_name, ' ', last_name) AS full_name
FROM 
    lab_customers
WHERE 
    country <> 'USA'; -- Ou country != 'USA'
```

### 3. Do Zero
```sql
SELECT email 
FROM lab_customers 
WHERE registration_date BETWEEN '2023-01-01' AND '2023-03-31';
```

## 🎫 Tickets: Resoluções

### Ticket SQL-01-01: Extração de Leads
```sql
SELECT email 
FROM lab_customers 
WHERE city = 'São Paulo';
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
