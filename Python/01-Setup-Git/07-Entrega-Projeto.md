---
tipo: projeto
trilha: python
capitulo: 01
titulo: "Entrega: Infraestrutura do Projeto"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, setup]
---
# Entrega: Infraestrutura do Projeto

> [!abstract] Parte do Projeto Python
> ⏱ 1h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/01-Setup-Git/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Estabelecer a fundação do repositório de portfólio, garantindo que qualquer recrutador consiga clonar e rodar o projeto com apenas dois comandos.

## 🛠 Implementação
Você deve configurar o repositório da seguinte forma:
1. Repositório Git inicializado.
2. Pasta `.venv` criada e ignorada no `.gitignore`.
3. Arquivo `.env.example` criado com as chaves necessárias (sem valores reais).
4. Arquivo `requirements.txt` com as bibliotecas base: `pandas`, `python-dotenv`, `pytest`.
5. README inicial com a seção "Como Rodar".

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Para este projeto, utilizei um ambiente virtual isolado com `venv` e pinagem de versões no `requirements.txt`. Esta decisão garante a reprodutibilidade do pipeline, evitando o erro comum de 'funciona na minha máquina', essencial para a manutenção de pipelines de dados em produção."

## ✅ Checklist de Aceite
- [ ] `.gitignore` contém `.venv`, `.env`, `__pycache__`.
- [ ] `.env.example` existe.
- [ ] `requirements.txt` possui versões fixas (ex: `==2.2.2`).
- [ ] `py -m pytest` roda sem erros (mesmo que não haja testes ainda).
