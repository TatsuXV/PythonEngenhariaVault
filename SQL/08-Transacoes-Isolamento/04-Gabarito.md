---
tipo: gabarito
trilha: SQL
capitulo: 08
titulo: "Resoluções do Capítulo 08"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 08

## 🛠 Lab 08: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
START TRANSACTION;

UPDATE lab_bank_accounts 
SET balance = balance - 500 
WHERE account_id = 1;

ROLLBACK;
```

### 3. Do Zero
```sql
START TRANSACTION;

-- Passo 1: Retira de Alice
UPDATE lab_bank_accounts SET balance = balance - 200 WHERE account_id = 1;

-- Passo 2: Marca ponto de salvamento
SAVEPOINT depois_do_primeiro_passo;

-- Passo 3: Tenta retirar de Bob (simulando erro)
UPDATE lab_bank_accounts SET balance = balance - 200 WHERE account_id = 2;

-- Passo 4: Desiste da segunda operação
ROLLBACK TO SAVEPOINT depois_do_primeiro_passo;

-- Passo 5: Confirma a transação
COMMIT;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-08-01: Garantia de Carga Atômica
```sql
START TRANSACTION;

-- 1. Limpeza (Usando DELETE para permitir ROLLBACK, pois TRUNCATE é DDL)
DELETE FROM fact_sales;

-- 2. Carga
INSERT INTO fact_sales (order_id, amount, date)
SELECT order_id, amount, date FROM stg_sales;

-- Se tudo correr bem
COMMIT;
-- Caso ocorra erro em qualquer etapa: ROLLBACK;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
