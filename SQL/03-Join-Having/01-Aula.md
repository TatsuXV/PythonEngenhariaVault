---
tipo: aula
trilha: SQL
capitulo: 03
titulo: "Joins: Conectando o Mundo dos Dados"
nivel: 3
tempo_estimado_h: 8
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, joins, relationships]
comparativo_dialecto: true
---
# Joins: Conectando o Mundo dos Dados

> [!abstract] Capítulo 03 · Joins: Conectando o Mundo dos Dados
> ⏱ 8h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[02-DDL-DML-Filtros-Agregacoes]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença fundamental entre um `LEFT JOIN` e um `INNER JOIN`?
> ?
> [!question] Pergunta 2: O que acontece se houver múltiplas correspondências para a mesma chave em um JOIN?
> ?
> [!question] Pergunta 3: Quando devemos usar um `CROSS JOIN` em pipelines de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a arte de combinar dados de múltiplas tabelas, entendendo as diferentes estratégias de junção e como evitar a explosão de linhas (Cartesian Product) em bases de larga escala.

## ⚙️ No Pipeline
> [!pipeline]
> Na vida real, os dados nunca estão em uma única tabela. Para criar um Data Mart ou alimentar um Dashboard, você passará 80% do seu tempo fazendo JOINs entre tabelas de Dimensão (ex: Clientes) e tabelas de Fato (ex: Vendas).

## 📚 Teoria

### 1. O Conceito de Relacionamento
O SQL baseia-se em chaves. O `JOIN` conecta a **Foreign Key (FK)** de uma tabela à **Primary Key (PK)** de outra.

### 2. Tipos de Joins
- **INNER JOIN:** Retorna apenas as linhas onde há correspondência em AMBAS as tabelas. (Intersecção).
- **LEFT JOIN (ou LEFT OUTER JOIN):** Retorna TODAS as linhas da tabela da esquerda, e as correspondentes da direita. Se não houver correspondência, preenche com `NULL`. (Essencial para encontrar "buracos" nos dados).
- **RIGHT JOIN:** O inverso do LEFT JOIN. (Raramente usado, geralmente substituímos por LEFT JOIN invertendo a ordem das tabelas).
- **CROSS JOIN:** Cria um produto cartesiano (cada linha de A com cada linha de B). Cuidado: em tabelas grandes, isso pode travar o servidor.

### 3. Self Join
É quando juntamos uma tabela com ela mesma. Útil para hierarquias (ex: Tabela de Funcionários onde uma coluna é o `id_gestor`, que também é um funcionário).

### 4. Filtragem de Grupos: HAVING vs WHERE
Como vimos no capítulo anterior, o `HAVING` filtra o resultado de agregados. Quando usamos Joins, o `HAVING` é fundamental para filtrar grupos resultantes da junção de várias tabelas.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Full Outer Join** | Suportado nativamente via `FULL OUTER JOIN`. | **NÃO suportado nativamente**. | Para simular um FULL JOIN no MySQL, você deve fazer um `LEFT JOIN` e um `RIGHT JOIN` unidos por um `UNION`. |
> | **Join Performance** | Otimizador muito robusto para Hash Joins. | Depende muito dos índices (B-Tree). | No MySQL, a ausência de índices nas colunas do JOIN causa lentidão extrema (Full Table Scan). |
> | **Sintaxe de Junção** | Aceita `JOIN` como sinônimo de `INNER JOIN`. | Aceita `JOIN` como sinônimo de `INNER JOIN`. | Ambos seguem o padrão ANSI. |

## ⚠️ Armadilhas e Erros Comuns
- **Explosão de Linhas:** Fazer um JOIN em colunas que não são únicas, resultando em milhões de linhas inesperadas.
- **Filtrar LEFT JOIN no WHERE:** Se você colocar um filtro da tabela da direita no `WHERE`, você transforma seu `LEFT JOIN` em um `INNER JOIN` acidentalmente (porque o `WHERE` remove os `NULLs`). O correto é colocar o filtro na cláusula `ON`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT * FROM clientes LEFT JOIN vendas ON c.id = v.id_cliente WHERE v.data > '2023-01-01';`
> **Por que está errado:** O `WHERE` filtra os `NULLs` da direita, excluindo clientes que não tiveram vendas.
> **Correto:** `SELECT * FROM clientes LEFT JOIN vendas ON c.id = v.id_cliente AND v.data > '2023-01-01';`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Pesquise sobre **Sargability (Search Argumentable)**: Como escrever cláusulas de JOIN e WHERE que permitam ao MySQL usar índices, evitando o custo computacional de ler a tabela inteira.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Join Types](https://dev.mysql.com/doc/refman/8.0/en/join-types.html) (Versão 8.0)

---
← [[02-DDL-DML-Filtros-Agregacoes]] · [[MOC-SQL]] · [[04-Window-Functions]] →
