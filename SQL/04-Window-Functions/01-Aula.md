---
tipo: aula
trilha: SQL
capitulo: 04
titulo: "Window Functions: A Magia do Analytics"
nivel: 4
tempo_estimado_h: 10
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, window-functions, analytics]
comparativo_dialecto: true
---
# Window Functions: A Magia do Analytics

> [!abstract] Capítulo 04 · Window Functions: A Magia do Analytics
> ⏱ 10h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[03-Join-Having]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença fundamental entre `RANK()` e `DENSE_RANK()`?
> ?
> [!question] Pergunta 2: Para que serve a cláusula `PARTITION BY`?
> ?
> [!question] Pergunta 3: O que acontece se você omitir o `ORDER BY` dentro de um `OVER()`?
> ?

## 🎯 Objetivo
> [!goal]
> Aprender a realizar cálculos complexos sobre conjuntos de linhas relacionados à linha atual, sem a necessidade de agrupar os dados (mantendo a granularidade da tabela original).

## ⚙️ No Pipeline
> [!pipeline]
> Window Functions são a ferramenta favorita de qualquer Analista de Dados e Engenheiro de Dados. Elas são usadas para criar rankings, calcular médias móveis, encontrar a diferença entre a venda de hoje e a de ontem (Growth) e definir janelas de tempo para detecção de anomalias.

## 📚 Teoria

### 1. O Conceito de Window (Janela)
Diferente do `GROUP BY`, que "esmaga" as linhas em um resumo, a Window Function calcula um valor mas mantém todas as linhas originais. A sintaxe base é:
`FUNCAO() OVER (PARTITION BY coluna ORDER BY coluna)`

### 2. Ranking Functions
- `ROW_NUMBER()`: Atribui um número sequencial único para cada linha (1, 2, 3, 4...).
- `RANK()`: Atribui ranking. Se houver empate, pula números (1, 2, 2, 4...).
- `DENSE_RANK()`: Atribui ranking. Se houver empate, NÃO pula números (1, 2, 2, 3...).

### 3. Value Functions (Navegação)
- `LAG()`: Acessa o valor de uma linha **anterior** à linha atual. (Essencial para calcular variação % dia a dia).
- `LEAD()`: Acessa o valor de uma linha **posterior** à linha atual.

### 4. Aggregate Window Functions
Você pode usar `SUM()`, `AVG()`, `COUNT()` com `OVER()`.
- `SUM(valor) OVER (ORDER BY data)`: Cria uma **Soma Acumulada** (Running Total).

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Disponibilidade** | Suporta Window Functions desde versões muito antigas. | Introduzidas apenas no **MySQL 8.0**. | Se você estiver trabalhando com MySQL 5.7 ou inferior, Window Functions NÃO existem (você terá que usar subqueries complexas). |
> | **Sintaxe** | Totalmente compatível com ANSI. | Totalmente compatível com ANSI. | A sintaxe `OVER()` é idêntica em ambos. |
> | **Performance** | Otimizador de janelas extremamente eficiente. | Muito eficiente, mas exige índices nas colunas de `PARTITION BY` e `ORDER BY`. | Crie índices para evitar que o MySQL faça sorting em disco (Temporary Table). |

## ⚠️ Armadilhas e Erros Comuns
- **Lentidão em Bases Gigantes:** Window functions exigem sorting. Se a partição for muito grande, a query ficará lenta.
- **Esquecer o ORDER BY:** Em funções como `ROW_NUMBER()` ou `SUM() OVER()`, o resultado é imprevisível se você não definir a ordem.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT name, RANK() OVER (PARTITION BY city) FROM users;`
> **Por que está errado:** O `RANK()` exige obrigatoriamente um `ORDER BY` para saber quem é o 1º, 2º, etc.
> **Correto:** `SELECT name, RANK() OVER (PARTITION BY city ORDER BY salary DESC) FROM users;`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude sobre **Frames (ROWS BETWEEN ...)**: Como definir se a janela deve considerar apenas a linha atual, as 3 linhas anteriores ou todas as linhas desde o início da partição.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Window Functions](https://dev.mysql.com/doc/refman/8.0/en/window-functions.html) (Versão 8.0)

---
← [[03-Join-Having]] · [[MOC-SQL]] · [[05-CTE-Views-Tabelas]] →
