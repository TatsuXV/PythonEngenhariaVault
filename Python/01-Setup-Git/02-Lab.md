---
tipo: lab
trilha: python
capitulo: 01
titulo: "Lab: Isolamento de Ambiente e Dependências"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, venv, pip]
---
# Lab: Isolamento de Ambiente e Dependências

> [!abstract] Capítulo 01 · Lab: Isolamento de Ambiente e Dependências
> ⏱ 2h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/01-Setup-Git/01-Aula]] · 📦 Entrega: [[Python/01-Setup-Git/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> Se eu criar um venv, instalar a biblioteca `requests` nele, desativar o venv e tentar rodar `import requests` no terminal global, o que acontecerá?
> > [!success] Resposta
> > Ocorrerá um `ModuleNotFoundError: No module named 'requests'`.
> > **Explicação:** O pacote foi instalado apenas no diretório local do venv, não no site-packages global do Python.

```powershell
# 1. Criar ambiente virtual
python -m venv .venv

# 2. Ativar ambiente
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependências pinadas
pip install requests==2.31.0 python-dotenv==1.0.1

# 4. Congelar dependências em arquivo
pip freeze > requirements.txt

# 5. Desativar
deactivate
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo tenta configurar um ambiente para leitura de arquivos `.env`. Complete as lacunas.

```python
# TODO: Importar a classe load_dotenv da biblioteca dotenv
from dotenv # TODO: complete aqui

import os

# TODO: Carregar as variáveis do arquivo .env
# TODO: complete aqui

# Acessar a variável
db_url = os.getenv("DATABASE_URL")
print(f"Conectando ao banco: {db_url}")
```

**Como verificar:** Crie um arquivo `.env` com `DATABASE_URL=postgres://localhost:5432` e execute o script.

## 🚀 3. Do Zero
**Enunciado:** Crie um script chamado `setup_env.py` que:
1. Verifique se o arquivo `.env` existe no diretório atual.
2. Se não existir, crie-o com a chave `ENVIRONMENT=development`.
3. Imprima a mensagem: "Ambiente configurado com sucesso!".

**Critério de Aceite:** O script deve ser idempotente (não sobrescrever o `.env` se ele já existir).

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente instalar um pacote sem ativar o venv** $\rightarrow$ Erro esperado: Pacote instalado globalmente (ou erro de permissão `sudo/Admin`).
2. **Tente importar `dotenv` sem ter instalado via pip** $\rightarrow$ Erro esperado: `ModuleNotFoundError`.
3. **Crie um arquivo `.env` com sintaxe errada (ex: `DB_URL : localhost`)** $\rightarrow$ Erro esperado: `os.getenv` retornará `None` ou a string literal incorreta.

---
← [[Python/01-Setup-Git/01-Aula]] · [[MOC-Python]] · [[Python/01-Setup-Git/03-Tickets]] →
