---
tipo: lab
trilha: python
capitulo: 12
titulo: "Lab: Estratégias de Escala e Memória"
nivel: 5
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [lab, big-data, multiprocessing, memory]
---
# Lab: Estratégias de Escala e Memória

> [!abstract] Capítulo 12 · Lab: Estratégias de Escala e Memória
> ⏱ 3h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Python/12-Projeto-Escala/01-Aula]] · 📦 Entrega: [[Python/12-Projeto-Escala/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontece se você tentar ler um arquivo de 100GB usando `pd.read_csv('big_file.csv')` em uma máquina com 16GB de RAM?
> > [!success] Resposta
> > O sistema disparará um `MemoryError` ou o sistema operacional matará o processo (`OOM Killer`).
> > **Explicação:** O Pandas tenta carregar todo o conteúdo do arquivo em memória RAM antes de transformá-lo em um DataFrame.

```python
import pandas as pd

# Estratégia correta: Chunking + Agregação Parcial
total_sales = 0
for chunk in pd.read_csv('huge_sales.csv', chunksize=100_000):
    total_sales += chunk['amount'].sum()

print(f"Soma total: {total_sales}")
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a otimização de tipos de dados para reduzir o consumo de memória de um DataFrame.

```python
import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')

# TODO: Reduzir float64 para float32
# TODO: complete aqui
df['price'] = df['price'].astype('float32')

# TODO: Reduzir int64 para int32
# TODO: complete aqui
df['quantity'] = df['quantity'].astype('int32')

# TODO: Converter coluna de 'category' (com poucos valores repetidos) para o tipo 'category'
# TODO: complete aqui
df['category'] = df['category'].astype('category')

print(f"Memória reduzida de {df.memory_usage().sum()} para {df.memory_usage().sum()} bytes")
```

## 🚀 3. Do Zero
**Enunciado:** Crie um processador de arquivos paralelo. 
Você tem uma pasta com 100 arquivos CSV grandes. Crie um script que:
1. Utilize `multiprocessing.Pool` para processar os arquivos em paralelo.
2. Cada processo deve:
    - Ler o arquivo em chunks.
    - Calcular a média de uma coluna específica.
    - Retornar apenas a média e a contagem de linhas do arquivo.
3. O processo principal deve consolidar as médias parciais para calcular a **Média Global Ponderada**.

**Critério de Aceite:**
- O script deve utilizar todos os núcleos da CPU disponíveis.
- A memória RAM não deve subir linearmente com o número de arquivos.
- O resultado final deve ser numericamente preciso.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente passar o DataFrame inteiro como argumento para a função do `Pool.map`** $\rightarrow$ Erro esperado: Lentidão extrema ou `MemoryError` devido ao overhead de serialização (Pickle).
2. **Tente usar `threading.Thread` para fazer cálculos matemáticos pesados** $\rightarrow$ Erro esperado: O tempo de execução será quase igual ao sequencial devido ao GIL.
3. **Tente criar 1.000 processos em um computador de 4 núcleos** $\rightarrow$ Erro esperado: Performance degradada por excesso de context switching.

---
← [[Python/12-Projeto-Escala/01-Aula]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/03-Tickets]] →
