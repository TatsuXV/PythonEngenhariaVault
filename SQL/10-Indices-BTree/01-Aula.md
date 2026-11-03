---
tipo: aula
trilha: SQL
capitulo: 10
titulo: "Índices B-Tree: A Engenharia da Velocidade"
nivel: 4
tempo_estimado_h: 7
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, btree, indexing, performance]
comparativo_dialecto: true
---
# Índices B-Tree: A Engenharia da Velocidade

> [!abstract] Capítulo 10 · Índices B-Tree: A Engenharia da Velocidade
> ⏱ 7h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[09-Ordem-Execucao-Explain]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: O que é um índice B-Tree e como ele acelera a busca de dados?
> ?
> [!question] Pergunta 2: Qual a diferença entre um Clustered Index e um Non-Clustered Index?
> ?
> [!question] Pergunta 3: Por que criar índices em todas as colunas de uma tabela é uma má ideia?
> ?

## 🎯 Objetivo
> [!goal]
> Compreender a estrutura interna dos índices do MySQL, saber projetar estratégias de indexação eficientes e equilibrar a performance de leitura (SELECT) com o custo de escrita (INSERT/UPDATE/DELETE).

## ⚙️ No Pipeline
> [!pipeline]
> Para um Engenheiro de Dados, índices são como "estradas expressas" para os dados. Se você indexa a coluna errada, o banco continua andando "na terra" (Full Table Scan). Se indexa tudo, o "pedágio" (custo de escrita) torna o carregamento de dados (ETL) insuportavelmente lento.

## 📚 Teoria

### 1. A Estrutura B-Tree (Balanced Tree)
O MySQL (via InnoDB) utiliza a estrutura B-Tree para organizar índices. Imagine uma árvore onde a raiz aponta para ramos, que apontam para folhas.
- Em vez de ler 1 milhão de linhas, o MySQL faz alguns "pulos" na árvore e chega ao dado em 3 ou 4 leituras de disco.
- A B-Tree mantém os dados ordenados, o que a torna perfeita para buscas de igualdade (`=`) e intervalos (`BETWEEN`, `>`, `<`).

### 2. Clustered Index (Índice Agrupado)
No InnoDB, a **Primary Key** é o Clustered Index.
- Os dados da tabela **são a própria folha do índice**.
- Só existe UM Clustered Index por tabela.
- Acessar um dado via PK é a operação mais rápida possível, pois não há "salto" para outro lugar; o dado já está lá.

### 3. Non-Clustered Index (Índice Secundário)
Índices criados via `CREATE INDEX`.
- Eles não contêm os dados da linha, mas sim o valor da coluna indexada + o ponteiro para a Primary Key.
- **Processo:** O MySQL busca o valor no índice secundário $\rightarrow$ encontra a PK $\rightarrow$ vai até o Clustered Index buscar a linha completa. (Isso chama-se *Bookmark Lookup*).

### 4. Índices Compostos e a Regra do Prefixo
Quando você cria um índice em `(coluna_A, coluna_B)`, o MySQL ordena primeiro por A, e depois por B.
- **Funciona:** `WHERE coluna_A = 1` ou `WHERE coluna_A = 1 AND coluna_B = 2`.
- **NÃO funciona:** `WHERE coluna_B = 2` (O índice é ignorado porque você pulou a "porta de entrada" A).

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Heap vs Clustered** | Usa "Heaps" (os dados ficam em qualquer lugar, o índice aponta para o TID). | Usa "Clustered" (os dados ficam ordenados pela PK). | O MySQL é geralmente mais rápido para buscas por PK, mas o Postgres pode ser mais flexível em updates massivos. |
> | **Index Types** | GIN, GiST, BRIN, B-Tree. | B-Tree (padrão), Full-Text, Spatial. | Para buscas de texto complexas, o Postgres é superior. No MySQL, use Full-Text Indices. |
> | **Index-Only Scan** | Muito eficiente através do Index Only Scan. | Também suporta (Covering Index). | Se você selecionar apenas colunas que fazem parte do índice, o MySQL não precisa ir até a tabela principal. |

## ⚠️ Armadilhas e Erros Comuns
- **Low Cardinality:** Indexar colunas como "Sexo" ou "Ativo/Inativo". O MySQL verá que 50% da tabela é 'M' e decidirá que é mais rápido fazer um Full Table Scan do que usar o índice.
- **Over-Indexing:** Ter 20 índices em uma tabela de 5 colunas. Cada `INSERT` terá que atualizar 20 árvores diferentes, matando a performance do seu pipeline de ingestão.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `CREATE INDEX idx_name ON users(last_name, first_name);` $\rightarrow$ Buscar por `first_name` usando este índice.
> **Por que está errado:** Viola a regra do prefixo. O índice está ordenado por sobrenome primeiro.
> **Correto:** Criar um índice separado para `first_name` ou mudar a ordem do índice composto dependendo de qual coluna é mais usada sozinha.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude o conceito de **Covering Index**. Se sua query é `SELECT nome FROM users WHERE id = 10` e você tem um índice em `(id, nome)`, o MySQL retorna o nome direto do índice sem sequer tocar na tabela. Isso é a performance máxima.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Optimization - Indexes](https://dev.mysql.com/doc/refman/8.0/en/optimization-indexes.html) (Versão 8.0)

---
← [[09-Ordem-Execucao-Explain]] · [[MOC-SQL]] · [[11-Particionamento]] →
