---
tipo: gabarito
trilha: SQL
capitulo: 10
titulo: "Resoluções do Capítulo 10"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 10

## 🛠 Lab 10: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
-- Step 1: Criar o índice
CREATE INDEX idx_email ON lab_users_idx(email);

-- Step 2: Analisar a query novamente
EXPLAIN SELECT * FROM lab_users_idx WHERE email = 'ana@email.com';
```

### 3. Do Zero
```sql
-- Criação do índice composto
CREATE INDEX idx_city_lname ON lab_users_idx(city, last_name);

-- Query 1: Filtro por cidade (Usa o índice)
EXPLAIN SELECT * FROM lab_users_//idx_users_idx WHERE city = 'São Paulo';

-- Query 2: Filtro apenas por sobrenome (IGNORA o índice)
EXPLAIN SELECT * FROM lab_users_idx WHERE last_name = 'Silva';
```

## 🎫 Tickets: Resoluções

### Ticket SQL-10-01: Otimização de Ingestão
```sql
-- 1. Identificar redundâncias
SHOW INDEX FROM fact_logs;

-- 2. Remover índices redundantes (Exemplo: índice simples que já é prefixo do composto)
DROP INDEX idx_cliente_simples ON fact_logs;

-- 3. Estratégia para carga massiva
-- a) DROP INDEX idx_data ON fact_logs;
-- b) LOAD DATA INFILE ... (Ingestão rápida)
-- c) CREATE INDEX idx_data ON fact_logs(data);
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
