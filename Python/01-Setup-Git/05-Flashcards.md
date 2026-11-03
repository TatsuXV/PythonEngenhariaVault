---
tipo: flashcard
trilha: python
capitulo: 01
titulo: "Flashcards: Setup & Git"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, setup]
---
# Flashcards: Setup & Git

## 🧠 Conceitos
O que é um `venv`?::Um ambiente virtual que isola as dependências de um projeto, evitando conflitos de versões globais.
Para que serve o arquivo `requirements.txt`?::Para listar e pinar as versões exatas das bibliotecas necessárias para a reproduzibilidade do projeto.
Qual a função da biblioteca `python-dotenv`?::Carregar variáveis de configuração de um arquivo `.env` para o ambiente do sistema (`os.environ`).

## ⌨️ Código & Sintaxe
Comando para criar um venv no Windows?::`python -m venv .venv`
Comando para ativar venv no Linux/macOS?::`source .venv/bin/activate`
Comando para gerar o `requirements.txt` com os pacotes instalados?::`pip freeze > requirements.txt`

## ⚠️ Erros e Correções
Erro: `ModuleNotFoundError: No module named 'requests'` mesmo tendo instalado o pacote?::Causa: O venv não está ativado ou o pacote foi instalado globalmente e o script roda no venv. Correção: Ativar venv e instalar novamente.
Arquivo `.env` aparece no `git status` após ter sido adicionado ao `.gitignore`?::Causa: O arquivo já estava sendo rastreado (cached). Correção: `git rm --cached .env`.

## 🧩 Cloze (Preencher)
Para evitar que senhas sejam expostas, utilizamos o arquivo ==.gitignore== para excluir arquivos sensíveis do repositório?
resposta: .gitignore
