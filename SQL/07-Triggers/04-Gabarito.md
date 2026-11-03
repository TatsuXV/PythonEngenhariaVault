---
tipo: gabarito
trilha: SQL
capitulo: 07
titulo: "Resoluções do Capítulo 07"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 07

## 🛠 Lab 07: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
DELIMITER //
CREATE TRIGGER tr_validate_price
BEFORE INSERT ON lab_products_t
FOR EACH ROW
BEGIN
    IF NEW.price < 0 THEN
        SET NEW.price = 0;
    END IF;
END //
DELIMITER ;
```

### 3. Do Zero
```sql
-- Primeiro, adicionar coluna de ação
ALTER TABLE lab_product_logs ADD COLUMN action VARCHAR(50);

DELIMITER //
CREATE TRIGGER tr_update_stock_log
AFTER DELETE ON lab_products_t
FOR EACH ROW
BEGIN
    INSERT INTO lab_product_logs (product_id, action)
    VALUES (OLD.product_id, CONCAT('Produto ', OLD.product_name, ' removido'));
END //
DELIMITER ;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-07-01: Auditoria de Segurança
```sql
DELIMITER //
CREATE TRIGGER tr_audit_salary
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_audit_log (employee_id, old_salary, new_salary, changed_by, changed_at)
        VALUES (OLD.emp_id, OLD.salary, NEW.salary, USER(), NOW());
    END IF;
END //
DELIMITER ;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
