---
tipo: gabarito
trilha: SQL
capitulo: 11
titulo: "Resoluções do Capítulo 11"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, gabarito]
---
# Gabarito: Capítulo 11

## 🛠 Lab 11: Resoluções

### 2. Complete (Fill-in-the-blanks)
```sql
CREATE TABLE lab_logs_region (
    log_id INT NOT NULL,
    region_code VARCHAR(2) NOT NULL,
    message TEXT,
    PRIMARY KEY (log_id, region_code)
) 
PARTITION BY LIST (region_code) (
    PARTITION p_br VALUES IN ('BR'),
    PARTITION p_us VALUES IN ('US'),
    PARTITION p_eu VALUES IN ('FR', 'DE', 'IT', 'ES')
);
```

### 3. Do Zero
```sql
-- 1. Criar tabela particionada
CREATE TABLE lab_sales_yearly (
    sale_id INT NOT NULL,
    sale_date DATE NOT NULL,
    amount DECIMAL(10,2),
    PRIMARY KEY (sale_id, sale_date)
)
PARTITION BY RANGE (YEAR(sale_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);

-- 2. Remover partição antiga instantaneamente
ALTER TABLE lab_sales_yearly DROP PARTITION p2022;
```

## 🎫 Tickets: Resoluções

### Ticket SQL-11-01: Otimização de Arquivamento
```sql
-- 1. Criação da Nova Tabela Particionada
CREATE TABLE event_logs_partitioned (
    event_id INT NOT NULL,
    event_date DATE NOT NULL,
    event_type VARCHAR(50),
    message TEXT,
    PRIMARY KEY (event_id, event_date)
)
PARTITION BY RANGE (YEAR(event_date)) (
    PARTITION p2021 VALUES LESS THAN (2022),
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p_max VALUES LESS THAN MAXVALUE
);

-- 2. Migração de Dados
INSERT INTO event_logs_partitioned SELECT * FROM event_logs;

-- 3. Remoção de dados antigos ( la veloz)
ALTER TABLE event_logs_partitioned DROP PARTITION p2021;
```

---
← [[03-Tickets]] · [[MOC-SQL]] · [[05-Flashcards]] →
