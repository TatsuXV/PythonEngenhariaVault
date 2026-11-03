---
tipo: lab
trilha: SQL
capitulo: 02
titulo: "Manipulação e Resumo de Dados"
nivel: 2
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, ddl, dml, lab]
---
# Lab: Manipulação e Resumo de Dados

> [!abstract] Capítulo 02 · Manipulação e Resumo de Dados
> ⏱ 3h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
-- Criação de tabela de vendas para agregados
CREATE TABLE IF NOT EXISTS lab_sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    amount DECIMAL(10, 2),
    sale_date DATE
);

INSERT INTO lab_sales (customer_id, product_id, amount, sale_date) VALUES
(1, 101, 150.00, '2023-01-10'),
(1, 102, 50.00, '2023-01-15'),
(2, 101, 150.00, '2023-02-01'),
(3, 103, 300.00, '2023-02-10'),
(3, 101, 150.00, '2023-03-01'),
(4, 102, 50.00, '2023-03-05'),
(5, 101, 150.00, '2023-03-10');
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Retornará o ID do cliente e o valor total gasto por ele. 
> > Cliente 1: 200.00 | Cliente 2: 150.00 | Cliente 3: 450.00 ...
> > **Explicação:** O `GROUP BY` "esmaga" todas as linhas do mesmo cliente em uma só, e o `SUM` soma os valores dessas linhas.

```sql
SELECT customer_id, SUM(amount) AS total_spent
FROM lab_sales
GROUP BY customer_id;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Atualizar o valor da venda `sale_id = 3` para 175.00 e deletar todas as vendas com valor menor que 60.00.

```sql
-- Parte A: Update
UPDATE lab_sales 
SET amount # TODO: Defina o novo valor para 175.00
WHERE sale_id = 3;

-- Parte B: Delete
DELETE FROM lab_sales 
WHERE amount # TODO: Filtre valores menores que 60.00
;
```

**Como verificar:** Execute `SELECT * FROM lab_sales;` e valide se o valor da venda 3 mudou e se as vendas de 50.00 sumiram.

## 🚀 3. Do Zero
**Enunciado:** Crie uma tabela chamada `lab_products` com as colunas: `product_id` (PK, auto-incremento), `product_name` (texto), `category` (texto) e `price` (decimal). Em seguida, insira 3 produtos de categorias diferentes.
**Critério de Aceite:** 
1. Uso correto de `AUTO_INCREMENT`.
2. Tipos de dados adequados (`VARCHAR` e `DECIMAL`).

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. `SELECT customer_id, SUM(amount) FROM lab_sales;` $\rightarrow$ Erro esperado: **Incompatible with sql_mode=only_full_group_by** (ou resultado inconsistente). O MySQL 8.x exige que colunas no SELECT estejam no GROUP BY.
2. `DELETE FROM lab_sales;` $\rightarrow$ Resultado: Apagou TUDO. Explique por que o `WHERE` é vital.
3. `DROP TABLE lab_sales;` $\rightarrow$ Resultado: A tabela sumiu do banco. Diferença para o `TRUNCATE`.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
