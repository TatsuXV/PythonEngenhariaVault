---
tipo: aula
trilha: SQL
capitulo: 12
titulo: "Modelagem e Normalização: A Arquitetura dos Dados"
nivel: 5
tempo_estimado_h: 10
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, modeling, normalization, star-schema]
comparativo_dialecto: true
---
# Modelagem e Normalização: A Arquitetura dos Dados

> [!abstract] Capítulo 12 · Modelagem e Normalização: A Arquitetura dos Dados
> ⏱ 10h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[11-Particionamento]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença fundamental entre a 1ª, 2ª e 3ª Formas Normais (1NF, 2NF, 3NF)?
> ?
> [!question] Pergunta 2: Por que em Data Warehousing costumamos "desnormalizar" as tabelas?
> ?
> [!question] Pergunta 3: Qual a diferença entre um Star Schema e um Snowflake Schema?
> ?

## 🎯 Objetivo
> [!goal]
> Aprender a projetar bancos de dados eficientes, eliminando redundâncias através da normalização para sistemas transacionais (OLTP) e otimizando a leitura através de modelos dimensionais para sistemas analíticos (OLAP).

## ⚙️ No Pipeline
> [!pipeline]
> Como Engenheiro de Dados, você lidará com dois mundos. No mundo **Transacional (App)**, a normalização é lei para evitar que um dado seja atualizado em um lugar e esquecido em outro. No mundo **Analítico (BI/Data Lake)**, a normalização é o inimigo, pois Joins excessivos matam a performance. Saber transitar entre esses dois modelos é o que define a maturidade de um arquiteto de dados.

## 📚 Teoria

### 1. Normalização (O caminho para o OLTP)
O objetivo é eliminar a redundância e as anomalias de atualização.
- **1ª Forma Normal (1NF):** Eliminar grupos repetidos. Cada célula deve conter apenas um valor atômico. (Ex: Não salvar "Telefones" como uma string separada por vírgula).
- **2ª Forma Normal (2NF):** Estar na 1NF e garantir que todas as colunas não-chave dependam da chave primária *inteira* (não apenas de parte dela em chaves compostas).
- **3ª Forma Normal (3NF):** Estar na 2NF e garantir que nenhuma coluna dependa de outra coluna que não seja a chave primária (eliminar dependências transitivas).

### 2. Modelagem Dimensional (O caminho para o OLAP)
Para análise de dados, usamos a desnormalização para reduzir Joins.
- **Tabelas de Fato (Fact Tables):** Contêm as métricas quantitativas (ex: `valor_venda`, `quantidade`) e chaves estrangeiras para as dimensões.
- **Tabelas de Dimensão (Dimension Tables):** Contêm os atributos descritivos (ex: `nome_produto`, `categoria`, `regiao`).

#### Star Schema vs Snowflake Schema
- **Star Schema:** As dimensões são desnormalizadas. Uma única tabela de `dim_produto` contém tudo. É mais rápido para leitura.
- **Snowflake Schema:** As dimensões são normalizadas. `dim_produto` aponta para `dim_categoria`. Mais organizado, mas exige mais Joins.

### 3. Integridade Referencial
O uso de `FOREIGN KEY` garante que você não tenha "dados orfãos".
- `ON DELETE CASCADE`: Se deletar o cliente, deleta todos os seus pedidos.
- `ON DELETE SET NULL`: Se deletar o cliente, mantém o pedido mas marca o cliente como NULL.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Suporte a JSON** | Tipo `JSONB` extremamente potente com índices GIN. | Tipo `JSON` com funções de busca. | O Postgres é muito superior para modelagem híbrida (Relacional + Documento). No MySQL, use JSON apenas para dados secundários. |
> | **Constraints** | Suporta `CHECK` constraints complexas em versões antigas. | Suporta `CHECK` constraints a partir do 8.0.16. | Verifique a versão do MySQL; versões antigas ignoravam a cláusula `CHECK`. |
> | **Enums** | Tipo `ENUM` é um objeto global no banco. | `ENUM` é definido por coluna. | O MySQL torna a alteração de valores de um ENUM mais simples, mas menos consistente globalmente. |

## ⚠️ Armadilhas e Erros Comuns
- **Over-normalization:** Normalizar demais e acabar com 50 tabelas para representar um simples pedido. Isso torna as queries ilegíveis e lentas.
- **Ignorar a Cardinalidade:** Criar relacionamentos 1:1 desnecessários ou esquecer de tratar relacionamentos N:N (que exigem uma tabela associativa/pivot).

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** Tabela `Pedidos` com a coluna `Nome_Cliente`.
> **Por que está errado:** Viola a 3NF. Se o cliente mudar de nome, você teria que atualizar milhares de linhas na tabela de pedidos.
> **Correto:** Tabela `Pedidos` com `cliente_id` $\rightarrow$ Tabela `Clientes` com `nome`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude o conceito de **Slowly Changing Dimensions (SCD)**. Como lidar com dimensões que mudam ao longo do tempo (ex: um cliente que mudou de cidade)? SCD Tipo 1 (Sobrescrever), Tipo 2 (Novo registro com data) e Tipo 3 (Nova coluna).

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Data Modeling](https://dev.mysql.com/doc/refman/8.0/en/index.html) (Versão 8.0)

---
← [[11-Particionamento]] · [[MOC-SQL]] · [[Simulado-SQL]] →
