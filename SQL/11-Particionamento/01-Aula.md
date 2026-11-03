---
tipo: aula
trilha: SQL
capitulo: 11
titulo: "Particionamento: Lidando com Tabelas Massivas"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, partitioning, big-data, scalability]
comparativo_dialecto: true
---
# Particionamento: Lidando com Tabelas Massivas

> [!abstract] Capítulo 11 · Particionamento: Lidando com Tabelas Massivas
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[10-Indices-BTree]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença entre Sharding e Particionamento?
> ?
> [!question] Pergunta 2: O que é "Partition Pruning" e por que ele é vital para a performance?
> ?
> [!question] Pergunta 3: Posso criar um índice que ignore a partição da tabela?
> ?

## 🎯 Objetivo
> [!//goal]
> Aprender a dividir tabelas com bilhões de linhas em pedaços menores e gerenciáveis, melhorando a performance de queries e facilitando a manutenção de dados históricos (arquivamento).

## ⚙️ No Pipeline
> [!pipeline]
> No mundo de Big Data, deletar 100 milhões de linhas com `DELETE FROM` pode travar o banco por horas devido aos logs de transação. Com particionamento, você simplesmente dá um `DROP PARTITION` e remove milhões de linhas em milissegundos. É a diferença entre "limpar a casa com uma pinça" e "trocar o saco de lixo".

## 📚 Teoria

### 1. O Conceito de Particionamento
O particionamento divide a tabela logicamente em várias tabelas menores (partições), mas para o usuário, ela continua parecendo uma tabela única. O MySQL decide em qual partição o dado deve ser gravado ou lido com base em uma **Partition Key**.

### 2. Tipos de Particionamento
- **RANGE (Intervalo):** Divide os dados com base em valores. Ex: Partição por ano (`2022`, `2023`, `2024`). É o mais comum para dados temporais.
- **LIST (Lista):** Divide os dados com base em uma lista de valores. Ex: Partição por região (`Sul`, `Norte`, `Leste`, `Oeste`).
- **HASH:** O MySQL usa um algoritmo de hash para distribuir os dados uniformemente entre um número fixo de partições. Útil para evitar "hotspots" de escrita.
- **KEY:** Similar ao HASH, mas usa a chave primária ou índices existentes.

### 3. Partition Pruning (Poda de Partição)
É a capacidade do otimizador de ignorar partições que não contêm os dados solicitados. 
Exemplo: Se você filtra `WHERE data >= '2024-01-01'`, o MySQL "poda" as partições de 2022 e 2023 e lê apenas a de 2024. Isso reduz drasticamente a IO de disco.

### 4. Manutenção de Dados (Lifecycle)
O particionamento facilita o **Data Retention**:
- Em vez de `DELETE FROM logs WHERE data < '2023-01-01'`, que gera milhões de logs de undo, você usa:
`ALTER TABLE logs DROP PARTITION p2022;` $\rightarrow$ Operação instantânea.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Arquitetura** | Usa "Declarative Partitioning" (Tabela Pai $\rightarrow$ Tabelas Filhas). | As partições são internas ao motor de armazenamento (InnoDB). | O Postgres é mais flexível para mudar a estratégia de partição depois de criada. |
> | **Índices** | Pode ter índices globais ou locais por partição. | Os índices são **locais** a cada partição. | No MySQL, se você buscar por uma coluna NÃO particionada, ele terá que ler o índice de TODAS as partições. |
> | **Automaticidade** | Exige a criação manual de cada partição filha. | Permite a criação de múltiplas partições em um único comando. | Ambos exigem que o DE gerencie a criação de novas partições (ex: criar a partição de 2025 antes do ano começar). |

## ⚠️ Armadilhas e Erros Comuns
- **A Chave de Partição na PK:** No MySQL, toda coluna usada no particionamento **DEVE** fazer parte de todas as Primary Keys e Unique Keys da tabela. Isso é a maior dor de cabeça ao migrar tabelas existentes para particionadas.
- **Over-partitioning:** Criar 1000 partições pequenas pode deixar o otimizador lento. Encontre o equilíbrio (ex: partições mensais ou anuais).

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `CREATE TABLE logs (...) PARTITION BY RANGE (year(data)) (PARTITION p0 VALUES LESS THAN (2023));`
> **Por que está errado:** O MySQL exige que a função de particionamento retorne um inteiro. O `year()` funciona, mas a sintaxe precisa ser exata.
> **Correto:** Certifique-se de que a coluna `data` seja do tipo `DATE` ou `DATETIME` e a função seja suportada.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Pesquise sobre **Sharding**. Enquanto o Particionamento divide a tabela em um único servidor, o Sharding divide a tabela em múltiplos servidores físicos.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Partitioning](https://dev.mysql.com/doc/refman/8.0/en/partitioning.html) (Versão 8.0)

---
← [[10-Indices-BTree]] · [[MOC-SQL]] · [[12-Modelagem-Normalizacao]] →
