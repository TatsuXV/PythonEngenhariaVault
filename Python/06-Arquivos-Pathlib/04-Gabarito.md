---
tipo: gabarito
trilha: python
capitulo: 06
titulo: "Gabarito: Arquivos e Pathlib"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, pathlib, csv, json]
---
# Gabarito: Arquivos e Pathlib

## 💡 Solução do Lab (Item 2 - Complete)
```python
from pathlib import Path
from typing import List

def list_csv_files(folder_path: str) -> List[Path]:
    path = Path(folder_path)
    # Usando .glob() para buscar todos os arquivos com extensão .csv
    csv_files = path.glob("*.csv")
    return list(csv_files)

# Teste
# print(list_csv_files("./dataset"))
```
**Raciocínio:** O método `.glob()` da `pathlib` é a forma mais eficiente de realizar buscas por padrão de nome em diretórios, retornando um gerador (lazy evaluation) que economiza memória.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_output_path: str):
    # 1. Definindo caminhos
    p_in = Path(json_path)
    p_out = Path(csv_output_path)
    
    # 2. Garantir que a pasta de saída existe
    p_out.parent.mkdir(parents=True, exist_ok=True)
    
    # 3. Leitura do JSON
    with open(p_in, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if not data:
        print("JSON vazio.")
        return

    # 4. Escrita do CSV
    # Assumindo que data é uma lista de dicionários
    keys = data[0].keys()
    with open(p_out, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

# Teste
# json_to_csv("data.json", "output/data.csv")
```
**Raciocínio:** O uso de `DictWriter` automatiza a criação do cabeçalho e o mapeamento dos valores, tornando o código robusto a mudanças na ordem das chaves do JSON.

## 🎫 Soluções dos Tickets

### P06-01: A Ingestão Lenta
```python
# Ineficiente
# lines = f.readlines() # Carrega 2GB na RAM -> CRASH

# Eficiente (Streaming)
with open("logs.txt", "r", encoding="utf-8") as f:
    for line in f: # Lê uma linha por vez (estável)
        process(line)
```

### P06-02: O Caminho Quebrado
```python
from pathlib import Path

# Incorreto (Hardcoded string)
# path = "data/raw/file.csv" 

# Correto (Portável)
BASE_DIR = Path(__file__).parent
FILE_PATH = BASE_DIR / "data" / "raw" / "file.csv"
```

### P06-03: O JSON Corrompido
```python
import json

def load_config(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Erro de sintaxe no JSON na linha {e.lineno}, coluna {e.colno}: {e.msg}")
        return None
```

---
← [[Python/06-Arquivos-Pathlib/03-Tickets]] · [[MOC-Python]] · [[Python/07-Logging-Decoradores/01-Aula]] →
