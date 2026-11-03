---
tipo: ticket
trilha: python
capitulo: 01
titulo: "Tickets de Configuração de Ambiente"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, git, venv]
---
# Tickets: Configuração de Ambiente

> [!abstract] Capítulo 01 · Tickets de Configuração de Ambiente
> ⏱ 2h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/01-Setup-Git/02-Lab]] · 📦 Entrega: [[Python/01-Setup-Git/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P01-01: O Arquivo Fantasma (PREDIZER)
**Prioridade:** Alta | **Tipo:** Bug | **Tempo:** 15min
> **Contexto:** O desenvolvedor subiu o projeto para o GitHub, mas o colega não consegue rodar porque faltam as bibliotecas. O arquivo `requirements.txt` não está no repositório.
> **Entrada:** Pasta do projeto com `.venv/` e `main.py`.
> **Saída Esperada:** O comando `pip freeze > requirements.txt` deve ser executado e o arquivo commitado.

**✅ Critério de Aceite:** 
- [ ] Arquivo `requirements.txt` criado com versões exatas (ex: `pandas==2.2.2`).

**💡 Dicas:**
> [!tip] Nível 1
> Lembre-se de ativar o ambiente virtual antes de dar o freeze.
> 
> [!tip] Nível 2
> O comando é `pip freeze`.

**🧪 Como Verificar:** 
`cat requirements.txt` (Linux) ou `Get-Content requirements.txt` (Windows).

---

## 🎫 TICKET P01-02: Segurança de Segredos (CONSERTAR)
**Prioridade:** Crítica | **Tipo:** Incidente | **Tempo:** 30min
> **Contexto:** Foi detectado que o arquivo `.env` contendo a senha do banco de produção foi commitado no Git. 
> **Entrada:** Repositório com `.env` visível no histórico.
> **Saída Esperada:** O arquivo `.env` deve ser removido do índice do Git (sem deletar do disco local) e adicionado ao `.gitignore`.

**✅ Critério de Aceite:** 
- [ ] `.env` presente no `.gitignore`.
- [ ] `git rm --cached .env` executado.

**💡 Dicas:**
> [!tip] Nível 1
> Use o comando `git rm --cached` para remover do rastreamento mas manter o arquivo físico.
> 
> [!tip] Nível 2
> O `.gitignore` deve conter a linha `.env`.

**🧪 Como Verificar:** 
`git status` $\rightarrow$ O arquivo `.env` não deve aparecer como "tracked".

---

## 🎫 TICKET P01-03: Automação de Setup (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** a empresa quer um script `bootstrap.py` que automatize a criação do venv e a instalação de dependências para novos devs.
> **Entrada:** Arquivo `requirements.txt` presente.
> **Saída Esperada:** Script que usa `subprocess` para rodar comandos de sistema.

**✅ Critério de Aceite:** 
- [ ] O script deve criar a pasta `.venv`.
- [ ] O script deve instalar os pacotes do `requirements.txt`.

**💡 Dicas:**
> [!tip] Nível 1
> Use `subprocess.run(["python", "-m", "venv", ".venv"])`.
> 
> [!tip] Nível 2
> Lembre-se que para instalar pacotes no venv via script, você deve apontar para o executável do pip dentro de `.venv/Scripts/pip.exe`.

**🧪 Como Verificar:** 
`py bootstrap.py` $\rightarrow$ Verificar se a pasta `.venv` foi criada e populada.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/01-Setup-Git/01-Aula]] ou [[Python/01-Setup-Git/02-Lab]].
