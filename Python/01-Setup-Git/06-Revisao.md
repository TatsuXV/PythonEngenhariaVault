---
tipo: revisao
trilha: python
capitulo: 01
titulo: "Revisão: Setup & Git"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, setup]
---
# Revisão: Setup & Git

## ⚪ Folha em Branco
**Desafio:** Desenhe o fluxo de inicialização de um projeto Python profissional, desde a criação da pasta até o primeiro commit, incluindo a gestão de segredos.
> [!success] Comparação
> Pasta $\rightarrow$ `git init` $\rightarrow$ `python -m venv .venv` $\rightarrow$ `.gitignore` (incluindo `.venv` e `.env`) $\rightarrow$ `pip install ...` $\rightarrow$ `pip freeze > requirements.txt` $\rightarrow$ `.env` $\rightarrow$ Git commit.

## 🗣 Explique ao Júnior
Explique por que não usamos `pip install` sem versão (ex: `pip install pandas`) em projetos de produção.
> [!tip] Resposta Sugerida
> "Se você não pinar a versão, o projeto pode quebrar amanhã se a biblioteca atualizar e mudar a sintaxe de alguma função. Pinando a versão, garantimos que o código que roda na minha máquina seja exatamente o mesmo que rodará no servidor de produção."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/01-Setup-Git/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/01-Setup-Git/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/01-Setup-Git/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. (Próximo capítulo) - O que é um tipo dinâmico?
2. (MOC) - Qual a sequência de capítulos de Python?
3. (Setup) - Como remover um arquivo do Git sem deletar do disco?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (configuro ambiente sem olhar guia).
- [ ] 3: Consegui ensinar a configurar o ambiente para outro dev.

## 📓 Registro de Erros
Sintoma: `Activate.ps1 cannot be loaded because running scripts is disabled on this system`.
Causa: Política de execução do PowerShell.
Regra: Executar `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` no terminal Admin.
Tag: #erro/setup
