---
tipo: ticket
trilha: python
capitulo: 11
titulo: "Tickets de APIs & REST"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [ticket, api, fastapi, requests, security]
---
# Tickets: APIs & REST

> [!abstract] Capítulo 11 · Tickets de APIs & REST
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/11-APIs-REST-CRUD/02-Lab]] · 📦 Entrega: [[Python/11-APIs-REST-CRUD/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P11-01: O Colapso da API (OTIMIZAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O script de ingestão de dados faz 1.000 requisições `GET` sequenciais para buscar detalhes de cada pedido. Isso leva 10 minutos para rodar e o servidor da API começou a bloquear as requisições.
> **Entrada:** Loop `for` chamando `requests.get()`.
> **Saída Esperada:** Implementação de chamadas assíncronas com `httpx`.

**✅ Critério de Aceite:**
- [ ] Substituir `requests` por `httpx.AsyncClient()`.
- [ ] Utilizar `asyncio.gather()` para disparar múltiplas requisições simultaneamente.
- [ ] Reduzir o tempo de execução de minutos para segundos.

**💡 Dicas:**
> [!tip] Nível 1
> Requisições HTTP são operações de I/O (entrada/saída). Enquanto o Python espera a resposta do servidor, a CPU fica ociosa. O `asyncio` permite que o Python inicie a segunda requisição sem esperar a primeira terminar.
> 
> [!tip] Nível 2
> Cuidado para não disparar 1.000 requisições de uma vez e sofrer um banimento por DoS. Use um `Semaphore` para limitar a concorrência (ex: 10 requisições por vez).

**🧪 Como Verificar:**
O script deve completar a ingestão de 1.000 registros em uma fração do tempo original.

---

## 🎫 TICKET P11-02: A Chave Exposta (SEGURANÇA)
**Prioridade:** Média | **Tipo:** Security | **Tempo:** 60min
> **Contexto:** Foi descoberto que a API Key do provedor de dados está escrita diretamente no código (`api_key = "abc123xyz"`). Isso é um risco crítico de segurança.
> **Entrada:** Código com strings hardcoded.
> **Saída Esperada:** Implementação de variáveis de ambiente via `python-dotenv`.

**✅ Critério de Aceite:**
- [ ] Criação de arquivo `.env` (ignorado pelo git).
- [ ] Uso de `os.getenv("API_KEY")` para recuperar a chave.
- [ ] O código deve lançar um erro claro se a chave não for encontrada no ambiente.

**💡 Dicas:**
> [!tip] Nível 1
> Instale a biblioteca `python-dotenv` e chame `load_dotenv()` no início do script.
> 
> [!tip] Nível 2
> Adicione o `.env` ao seu `.gitignore` para garantir que a chave nunca suba para o repositório.

**🧪 Como Verificar:**
O script deve funcionar normalmente com a chave no `.env`, mas falhar se o arquivo for removido.

---

## 🎫 TICKET P11-03: O Endpoint "Lento" (DEBUG)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** O endpoint `GET /orders/summary` demora 5 segundos para responder. Ao analisar, percebeu-se que ele faz a soma de milhões de linhas no banco de dados a cada requisição.
> **Entrada:** Endpoint que executa `sum()` no banco a cada chamada.
> **Saída Esperada:** Sugestão de implementação de Cache.

**✅ Critério de Aceite:**
- [ ] Identificar que o cálculo repetitivo é o gargalo.
- [ ] Sugerir a implementação de um cache simples (ex: `functools.lru_cache` ou Redis).
- [ ] Definir um tempo de expiração (TTL) para o cache.

**💡 Dicas:**
> [!tip] Nível 1
> Cache é a técnica de salvar o resultado de uma operação cara para que a próxima chamada seja instantânea.
> 
> [!tip] Nível 2
> Em pipelines de dados, caches de 5 ou 15 minutos costumam ser suficientes para dashboards.

**🧪 Como Verificar:**
Relatório de review descrevendo o impacto do cache no tempo de resposta.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/11-APIs-REST-CRUD/01-Aula]] ou [[Python/11-APIs-REST-CRUD/02-Lab]].
