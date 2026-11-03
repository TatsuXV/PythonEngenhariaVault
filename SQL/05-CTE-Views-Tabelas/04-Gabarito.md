---
tipo: gabarito
trilha: SQL
capitulo: 05
titulo: "Resoluções do Capítulo 05"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 05

## 🛠 Lab 05: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
CREATE VIEW vw_high_earners AS
SELECT 
    e.emp_name, 
    d.dept_name
FROM 
    lab_emp e
JOIN lab_dept d ON e.dept_id = d.dept_id
WHERE 
    e.salary > 6000;
```

### 3. Do Zero
```sql
-- Step 1: Criar tabela temporária com dados de Engenharia
CREATE TEMPORARY TABLE temp_eng_employees AS
SELECT e.* 
FROM lab_emp e
JOIN lab_dept d ON e.dept_id = d.dept_id
WHERE d.dept_name = 'Engenharia';

-- Step 2: Consultar com aumento de 10%
SELECT emp_name, salary * 1.1 as new_salary
FROM temp_eng_employees;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-05-01: Refatoração de Faturamento
```sql
WITH vendas_limpas AS (
    SELECT v.cliente_id, v.valor
    FROM vendas v
    WHERE v.status = 'concluido'
),
faturamento_regiao AS (
    SELECT r.regiao_nome, SUM(vl.valor) as total
    FROM vendas_limpas vl
    JOIN clientes c ON vl.cliente_id = c.id
    JOIN regioes r ON c.regiao_id = r.id
    GROUP BY r.regiao_nome
)
SELECT regiao_nome, total 
FROM faturamento_regiao;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
