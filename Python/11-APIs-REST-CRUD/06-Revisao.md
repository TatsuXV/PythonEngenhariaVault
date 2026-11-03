---
tipo: revisao
trilha: python
capitulo: 11
titulo: "Revisão: APIs & REST"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [revisao, api, fastapi, requests]
---
# Revisão: APIs & REST

> [!abstract] Capítulo 11 · Revisão de Integração de Dados
> ⏱ 1h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/11-APIs-REST-CRUD/01-Aula]] · 📦 Entrega: [[Python/11-APIs-REST-CRUD/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **Protocolo HTTP:** Sei a diferença entre GET, POST, PUT, PATCH e DELETE e quando usar cada um?
- [ ] **Consumo:** Consigo fazer requisições complexas usando `requests` e tratar erros de status code?
- [ ] **Construção:** Sei criar endpoints no FastAPI com validação Pydantic?
- [ ] **Performance:** Entendo a diferença entre requisições síncronas e assíncronas (`httpx` + `asyncio`)?
- [ ] **Segurança:** Sei a importância de usar variáveis de ambiente (`.env`) para chaves de API?

## 🧠 Mapa Mental de Conceitos

**APIs REST $\rightarrow$**
- **Comunicação $\rightarrow$** Client $\rightarrow$ HTTP Request $\rightarrow$ Server $\rightarrow$ HTTP Response.
- **Recursos $\rightarrow$** URIs (End-points) $\rightarrow$ Verbos HTTP (GET, POST, etc).
- **Dados $\rightarrow$** JSON $\rightarrow$ Tipagem (Pydantic).
- **Escala $\rightarrow$** Assincronismo $\rightarrow$ Cache $\rightarrow$ Rate Limiting.

**FastAPI $\rightarrow$**
- **Input $\rightarrow$** Path Parameters $\rightarrow$ Query Parameters $\rightarrow$ Request Body.
- **Output $\rightarrow$** Status Codes $\rightarrow$ JSON Response.

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você precisa criar um pipeline que consuma dados de 5 APIs diferentes, processe-os e salve no banco de dados. Se você usar `requests` sequencialmente, o pipeline levará 30 minutos.

**Qual a estratégia para reduzir esse tempo para 2 minutos?**
1. Implementar `asyncio` com `httpx`.
2. Disparar as chamadas para as 5 APIs simultaneamente.
3. Processar as respostas conforme elas chegam (utilizando `asyncio.as_completed` ou `gather`).
4. Salvar no banco em lotes (Bulk Insert) para evitar gargalos de I/O.

## 🔗 Links Rápidos
- Aula Teórica: [[Python/11-APIs-REST-CRUD/01-Aula]]
- Lab Prático: [[Python/11-APIs-REST-CRUD/02-Lab]]
- Tickets de Performance: [[Python/11-APIs-REST-CRUD/03-Tickets]]

---
← [[Python/11-APIs-REST-CRUD/05-Flashcards]] · [[MOC-Python]] · [[Python/11-APIs-REST-CRUD/07-Entrega-Projeto]] →
