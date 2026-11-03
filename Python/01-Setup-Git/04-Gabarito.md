---
tipo: gabarito
trilha: python
capitulo: 01
titulo: "Gabarito: Setup & Git"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, setup]
---
# Gabarito: Setup & Git

## 💡 Solução do Lab (Item 2 - Complete)
```python
from dotenv import load_dotenv # Correção: importar a função específica
import os

load_dotenv() # Correção: chamar a função para ler o .env

db_url = os.getenv("DATABASE_URL")
print(f"Conectando ao banco: {db_url}")
```
**Raciocínio:** A biblioteca `python-dotenv` exige que a função `load_dotenv()` seja invocada para que as variáveis do arquivo `.env` sejam injetadas no `os.environ`.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
import os
from pathlib import Path

def setup_env():
    env_file = Path(".env")
    if not env_file.exists():
        env_file.write_text("ENVIRONMENT=development", encoding="utf-8")
        print("Ambiente configurado com sucesso!")
    else:
        print("Arquivo .env já existe. Nenhuma alteração feita.")

if __name__ == "__main__":
    setup_env()
```
**Raciocínio:** O uso de `pathlib.Path` é a boa prática moderna em Python (substituindo `os.path`). O método `.exists()` garante a idempotência.

## 🎫 Soluções dos Tickets

### P01-01: O Arquivo Fantasma
Comandos:
1. `.\.venv\Scripts\Activate.ps1`
2. `pip freeze > requirements.txt`
3. `git add requirements.txt`
4. `git commit -m "chore: add requirements.txt for reproducibility"`

### P01-02: Segurança de Segredos
Comandos:
1. `echo .env >> .gitignore`
2. `git rm --cached .env`
3. `git add .gitignore`
4. `git commit -m "fix: remove .env from tracking and add to gitignore"`

### P01-03: Automação de Setup
```python
import subprocess
import sys
from pathlib import Path

def bootstrap():
    print("Criando ambiente virtual...")
    subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
    
    # Caminho para o pip do venv (Windows)
    pip_exe = Path(".venv/Scripts/pip.exe")
    
    print("Instalando dependências...")
    subprocess.run([str(pip_exe), "install", "-r", "requirements.txt"], check=True)
    print("Ambiente configurado com sucesso!")

if __name__ == "__main__":
    bootstrap()
```

---
← [[Python/01-Setup-Git/03-Tickets]] · [[MOC-Python]] · [[Python/02-Tipos-Conversao-Erros/01-Aula]] →
