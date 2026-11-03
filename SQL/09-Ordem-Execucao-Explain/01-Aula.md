---
tipo: aula
trilha: SQL
capitulo: 09
titulo: "Ordem de Execução e EXPLAIN: O Olhar do Otimizador"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, explain, performance, optimization]
comparativo_dialecto: true
---
# Ordem de Execução e EXPLAIN: O Olhar do Otimizador

> [!abstract] Capítulo 09 · Ordem de Execução e EXPLAIN: O Olhar do Otimizador
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[08-Transacoes-Isolamento]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: A ordem em que escrevemos o SQL é a mesma ordem em que o banco o executa?
> ?
> [!question] Pergunta 2: O que significa a coluna `type: ALL` em um resultado do EXPLAIN?
> ?
> [!question] Pergunta 3: Para que serve a coluna `rows` no plano de execução?
> ?

## 🎯 Objetivo
> [!goal]
> Aprender a ler a "mente" do banco de dados, utilizando a ferramenta `EXPLAIN` para identificar gargalos de performance, evitar varreduras completas de tabelas e escrever queries que escalem para milhões de linhas.

## ⚙️ No Pipeline
> [!pipeline]
> No ambiente de desenvolvimento, sua query roda em 0.1s com 100 linhas. Em produção, com 100 milhões de linhas, a mesma query trava o banco. O `EXPLAIN` é a única ferramenta que permite prever esse desastre antes que ele aconteça, revelando se o MySQL está usando índices ou fazendo um Full Table Scan.

## 📚 Teoria

### 1. Ordem Lógica de Execução
O SQL é uma linguagem declarativa (você diz O QUE quer, não COMO fazer). O motor do MySQL reorganiza sua query na seguinte ordem:

1. **FROM** $\rightarrow$ Identifica as tabelas e faz os JOINs.
2. **ON** $\rightarrow$ Filtra as junções.
3. **JOIN** $\rightarrow$ Combina as tabelas.
4. **WHERE** $\rightarrow$ Filtra as linhas individuais.
5. **GROUP BY** $\rightarrow$ Agrupa os dados.
6. **HAVING** $\rightarrow$ Filtra os grupos resultantes.
7. **SELECT** $\rightarrow$ Escolhe as colunas e calcula as expressões.
8. **DISTINCT** $\rightarrow$ Remove duplicatas.
9. **ORDER BY** $\rightarrow$ Ordena o resultado final.
10. **LIMIT** $\rightarrow$ Corta a quantidade de linhas.

**Insight:** É por isso que você não pode usar um alias do `SELECT` no `WHERE` $\rightarrow$ o `WHERE` roda primeiro!

### 2. Desvendando o EXPLAIN
Ao prefixar qualquer query com `EXPLAIN`, o MySQL retorna o plano de execução. As colunas mais importantes são:

- **type (O mais crítico):**
    - `system` / `const`: Acesso ultra rápido (chave primária).
    - `eq_ref` / `ref`: Acesso rápido via índice.
    - `range`: Varredura de um intervalo de índices (ex: `BETWEEN`).
    - `index`: Varredura de todo o índice (melhor que ALL, mas ainda lento).
    - `ALL`: **Full Table Scan**. O banco leu a tabela inteira. Evite a todo custo em produção!

- **possible_keys:** Índices que o MySQL *poderia* usar.
- **key:** O índice que o MySQL *realmente* usou. Se estiver `NULL`, você tem um problema.
- **rows:** Estimativa de quantas linhas o MySQL precisará ler para encontrar o resultado.
- **Extra:** Informações adicionais como `Using filesort` (lento) ou `Using temporary` (muito lento).

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Comando** | `EXPLAIN ANALYZE` (executa a query e dá o tempo real). | `EXPLAIN ANALYZE` (introduzido no MySQL 8.0.18). | Antes do 8.0.18, o MySQL apenas estimava. Agora, ambos podem dar a execução real. |
> | **Planos de Execução** | Exibe a árvore de operações (Sequential Scan $\rightarrow$ Hash Join). | Exibe uma tabela tabular com tipos de acesso (`type`). | O Postgres é mais detalhista sobre a estratégia (Nested Loop vs Hash Join). |
> | **Índices** | Suporta índices GIN e GiST (muito potentes). | Foco em B-Tree. | O MySQL é extremamente otimizado para B-Tree, mas menos versátil em tipos de índice que o Postgres. |

## ⚠️ Armadilhas e Erros Comuns
- **Confiar apenas no `rows`:** O valor de `rows` é uma estimativa. Se as estatísticas da tabela estiverem desatualizadas, o MySQL pode estimar 10 linhas e ler 10 milhões.
- **SARGability:** Escrever queries que impedem o uso de índices. 
    - Ruim: `WHERE YEAR(data) = 2023` (O MySQL não usa o índice da data).
    - Bom: `WHERE data >= '2023-01-01' AND data <= '2023-12-31'`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT * FROM orders WHERE customer_id = 10 ORDER BY date;` (Sem índice em date).
> **Por que está errado:** O `EXPLAIN` mostrará `Using filesort`. Isso significa que o MySQL leu os dados e teve que ordená-los em disco/memória.
> **Correto:** Criar um índice composto `(customer_id, date)` para que o banco já leia os dados ordenados.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Pesquise sobre **Index Cardinality**: Quanto mais únicos forem os valores de uma coluna (ex: CPF), maior a cardinalidade e mais eficiente será o índice. Colunas como "Gênero" têm baixa cardinalidade e índices nelas são quase inúteis.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Optimization](https://dev.mysql.com/doc/refman/8.0/en/optimization.html) (Versão 8.0)

---
← [[08-Transacoes-Isolamento]] · [[MOC-SQL]] · [[10-Indices-BTree]] →
