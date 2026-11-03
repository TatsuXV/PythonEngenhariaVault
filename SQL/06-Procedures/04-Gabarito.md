---
tipo: gabarito
trilha: SQL
capitulo: 06
titulo: "Resoluções do Capítulo 06"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 06

## 🛠 Lab 06: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
DELIMITER //
CREATE PROCEDURE sp_check_status(IN p_acc_id INT, OUT p_status VARCHAR(20))
BEGIN
    DECLARE v_balance DECIMAL(10,2);
    
    SELECT balance INTO v_balance FROM lab_account_balance WHERE account_id = p_acc_id;
    
    IF v_balance > 0 THEN
        SET p_status = 'POSITIVO';
    ELSE
        SET p_status = 'NEGATIVO';
    END IF;
END //
DELIMITER ;
```

### 3. Do Zero
```sql
DELIMITER //
CREATE PROCEDURE sp_bulk_bonus()
BEGIN
    UPDATE lab_account_balance 
    SET balance = balance * 1.1 
    WHERE balance < 200.00;
END //
DELIMITER ;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-06-01: Automação de Fechamento
```sql
DELIMITER //
CREATE PROCEDURE sp_monthly_closing(OUT p_rows_migrated INT)
BEGIN
    -- 1. Migração
    INSERT INTO sales_history SELECT * FROM sales;
    
    -- Captura a quantidade de linhas migradas
    SET p_rows_migrated = ROW_COUNT();
    
    -- 2. Limpeza
    TRUNCATE TABLE sales;
    
    -- 3. Log
    INSERT INTO closing_logs (closing_date, rows_count) 
    VALUES (NOW(), p_rows_migrated);
END //
DELIMITER ;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
