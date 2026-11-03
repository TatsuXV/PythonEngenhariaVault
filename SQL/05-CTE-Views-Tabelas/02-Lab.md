---
tipo: lab
trilha: SQL
capitulo: 05
titulo: "Modularização de Queries e Persistência Temporária"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, cte, views, lab]
---
# Lab: Modularização de Queries e Persistência Temporária

> [!abstract] Capítulo 05 · Modularização de Queries e Persistência Temporária
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_dept (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS lab_emp (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT,
    salary DECIMAL(10, 2)
);

INSERT INTO lab_dept VALUES (1, 'Engenharia'), (2, 'Vendas'), (3, 'RH');
INSERT INTO lab_emp VALUES 
(101, 'Alice', 1, 8000), 
(102, 'Bob', 1, 7000), 
(103, 'Charlie', 2, 6000), 
(104, 'David', 2, 5000), 
(105, 'Eve', 3, 4000);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Retornará a média salarial por departamento e, em seguida, listará apenas os departamentos cuja média é maior que 5000.
> > Engenharia: 7500 | Vendas: 5500.
> > **Explicação:** A CTE `dept_avg` isola o cálculo da média, tornando a query final limpa.

```sql
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) as avg_sal
    FROM lab_emp
    GROUP BY dept_id
)
SELECT d.dept_name, a.avg_sal
FROM lab_dept d
JOIN dept_avg a ON d.dept_id = a.dept_id
WHERE a.avg_sal > 5000;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar uma View chamada `vw_high_earners` que retorne o nome do funcionário e o nome do departamento para quem ganha mais de 6000.

```sql
CREATE VIEW vw_high_earners AS
SELECT 
    e.emp_name, 
    d.dept_name
FROM 
    lab_emp e
# TODO: Use JOIN para conectar as tabelas
JOIN lab_dept d ON e.dept_id = d.dept_id
WHERE 
    e.salary # TODO: Filtre salários maiores que 6000
;
```

**Como verificar:** `SELECT * FROM vw_high_earners;`

## 🚀 3. Do Zero
**Enunciado:** Utilize uma `TEMPORARY TABLE` para extrair todos os funcionários do departamento de 'Engenharia', salve-os nessa tabela e depois faça um SELECT nessa tabela temporária multiplicando o salário por 1.1 (simulando um aumento de 10%).
**Critério de Aceite:** 
1. Uso de `CREATE TEMPORARY TABLE`.
2. Filtro correto pelo nome do departamento via JOIN.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Tente criar uma View usando a palavra `ORDER BY` no SELECT interno (em versões antigas do MySQL) $\rightarrow$ Verifique se o MySQL 8.0 permite ou se gera aviso.
2. Tente acessar a Tabela Temporária criada em uma nova aba/sessão do MySQL Workbench $\rightarrow$ Erro esperado: **Table '...' doesn't exist**. Explique o escopo de sessão.
3. Crie uma CTE e tente fazer um `UPDATE` nela $\rightarrow$ Erro esperado: CTEs são somente para leitura (READ-ONLY) no contexto de SELECT.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
