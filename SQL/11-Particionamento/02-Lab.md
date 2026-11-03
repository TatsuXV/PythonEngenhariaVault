---
tipo: lab
trilha: SQL
capitulo: 11
titulo: "Implementando Estratégias de Particionamento"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, partitioning, lab]
---
# Lab: Implementando Estratégias de Particionamento

> [!abstract] Capítulo 11 · Implementando Estratégias de Particionamento
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
-- Tabela de logs sem particionamento para comparação
CREATE TABLE lab_logs_simple (
    log_id INT NOT NULL,
    log_date DATE NOT NULL,
    message TEXT,
    PRIMARY KEY (log_id, log_date)
);

-- Inserindo dados de anos diferentes
INSERT INTO lab_logs_simple VALUES 
(1, '2022-05-10', 'Erro de conexão'),
(2, '2022-11-20', 'Timeout de API'),
(3, '2023-01-15', 'Sucesso no upload'),
(4, '2023-06-01', 'Erro de permissão'),
(5, '2024-02-10', 'Login efetuado');
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado do EXPLAIN
> > [!success] Resposta
> > O `partitions` na saída do EXPLAIN mostrará apenas a partição correspondente ao ano de 2024.
> > **Explicação:** Isso é o **Partition Pruning**. O MySQL ignora as partições de 2022 e 2023.

```sql
CREATE TABLE lab_logs_partitioned (
    log_id INT NOT NULL,
    log_date DATE NOT NULL,
    message TEXT,
    PRIMARY KEY (log_id, log_date)
) 
PARTITION BY RANGE (YEAR(log_date)) (
    PARTITION p2022 VALUES LESS THAN (2023),
    PARTITION p2023 VALUES LESS THAN (2024),
    PARTITION p2024 VALUES LESS THAN (2025)
);

INSERT INTO lab_logs_partitioned VALUES 
(1, '2022-05-10', 'Erro de conexão'),
(2, '2022-11-20', 'Timeout de API'),
(3, '2023-01-15', 'Sucesso no upload'),
(4, '2023-06-01', 'Erro de permissão'),
(5, '2024-02-10', 'Login efetuado');

EXPLAIN SELECT * FROM lab_logs_partitioned WHERE log_date >= '2024-01-01';
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Implementar um particionamento do tipo **LIST** para dividir os logs por região (Brasil, USA, Europa).

```sql
CREATE TABLE lab_logs_region (
    log_id INT NOT NULL,
    region_code VARCHAR(2) NOT NULL,
    message TEXT,
    PRIMARY KEY (log_id, region_code)
) 
PARTITION BY # TODO: Defina o tipo de particionamento como LIST
 (region_code) (
    PARTITION p_br VALUES IN ('BR'),
    PARTITION p_us VALUES IN ('US'),
    PARTITION p_eu VALUES IN ('FR', 'DE', 'IT', 'ES')
);
```

**Como verificar:** Insira um registro com `region_code = 'BR'` e use `EXPLAIN` para verificar se ele caiu na partição `p_br`.

## 🚀 3. Do Zero
**Enunciado:** Crie uma tabela particionada por **RANGE** para vendas anuais. Em seguida, simule a "limpeza de dados históricos" removendo a partição mais antiga do banco de dados.
**Critério de Aceite:** 
1. Usar `ALTER TABLE ... DROP PARTITION`.
2. Provar que a remoção foi instantânea comparada a um `DELETE`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Tente criar uma tabela particionada onde a coluna de partição NÃO faz parte da Primary Key $\rightarrow$ Erro esperado: **A PRIMARY KEY must include all columns in the table's partitioning function**. Explique por que o MySQL exige isso.
2. Tente inserir um dado que não se encaixa em nenhuma partição definida (ex: ano 2030) $\rightarrow$ Erro esperado: **Table has no partition for value...**. Solução: Adicionar uma partição `MAXVALUE`.
3. Tente fazer um `UPDATE` que altera a coluna de partição de um registro (mudando o ano de 2022 para 2024) $\rightarrow$ Verifique se o MySQL move a linha automaticamente para a nova partição ou se gera erro.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
