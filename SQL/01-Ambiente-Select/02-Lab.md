---
tipo: lab
trilha: SQL
capitulo: 01
titulo: "Prática de Extração Básica"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, select, lab]
---
# Lab: Prática de Extração Básica

> [!abstract] Capítulo 01 · Prática de Extração Básica
> ⏱ 2h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50),
    country VARCHAR(50),
    registration_date DATE
);

INSERT INTO lab_customers (customer_id, first_name, last_name, email, city, country, registration_date) VALUES
(1, 'Alice', 'Silva', 'alice@email.com', 'São Paulo', 'Brasil', '2023-01-15'),
(2, 'Bob', 'Jones', 'bob@email.com', 'New York', 'USA', '2023-02-20'),
(3, 'Charlie', 'Brown', 'charlie@email.com', 'London', 'UK', '2023-03-10'),
(4, 'Diana', 'Prince', 'diana@email.com', 'São Paulo', 'Brasil', '2023-04-05'),
(5, 'Eve', 'Online', 'eve@email.com', 'Berlin', 'Germany', '2023-05-12');
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Retornará os nomes e cidades de todos os clientes do Brasil.
> > **Explicação:** O `WHERE` filtra a coluna `country` antes de selecionar as colunas.

```sql
SELECT first_name, city 
FROM lab_customers 
WHERE country = 'Brasil';
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Selecionar o email e o nome completo (unindo first e last name) de clientes que NÃO moram nos USA.

```sql
SELECT 
    email, 
    CONCAT(first_name, ' ', last_name) AS full_name -- TODO: Use CONCAT para unir nomes
FROM 
    lab_customers
WHERE 
    country # TODO: Filtre para ser DIFERENTE de 'USA'
;
```

**Como verificar:** O resultado deve retornar 4 linhas (Alice, Charlie, Diana, Eve).

## 🚀 3. Do Zero
**Enunciado:** Escreva uma query que retorne a lista de emails de clientes que se registraram no primeiro trimestre de 2023 (entre Janeiro e Março).
**Critério de Aceite:** 
1. Usar a cláusula `BETWEEN`.
2. Apenas a coluna `email` deve ser retornada.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. `SELECT city AS cidade FROM lab_customers WHERE cidade = 'São Paulo';` $\rightarrow$ Erro esperado: **Unknown column 'cidade' in 'where clause'** (Alias não funciona no WHERE).
2. `SELECT * FROM lab_customers WHERE country = "Brasil";` $\rightarrow$ Teste se funciona com aspas duplas no seu MySQL (funciona por padrão, mas não é ANSI).
3. `SELECT first_name FROM lab_customers WHERE country IS 'Brasil';` $\rightarrow$ Erro esperado: **Sintaxe incorreta**. `IS` é usado apenas para `NULL` (`IS NULL`).

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
