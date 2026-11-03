---
tipo: lab
trilha: python
capitulo: 06
titulo: "Lab: Ingestão de Dados e Portabilidade"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, pathlib, csv, json]
---
# Lab: Ingestão de Dados e Portabilidade

> [!abstract] Capítulo 06 · Lab: Ingestão de Dados e Portabilidade
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/06-Arquivos-Pathlib/01-Aula]] · 📦 Entrega: [[Python/06-Arquivos-Pathlib/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontece ao executar o código abaixo?
> ```python
> from pathlib import Path
> p = Path("data/raw/sales.csv")
> print(p.exists())
> ```
> > [!success] Resposta
> > `False` (ou `True` se o arquivo existir).
> > **Explicação:** O método `.exists()` do `pathlib` verifica a presença física do arquivo/pasta no disco de forma eficiente.

```python
import csv
import json
from pathlib import Path

# Definindo caminhos portáteis
BASE_DIR = Path(__file__).parent
INPUT_FILE = BASE_DIR / "data.csv"
OUTPUT_FILE = BASE_DIR / "output.json"

# 1. Escrita de CSV
with open(INPUT_FILE, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "nome", "valor"])
    writer.writerow([1, "Produto A", 100.0])
    writer.writerow([2, "Produto B", 200.0])

# 2. Leitura Streaming (Linha a Linha) e Conversão para JSON
results = []
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Transformação simples: converter valor para float
        row["valor"] = float(row["valor"])
        results.append(row)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=4)

print(f"Processado com sucesso para {OUTPUT_FILE}")
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente uma função que percorra uma pasta, identifique todos os arquivos `.csv` e retorne uma lista com seus caminhos completos.

```python
from pathlib import Path
from typing import List

def list_csv_files(folder_path: str) -> List[Path]:
    path = Path(folder_path)
    # TODO: Usar o método .glob() para encontrar arquivos .csv
    # TODO: complete aqui
    return list(csv_files)

# Teste
# print(list_csv_files("./dataset"))
```

## 🚀 3. Do Zero
**Enunciado:** Crie um "Conversor de JSON para CSV". O script deve:
1. Ler um arquivo `.json` contendo uma lista de dicionários.
2. Escrever um arquivo `.csv` onde as chaves do dicionário sejam o cabeçalho.
3. Usar `pathlib` para definir os caminhos e garantir que o arquivo de saída seja criado em uma pasta chamada `output/` (que deve ser criada se não existir).

**Critério de Aceite:** 
- O script não deve travar se o JSON estiver vazio.
- A pasta `output/` deve ser criada automaticamente via `path.mkdir(parents=True, exist_ok=True)`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Remova o `encoding="utf-8"` ao ler um arquivo com acentos no Windows** $\rightarrow$ Erro esperado: `UnicodeDecodeError`.
2. **Tente escrever em um arquivo em uma pasta que não existe (sem usar mkdir)** $\rightarrow$ Erro esperado: `FileNotFoundError`.
3. **Tente ler um arquivo CSV com `json.load()`** $\rightarrow$ Erro esperado: `json.decoder.JSONDecodeError`.

---
← [[Python/06-Arquivos-Pathlib/01-Aula]] · [[MOC-Python]] · [[Python/07-Logging-Decoradores/01-Aula]] →
