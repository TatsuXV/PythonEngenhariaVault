---
tipo: aula
trilha: SQL
capitulo: 01
titulo: "Ambiente e o Poder do SELECT"
nivel: 1
tempo_estimado_h: 4
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, select, fundamentos]
comparativo_dialecto: true
---
# Ambiente e o Poder do SELECT

> [!abstract] Capítulo 01 · Ambiente e o Poder do SELECT
> ⏱ 4h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Setup-Obsidian]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença fundamental entre `WHERE` e `HAVING`?
> ?
> [!question] Pergunta 2: O que acontece se você usar um Alias de coluna na cláusula `WHERE` no MySQL?
> ?
> [!question] Pergunta 3: Para que serve a cláusula `DISTINCT`?
> ?

## 🎯 Objetivo
> [!goal]
> Configurar o ambiente MySQL 8.x e dominar a extração de dados básica, entendendo a ordem de execução do SQL para evitar erros de sintaxe comuns em migrações de dialetos.

## ⚙️ No Pipeline
> [!pipeline]
> Esta é a base de qualquer Job de ETL. Antes de transformar dados, você precisa extraí-los com precisão. Um `SELECT` mal escrito em produção pode derrubar um banco de dados (Full Table Scan).

## 📚 Teoria

### 1. O Ecossistema MySQL 8.x
O MySQL é um banco de dados relacional (RDBMS) amplamente utilizado em pipelines de dados devido à sua performance de leitura e facilidade de deploy. A versão 8.x trouxe melhorias críticas, como **Window Functions** e **CTEs**, aproximando-o do PostgreSQL.

### 2. Anatomia do SELECT
A estrutura básica de extração é:
```sql
SELECT coluna1, coluna2 
FROM tabela
WHERE condicao;
```

### 3. Alias (Apelidos)
Utilizamos `AS` para renomear colunas ou tabelas, facilitando a leitura de relatórios.
```sql
SELECT nome_cliente AS cliente FROM customers;
```

### 4. Filtragem Básica (WHERE)
O `WHERE` filtra linhas antes que qualquer agrupamento aconteça.
*   `=`, `<>`, `!=`, `<`, `>`, `<=`, `>=`
*   `BETWEEN`, `IN`, `LIKE` (utiliza `%` como wildcard).

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Case Sensitivity** | Identificadores são lowercase por padrão. | Depende do SO (Windows é case-insensitive, Linux é sensitive). | Use sempre lowercase para evitar erros entre dev e prod. |
> | **Casting** | `coluna::text` ou `CAST()` | `CAST(coluna AS tipo)` | MySQL não suporta o operador `::`. Use `CAST`. |
> | **Limit/Offset** | `LIMIT 10 OFFSET 0` | `LIMIT 0, 10` ou `LIMIT 10 OFFSET 0` | MySQL aceita a sintaxe compacta `LIMIT offset, count`. |
> | **Strings** | Aspas simples `'` para strings. | Aspas simples `'` ou duplas `"`. | Recomendado: use sempre aspas simples para compatibilidade ANSI. |

## ⚠️ Armadilhas e Erros Comuns
*   **Referenciar Alias no WHERE:** Você NÃO pode usar um alias criado no `SELECT` dentro do `WHERE`, porque o `WHERE` é processado **antes** do `SELECT`.
*   **Full Table Scan:** Selecionar `*` em tabelas de milhões de linhas em produção. Sempre especifique as colunas.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT nome AS n FROM users WHERE n = 'João';`
> **Por que está errado:** O alias `n` ainda não existe quando o `WHERE` é executado.
> **Correto:** `SELECT nome AS n FROM users WHERE nome = 'João';`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Consulte a documentação oficial do MySQL sobre a **Ordem de Execução do SQL (Logical Query Processing)**:
> `FROM` $\rightarrow$ `ON` $\rightarrow$ `JOIN` $\rightarrow$ `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING` $\rightarrow$ `SELECT` $\rightarrow$ `DISTINCT` $\rightarrow$ `ORDER BY` $\rightarrow$ `LIMIT`

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual](https://dev.mysql.com/doc/refman/8.0/en/) (Versão 8.0)

---
← [[MOC-SQL]] · [[MOC-SQL]] · [[02-DDL-DML-Filtros-Agregacoes]] →
