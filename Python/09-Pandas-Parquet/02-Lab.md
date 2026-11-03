---
tipo: lab
trilha: python
capitulo: 09
titulo: "Lab: Manipulação de Dados com Pandas & Parquet"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [lab, pandas, parquet]
---
# Lab: Manipulação de Dados com Pandas & Parquet

> [!abstract] Capítulo 09 · Lab: Manipulação de Dados com Pandas & Parquet
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/09-Pandas-Parquet/01-Aula]] · 📦 Entrega: [[Python/09-Pandas-Parquet/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> Dado um DataFrame `df` com as colunas `produto` e `valor`, qual a diferença entre as duas abordagens abaixo?
> 1. `df[df['valor'] > 100]`
> 2. `df.loc[df['valor'] > 100, ['produto']]`
> > [!success] Resposta
> > A primeira opção retorna **todas as colunas** do DataFrame para as linhas onde o valor é maior que 100.
> > A segunda opção retorna **apenas a coluna 'produto'** para essas mesmas linhas.
> > **Explicação:** O `.loc` permite filtrar linhas e selecionar colunas simultaneamente.

```python
import pandas as pd

data = {'produto': ['A', 'B', 'C'], 'valor': [150, 80, 200]}
df = pd.DataFrame(data)

# Filtrando apenas produtos acima de 100
caros = df[df['valor'] > 100]
print(caros) 
# Saída: Produto A e C
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente o código para carregar um CSV, tratar valores nulos na coluna 'preco' (substituindo pela média) e salvar o resultado em Parquet.

```python
import pandas as pd

# 1. Carregar dados
df = pd.read_csv('orders.csv')

# TODO: Identificar nulos na coluna 'preco'
# TODO: complete aqui
nulos = df['preco'].isna().sum()
print(f"Nulos encontrados: {nulos}")

# 2. Tratar Nulos
media_preco = df['preco'].mean()
# TODO: Preencher nulos com a média
# TODO: complete aqui
df['preco'] = df['preco'].fillna(media_preco)

# 3. Salvar em Parquet
# TODO: salvar o dataframe como 'orders.parquet'
# TODO: complete aqui
df.to_parquet('orders.parquet')
```

## 🚀 3. Do Zero
**Enunciado:** Você recebeu dois arquivos: `customers.csv` e `orders.csv`. 
Crie um script que:
1. Carregue ambos os arquivos em DataFrames.
2. Realize um **Merge** (estilo Left Join) para que cada pedido tenha o nome do cliente.
3. Agregue os dados para descobrir o **Total Gasto por Cliente**.
4. Salve o resultado final em um arquivo Parquet chamado `customer_spending.parquet`.

**Critério de Aceite:**
- O merge deve ser feito pela coluna `customer_id`.
- O resultado final deve ter as colunas `customer_name` e `total_spent`.
- O arquivo de saída deve estar no formato Parquet.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente somar uma coluna de números que foi lida como String** $\rightarrow$ Erro esperado: `TypeError` (não é possível somar strings).
2. **Tente acessar uma coluna que não existe via `.loc`** $\rightarrow$ Erro esperado: `KeyError`.
3. **Tente salvar um DataFrame em Parquet sem ter a biblioteca `pyarrow` ou `fastparquet` instalada** $\rightarrow$ Erro esperado: `ImportError`.

---
← [[Python/09-Pandas-Parquet/01-Aula]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/03-Tickets]] →
