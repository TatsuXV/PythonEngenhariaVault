---
tipo: gabarito
trilha: python
capitulo: 12
titulo: "Gabarito: Projeto de Escala"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [gabarito, big-data, multiprocessing]
---
# Gabarito: Projeto de Escala

## 💡 Solução do Lab (Item 2 - Complete)
```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# Otimização de tipos para reduzir footprint de memória
df['price'] = df['price'].astype('float32')
df['quantity'] = df['quantity'].astype('int32')
df['category'] = df['category'].astype('category')

print(f"Memória reduzida drasticamente!")
```
**Raciocínio:** O Pandas por padrão usa `float64` e `int64`. Ao reduzir para `32` ou `16` bits, cortamos o uso de memória pela metade ou mais, sem perda significativa de precisão para a maioria dos casos de negócio.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
import pandas as pd
from multiprocessing import Pool
import glob

def process_file(file_path):
    # Cada worker lê seu próprio arquivo para evitar overhead de Pickle
    chunk_sum = 0
    chunk_count = 0
    for chunk in pd.read_csv(file_path, chunksize=100_000):
        chunk_sum += chunk['valor'].sum()
        chunk_count += len(chunk)
    return chunk_sum, chunk_count

if __name__ == "__main__":
    files = glob.glob("data/*.csv")
    with Pool() as pool:
        # Passamos apenas o caminho (string), não o DataFrame
        results = pool.map(process_file, files)
    
    # Consolidação Final (Média Ponderada)
    total_sum = sum(r[0] for r in results)
    total_count = sum(r[1] for r in results)
    global_mean = total_sum / total_count
    print(f"Média Global: {global_mean}")
```
**Raciocínio:** O uso de `Pool.map` distribui a carga entre núcleos. A chave da performance aqui é o **isolamento de I/O**: cada processo cuida de sua leitura de disco.

## 🎫 Soluções dos Tickets

### P12-01: O Gargalo do Pickle
**Solução:** Alterar a assinatura da função de `def process(df):` para `def process(path):`.
Dentro da função, adicionar `df = pd.read_csv(path)`. 
**Resultado:** O tempo de serialização cai para quase zero, pois strings (caminhos) são leves para o Pickle, enquanto DataFrames são pesados.

### P12-02: A Morte por OOM
**Solução:** Em vez de `all_results.append(res)`, utilizar o `pyarrow.parquet.ParquetWriter`.
A cada chunk processado, chama-se `writer.write_table(table)`.
**Resultado:** A RAM permanece constante (ex: 500MB) independentemente de estarmos processando 1GB ou 1TB de dados.

### P12-03: O Desafio da Idempotência
**Solução:** 
1. Criar arquivo `state.txt`.
2. No loop de chunks: `if current_chunk_id <= int(open('state.txt').read()): continue`.
3. Após processar e salvar o chunk: `with open('state.txt', 'w') as f: f.write(str(current_chunk_id))`.
**Resultado:** O pipeline torna-se resiliente a falhas.

---
← [[Python/12-Projeto-Escala/03-Tickets]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/07-Entrega-Projeto]] →
