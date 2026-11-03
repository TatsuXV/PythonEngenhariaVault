---
tipo: aula
trilha: python
capitulo: 01
titulo: "Setup, Ambiente e Git para Dados"
nivel: 1
tempo_estimado_h: 4
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-09
tags: [setup, git, venv]
---
# Setup, Ambiente e Git para Dados

> [!abstract] Capítulo 01 · Setup, Ambiente e Git para Dados
> ⏱ 4h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: Nenhum · 📦 Entrega: [[Python/01-Setup-Git/07-Entrega-Projeto|Repo Inicial Configurado]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença fundamental entre `venv` e `conda` no contexto de engenharia de dados?
> ?
> [!question] Por que não devemos subir o arquivo `.env` para o GitHub?
> ?
> [!question] O que acontece se você instalar bibliotecas globalmente em vez de usar um ambiente virtual?
> ?

## 🎯 Objetivo
> [!goal]
> Configurar um ambiente de desenvolvimento Python profissional, isolado e versionado, preparando o terreno para pipelines de dados reproduzíveis.

## ⚙️ No Pipeline
> [!pipeline]
> Em produção, pipelines de dados rodam em containers (Docker) ou ambientes virtuais rigorosamente pinados. Se o ambiente de Dev difere do de Prod (ex: pandas 1.x vs 2.x), o pipeline pode quebrar silenciosamente devido a mudanças em tipos de dados ou comportamentos de indexação.

## 📚 Teoria

### 1. O Ambiente Virtual (`venv`)
Diferente do Java, onde o classpath é gerenciado pelo Maven/Gradle, o Python instala pacotes em pastas. O `venv` cria uma cópia isolada do interpretador Python.

**Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS (Bash):**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Gestão de Dependências (`requirements.txt`)
Para garantir a reproduzibilidade, pinamos as versões. 
**Regra de Ouro:** Nunca use `pip install pandas`. Use `pip install pandas==2.2.2`.

### 3. Variáveis de Ambiente (`.env`)
Usamos a biblioteca `python-dotenv` para separar configurações (DB_URL, API_KEY) do código.

### 4. Git para Dados
A engenharia de dados lida com código e *dados*. 
- **Código:** Versiona-se no Git.
- **Dados:** NUNCA versiona-se arquivos CSV/JSON grandes no Git. Usa-se `.gitignore` para ignorar a pasta `Dataset/` e arquivos `.env`.

## ⚠️ Armadilhas e Erros Comuns
- **Ativar o venv:** Tentar rodar o código sem ativar o venv e receber `ModuleNotFoundError`.
- **Global Install:** Instalar pacotes globalmente, causando conflitos entre projetos diferentes.
- **Git Leak:** Subir o `.env` com senhas do banco de dados para o repositório público.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Para projetos maiores, considere o **Poetry**. Ele resolve a árvore de dependências de forma mais rigorosa que o `requirements.txt`, similar ao `pom.xml` do Maven.

## 📖 Fonte
Fonte: [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/installing-packages/) (Versão 3.12)

---
← [[MOC-Python]] · [[MOC-Python]] · [[Python/02-Tipos-Conversao-Erros/01-Aula]] →
