---
tipo: aula
trilha: python
capitulo: 09
titulo: "Pandas & Parquet: Manipulação de Dados em Escala"
nivel: 4
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [pandas, parquet, dataframe, data-engineering]
---
# Pandas & Parquet: Manipulação de Dados em Escala

> [!abstract] Capítulo 09 · Pandas & Parquet: Manipulação de Dados em Escala
> ⏱ 8h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/08-OOP-Encapsulamento/01-Aula]] · 📦 Entrega: [[Python/09-Pandas-Parquet/07-Entrega-Projeto|Pipeline de Processamento Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Por que usar o formato Parquet em vez de CSV para pipelines de Big Data?
> ?
> [!question] Qual a diferença fundamental entre um `Series` e um `DataFrame` no Pandas?
> ?
> [!question] O que é "Vetorização" no Pandas e por que ela é preferível a loops `for`?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a biblioteca Pandas para limpeza, transformação e agregação de dados, e compreender a importância de formatos de armazenamento colunares (Parquet) para performance e custo de armazenamento em Cloud.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, raramente processamos um registro por vez. Processamos **lotes (batches)**. O Pandas permite que você realize operações em milhões de linhas simultaneamente usando álgebra linear (via NumPy). O Parquet, por sua vez, permite que você leia apenas as colunas necessárias de um arquivo, reduzindo o I/O de disco e acelerando consultas em ferramentas como AWS Athena ou Google BigQuery.

## 📚 Teoria

### 1. O Core do Pandas: DataFrames e Series
O Pandas introduz a estrutura de `DataFrame` (tabela) e `Series` (coluna).

**Operações Essenciais:**
- **Seleção:** `.loc[]` (por rótulo) e `.iloc[]` (por índice).
- **Filtragem:** `df[df['coluna'] > valor]`.
- **Agregação:** `.groupby('coluna').agg({'valor': 'sum'})`.
- **Transformação:** `.apply(lambda x: ...)` (use com cautela) e `.map()`.

### 2. Vetorização vs Loops
**Regra de Ouro:** Nunca use `for index, row in df.iterrows()` para cálculos.
- **Errado:** Loop `for` percorrendo linhas $\rightarrow$ Lento (Python puro).
- **Correto:** Operações vetorizadas $\rightarrow$ Rápido (C/Fortran via NumPy).

```python
# Lento
for i in range(len(df)):
    df.loc[i, 'total'] = df.loc[i, 'preco'] * df.loc[i, 'qtd']

# Rápido (Vetorizado)
df['total'] = df['preco'] * df['qtd']
```

### 3. Formatos de Armazenamento: CSV vs Parquet
| Característica | CSV | Parquet |
| :--- | :--- | :--- |
| **Tipo** | Texto (Linha) | Binário (Coluna) |
| **Compressão** | Baixa | Alta (Snappy/Gzip) |
| **Schema** | Não possui (tudo é string) | Preserva Tipos (int, float, date) |
| **Leitura** | Lê o arquivo todo | Lê apenas colunas selecionadas |
| **Performance** | Lento para arquivos grandes | Ultra rápido para queries |

### 4. Lidando com Dados Ausentes (`NaN`)
Estratégias de tratamento:
- `.isna()` / `.notna()`: Identificar nulos.
- `.fillna(valor)`: Preencher lacunas (ex: média ou zero).
- `.dropna()`: Remover registros incompletos.

## ⚠️ Armadilhas e Erros Comuns
- **SettingWithCopyWarning:** O erro mais comum do Pandas. Ocorre quando você tenta alterar um DataFrame que é, na verdade, uma "fatia" (view) de outro. Use `.copy()` explicitamente.
- **Consumo de RAM:** O Pandas carrega tudo na memória. Para arquivos maiores que a sua RAM, use o parâmetro `chunksize` no `read_csv` ou migre para PySpark/Polars.
- **Tipos Incorretos:** Ler um CSV onde números são interpretados como strings. Use `dtype={...}` no `read_csv`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `.apply()` para todas as transformações de colunas."
> **Por que está errado:** O `.apply()` é essencialmente um loop `for` disfarçado. 
> **Correto:** Sempre busque funções vetorizadas do Pandas ou NumPy antes de recorrer ao `.apply()`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Merge vs Join:** 
> - `merge()`: Similar ao JOIN do SQL (combina DataFrames por colunas comuns).
> - `concat()`: Empilha DataFrames (horizontal ou verticalmente).

## 📖 Fonte
Fonte: [Pandas Documentation](https://pandas.pydata.org/docs/) e [Apache Parquet](https://parquet.apache.org/) (Versão 2.2+)

---
← [[Python/08-OOP-Encapsulamento/01-Aula]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/02-Lab]] →
