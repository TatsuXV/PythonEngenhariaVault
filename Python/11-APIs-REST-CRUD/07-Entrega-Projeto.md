---
tipo: entrega
trilha: python
capitulo: 11
titulo: "Entrega: API de Gestão Aurora"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [entrega, projeto, fastapi, sqlalchemy, api]
---
# Entrega: API de Gestão Aurora

> [!abstract] Capítulo 11 · Projeto de Integração e API
> ⏱ 6h · 🎯 Nível 4/5 · 📦 Objetivo: Construir uma API profissional para gerir o ecossistema da Loja Aurora. · ✅ Verificado

## 🎯 Objetivo do Projeto
Você deve desenvolver uma API utilizando **FastAPI** que funcione como a interface de gerenciamento para a Loja Aurora. A API deve permitir a manipulação de produtos e clientes, integrando-se com o banco de dados via SQLAlchemy e consumindo dados de um provedor externo.

## 🛠 Requisitos Técnicos

### 1. Endpoints de CRUD (Internos)
Implementar as seguintes rotas:
- `GET /products`: Retorna a lista de todos os produtos.
- `POST /products`: Cria um novo produto (com validação Pydantic).
- `PATCH /products/{id}`: Atualiza apenas o preço ou a quantidade de um produto.
- `DELETE /products/{id}`: Remove um produto do sistema.
- `GET /customers/{id}/orders`: Retorna todos os pedidos de um cliente específico.

### 2. Sincronização Externa (Ingestão)
Criar um endpoint administrativo `POST /sync/external-products` que:
- Chame uma API externa simulada (ou um arquivo JSON externo).
- Utilize `httpx` de forma assíncrona para baixar os dados.
- Atualize os produtos no banco de dados local (Upsert).

### 3. Segurança e Validação
- Implementar um Header de Autenticação simples (`X-API-KEY`) para as rotas de POST, PATCH e DELETE.
- Garantir que todos os inputs sejam validados via Pydantic (ex: preços não podem ser negativos).
- Retornar status codes adequados: `201 Created`, `404 Not Found`, `401 Unauthorized`.

## ✅ Critérios de Aceite
- [ ] A API deve rodar sem erros via `uvicorn`.
- [ ] A documentação automática do Swagger (`/docs`) deve estar clara e tipada.
- [ ] O processo de sincronização externa deve ser assíncrono.
- [ ] Tentativas de atualizar produtos inexistentes devem retornar `404`.

## 🧪 Cenário de Teste
1. Criar um produto via `POST /products`.
2. Verificar se ele aparece no `GET /products`.
3. Atualizar o preço via `PATCH /products/{id}`.
4. Chamar `/sync/external-products` e verificar se novos produtos foram adicionados ao banco.

## 🏁 Entrega
Submeta o código completo da API (`main.py`, `schemas.py`, `models.py`, `database.py`) e o arquivo `.env` de exemplo.

---
← [[Python/11-APIs-REST-CRUD/06-Revisao]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/01-Aula]] →
