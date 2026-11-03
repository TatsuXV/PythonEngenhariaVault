---
tipo: aula
trilha: SQL
capitulo: 05
titulo: "CTEs, Views e Tabelas Temporárias"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, cte, views, temporary-tables]
comparativo_dialecto: true
---
# CTEs, Views e Tabelas Temporárias

> [!abstract] Capítulo 05 · CTEs, Views e Tabelas Temporárias
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[04-Window-Functions]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença principal entre uma CTE e uma Subquery?
> ?
> [!question] Pergunta 2: Uma View armazena os dados fisicamente no disco?
> ?
> [!question] Pergunta 3: Qual a vantagem de usar uma Tabela Temporária em um Job de ETL?
> ?

## 🎯 Objetivo
> [!goal]
> Aprender a organizar queries complexas para torná-las legíveis, reutilizáveis e performáticas, utilizando estruturas de modularização de código.

## ⚙️ No Pipeline
> [!pipeline]
> No mundo real, você encontrará queries de 500 linhas. Tentar ler isso sem CTEs é um pesadelo. Como Engenheiro de Dados, você usará CTEs para criar "degraus" de transformação: primeiro limpa os dados, depois agrega, depois filtra, e finalmente entrega o resultado.

## 📚 Teoria

### 1. CTEs (Common Table Expressions)
As CTEs são como "tabelas virtuais temporárias" que existem apenas durante a execução de uma única query. Elas são definidas usando a cláusula `WITH`.

**Vantagens:**
- **Legibilidade:** Substituem subqueries aninhadas por blocos nomeados.
- **Recursividade:** Permitem criar queries que chamam a si mesmas (essencial para hierarquias/árvores).

### 2. Views (Visões)
Uma View é uma query salva no banco de dados. Ela funciona como uma tabela virtual. Quando você faz `SELECT * FROM minha_view`, o MySQL executa a query original por trás.

**Casos de Uso:**
- **Segurança:** Esconder colunas sensíveis de certos usuários.
- **Simplificação:** Transformar um JOIN de 5 tabelas em uma única "tabela virtual" para o usuário final.

### 3. Tabelas Temporárias (`TEMPORARY TABLES`)
Diferente da View ou CTE, a Tabela Temporária armazena dados fisicamente (muitas vezes em memória), mas apenas para a sessão atual do usuário. Quando você desconecta, ela some.

**Quando usar:**
- Quando você precisa processar a mesma massa de dados várias vezes em etapas diferentes de um script.
- Para evitar reprocessar subqueries pesadas repetidamente.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Recursive CTEs** | Suportadas via `WITH RECURSIVE`. | Suportadas via `WITH RECURSIVE` (MySQL 8.0+). | Sintaxe idêntica. |
> | **Materialized Views** | Suporta `MATERIALIZED VIEW` (armazena o resultado fisicamente). | **NÃO suporta nativamente**. | No MySQL, você deve simular isso criando uma tabela real e atualizando-a via Job (Trigger ou Event). |
> | **Temp Tables Scope** | Podem ser locais ou globais. | São locais por sessão. | Ambas são eficientes, mas o MySQL lida muito bem com tabelas temporárias em memória (`MEMORY` engine). |

## ⚠️ Armadilhas e Erros Comuns
- **Performance de Views:** Achar que uma View é rápida. Lembre-se: se a query da View for lenta, qualquer SELECT nela será lento.
- **Uso Excessivo de CTEs:** CTEs não são indexadas. Se você fizer JOIN de duas CTEs gigantes, o MySQL pode ter que materializar os dados em disco, causando lentidão.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT * FROM (SELECT id FROM users) as t1 JOIN (SELECT id FROM logs) as t2 ON t1.id = t2.id;`
> **Por que está errado:** Não está tecnicamente errado, mas é ilegível (subquery aninhada).
> **Correto:** 
> `WITH users_list AS (SELECT id FROM users), logs_list AS (SELECT id FROM logs) SELECT * FROM users_list JOIN logs_list ON users_list.id = logs_list.id;`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude a diferença entre **Logical Views** e **Physical Tables**. No contexto de Big Data (como Spark ou Snowflake), isso é a base para a criação de camadas Bronze, Silver e Gold.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - CTEs](https://dev.mysql.com/doc/refman/8.0/en/with.html) (Versão 8.0)

---
← [[04-Window-Functions]] · [[MOC-SQL]] · [[06-Procedures]] →
