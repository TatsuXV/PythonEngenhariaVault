---
tipo: aula
trilha: python
capitulo: 06
titulo: "Arquivos: CSV, JSON e Pathlib"
nivel: 3
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [arquivos, csv, json, pathlib]
---
# Arquivos: CSV, JSON e Pathlib

> [!abstract] Capítulo 06 · Arquivos: CSV, JSON e Pathlib
> ⏱ 6h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/01-Aula]] · 📦 Entrega: [[Python/06-Arquivos-Pathlib/07-Entrega-Projeto|Ingestor de Dados Brutos]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença fundamental entre ler um arquivo com `file.read()` vs `for line in file:`?
> ?
> [!question] Por que o uso de `with open(...)` é obrigatório em pipelines de dados profissionais?
> ?
> [!question] Qual a vantagem de usar a biblioteca `pathlib` em vez de `os.path` para manipular caminhos de arquivos?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a manipulação de arquivos de texto e estruturados (CSV, JSON), implementando a leitura e escrita eficiente de dados com a biblioteca `pathlib`, garantindo a portabilidade do código entre Windows e Linux.

## ⚙️ No Pipeline
> [!pipeline]
> O primeiro passo de qualquer pipeline de dados é a **Ingestão**. Frequentemente, os dados chegam como "dumps" de CSV ou JSON. Se você carregar um arquivo de 10GB usando `.read()`, você causará um erro de `MemoryError` e derrubará o servidor. O segredo da engenharia de dados é o **processamento linha a linha (streaming)**, mantendo o consumo de memória constante independentemente do tamanho do arquivo.

## 📚 Teoria

### 1. Pathlib: A Forma Moderna de Caminhos
A `pathlib` trata caminhos como objetos, não como strings. Isso resolve o problema eterno de barras invertidas (`\`) no Windows vs barras normais (`/`) no Linux.

**Comparação:**
```python
# Antigo (os.path)
import os
path = os.path.join("data", "raw", "file.csv")

# Moderno (pathlib)
from pathlib import Path
path = Path("data") / "raw" / "file.csv" # Operador / sobrecarregado
```

### 2. Gerenciamento de Contexto (`with open`)
O comando `with` garante que o arquivo seja fechado automaticamente, mesmo se ocorrer uma exceção. Isso evita o "leak" de descritores de arquivo no sistema operacional.

### 3. Manipulando CSVs (Módulo `csv`)
Para arquivos simples, o módulo `csv` é mais rápido e leve que o pandas.
- `csv.reader`: Lê como listas.
- `csv.DictReader`: Lê como dicionários (muito melhor para manutenção).

### 4. Manipulando JSONs (Módulo `json`)
JSONs são a base de APIs.
- `json.load()`: Lê de um arquivo.
- `json.loads()`: Lê de uma string.
- `json.dump()`: Escreve em um arquivo.

## ⚠️ Armadilhas e Erros Comuns
- **Encoding:** Ignorar o `encoding="utf-8"` ao abrir arquivos. Isso causa o erro `UnicodeDecodeError` quando o arquivo contém caracteres especiais (acentos).
- **Carregar Tudo na Memória:** Usar `.readlines()` em arquivos grandes. Sempre itere sobre o arquivo: `for line in file:`.
- **Caminhos Hardcoded:** Usar `C:\Users\Nome\data...`. Use caminhos relativos baseados no `Path(__file__).parent`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `open('arquivo.txt').read()` para ler pequenos arquivos rapidamente."
> **Por que está errado:** Abrir um arquivo sem o contexto `with` deixa o descritor aberto até o Python decidir fazer o garbage collection, o que pode bloquear o arquivo no Windows.
> **Correto:** Sempre use `with open('arquivo.txt', encoding='utf-8') as f:`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **JSON Lines (`.jsonl`):** Em Big Data, usamos JSONL (um JSON por linha). Isso permite ler o arquivo linha a linha sem precisar carregar o JSON inteiro (que exigiria que o arquivo fosse um array gigante `[...]`).

## 📖 Fonte
Fonte: [Python Docs - pathlib](https://docs.python.org/3/library/pathlib.html) e [Python Docs - csv](https://docs.python.org/3/library/csv.html) (Versão 3.12)

---
← [[Python/05-Funcoes-TypeHints/01-Aula]] · [[MOC-Python]] · [[Python/07-Logging-Decoradores/01-Aula]] →
