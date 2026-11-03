---
tipo: projeto-final
trilha: python
capitulo: final
titulo: "Projeto Final de Portfólio: O Ecossistema de Dados Aurora"
nivel: 5
tempo_estimado_h: 20
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [projeto-final, portfolio, data-engineering, python, full-stack-data]
---
# Projeto Final de Portfólio: O Ecossistema de Dados Aurora

> [!abstract] Projeto de Conclusão da Trilha Python
> ⏱ 20h · 🎯 Nível 5/5 · 📦 Objetivo: Construir um sistema completo de ingestão, processamento e exposição de dados. · ✅ Verificado

## 🎯 Objetivo do Projeto
Este projeto é a peça central do seu portfólio. Você não construirá apenas um script, mas um **Ecossistema de Dados**. O objetivo é criar um pipeline end-to-end que extrai dados de APIs e arquivos, processa-os com alta performance e os expõe através de uma API profissional, tudo isso utilizando as melhores práticas de Engenharia de Software.

---

## 🛠 Escopo Técnico (O que deve ser construído)

### 1. Camada de Ingestão (Extract)
Construir um módulo de ingestão híbrido:
- **Async Collector:** Um coletor assíncrono (`httpx` + `asyncio`) que consome dados de uma API externa de produtos e clientes.
- **Bulk Loader:** Um carregador de arquivos que processe CSVs massivos via `chunksize`, tratando a tipagem para reduzir o footprint de memória.

### 2. Camada de Processamento (Transform)
Desenvolver o núcleo de transformação utilizando Pandas e NumPy:
- **Pipeline de Limpeza:** Implementar a remoção de duplicatas, tratamento de nulos e normalização de strings.
- **Agregador de Métricas:** Criar KPIs de vendas (Total por categoria, Ticket médio, Crescimento mensal) usando operações vetorizadas.
- **Otimização de Storage:** Exportar os dados transformados para arquivos **Parquet** particionados.

### 3. Camada de Persistência (Load)
Implementar a infraestrutura de banco de dados com SQLAlchemy 2.0:
- **Modelagem de Domínio:** Implementar a estrutura de tabelas (Customer, Product, Order, OrderItem) com relacionamentos `One-to-Many`.
- **Upsert Engine:** Criar a lógica de "Sincronização" que atualiza registros existentes ou insere novos sem duplicados.
- **Transaction Manager:** Garantir que a carga dos dados seja atômica (Commit/Rollback).

### 4. Camada de Exposição (API)
Construir a interface de saída com FastAPI:
- **Endpoints de Consulta:** Rotas para recuperar métricas agregadas e detalhes de pedidos.
- **Validação Rigorosa:** Uso de schemas Pydantic para todas as entradas e saídas.
- **Autenticação:** Implementar um sistema de API Key para proteger os endpoints de escrita.

---

## ✅ Critérios de Aceite (Padrão de Portfólio)

- [ ] **Performance:** O pipeline deve processar arquivos de 1GB+ sem estourar 2GB de RAM.
- [ ] **Tipagem:** O código deve ser 100% tipado e passar na validação do `mypy`.
- [ ] **Arquitetura:** O projeto deve ser dividido em módulos (`ingestion.py`, `processing.py`, `database.py`, `api.py`).
- [ ] **Resiliência:** O sistema deve possuir logs detalhados (`logging`) e tratamento de exceções profissional.
- [ ] **Documentação:** Um arquivo `README.md` explicando como rodar o projeto, a arquitetura utilizada e as decisões de performance.

## 🧪 Fluxo de Dados Esperado
`API Externa / CSV` $\rightarrow$ `Async Collector / Chunk Loader` $\rightarrow$ `Pandas Transform` $\rightarrow$ `SQLAlchemy DB` $\rightarrow$ `FastAPI Endpoints`.

## 🏁 Entrega Final
O projeto deve ser entregue como um repositório Git contendo:
1. O código fonte organizado.
2. Arquivo `requirements.txt` com todas as dependências.
3. Arquivo `.env.example` para configurações de banco e API.
4. O README detalhado para o recrutador.

---
← [[Python/Simulado-Python]] · [[MOC-Python]] · [[Tópico-Seguinte]] →
