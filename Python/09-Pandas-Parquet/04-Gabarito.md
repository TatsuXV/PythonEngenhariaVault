---
tipo: gabarito
trilha: python
capitulo: 09
titulo: "Gabarito: Pandas & Parquet"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [gabarito, pandas, parquet]
---
# Gabarito: Pandas & Parquet

## 💡 Solução do Lab (Item 2 - Complete)
```python
import pandas as pd

# 1. Carregar dados
df = pd.read_csv('orders.csv')

# Identificar nulos na coluna 'preco'
nulos = df['preco'].isna().sum()
print(f"Nulos encontrados: {nulos}")

# 2. Tratar Nulos
media_preco = df['preco'].mean()
# Preencher nulos com a média
df['preco'] = df['preco'].fillna(media_preco)

# 3. Salvar em Parquet
df.to_parquet('orders.parquet', engine='pyarrow')
```
**Raciocínio:** O `fillna()` é a forma mais eficiente de imputar valores ausentes sem remover linhas inteiras do dataset.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
import pandas as pd

# 1. Carregamento
df_cust = pd.read_csv('customers.csv')
df_ord = pd.read_csv('orders.csv')

# 2. Merge (Left Join)
# Pedidos -> Clientes
df_merged = pd.merge(df_ord, df_cust, on='customer_id', how='left')

# 3. Agregação (Total Gasto por Cliente)
# Agrupamos por nome e somamos o valor do pedido
result = df_merged.groupby('customer_name')['order_value'].sum().reset_index()
result.columns = ['customer_name', 'total_spent']

# 4. Exportação para Parquet
result.to_parquet('customer_spending.parquet')

print("Arquivo gerado com sucesso!")
```
**Raciocínio:** O `merge()` simula o JOIN do SQL. O `reset_index()` é crucial após um `groupby`, pois transforma a coluna de agrupamento (que vira index) de volta em uma coluna comum do DataFrame.

## 🎫 Soluções dos Tickets

### P09-01: A Armadilha do `.apply()`
```python
import pandas as pd
import time

# Setup de teste
df = pd.DataFrame({'price': [10.0] * 5_000_000})

# Abordagem Lenta (.apply)
start = time.time()
df['price_new_slow'] = df['price'].apply(lambda x: x * 1.1)
end = time.time()
print(f"Tempo com .apply(): {end - start:.4f}s")

# Abordagem Rápida (Vetorizada)
start = time.time()
df['price_new_fast'] = df['price'] * 1.1
end = time.time()
print(f"Tempo Vetorizado: {end - start:.4f}s")
```
**Resultado esperado:** A versão vetorizada costuma ser entre 50x a 100x mais rápida que o `.apply()`.

### P09-02: O Mistério do Memory Leak
```python
import pandas as pd

chunk_size = 100_000 # processa 100k linhas por vez
reader = pd.read_csv('large_data.csv', chunksize=chunk_size)

for i, chunk in enumerate(reader):
    # Processa o chunk (ex: filtra apenas vendas > 1000)
    processed_chunk = chunk[chunk['sale_value'] > 1000]
    
    # Salva cada chunk em um arquivo separado ou usa append
    processed_chunk.to_csv(f'processed_part_{i}.csv', index=False)
```
**Raciocínio:** Ao usar `chunksize`, o Pandas não carrega o arquivo de 10GB na RAM; ele carrega apenas 100k linhas, processa, limpa a memória e carrega as próximas 100k.

### P09-03: A Migração para Colunar
```python
import pandas as pd
import glob

# 1. Ler todos os CSVs
arquivos = glob.glob("data/*.csv")
dfs = [pd.read_csv(f) for f in arquivos]

# 2. Consolidar
df_final = pd.concat(dfs, ignore_index=True)

# 3. Exportar para Parquet
df_final.to_parquet('consolidated_data.parquet', compression='snappy')
```
**Raciocínio:** O formato Parquet reduz o espaço em disco e acelera a leitura de colunas específicas, sendo o padrão ouro para Data Lakes.

---
← [[Python/09-Pandas-Parquet/03-Tickets]] · [[MOC-Python]] · [[Python/10-SQLAlchemy-Sessoes/01-Aula]] →
