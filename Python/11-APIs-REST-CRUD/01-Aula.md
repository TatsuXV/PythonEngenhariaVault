---
tipo: aula
trilha: python
capitulo: 11
titulo: "APIs, REST & CRUD: Integração de Dados"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [api, rest, fastapi, requests, crud]
---
# APIs, REST & CRUD: Integração de Dados

> [!abstract] Capítulo 11 · APIs, REST & CRUD: Integração de Dados
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/10-SQLAlchemy-Sessoes/01-Aula]] · 📦 Entrega: [[Python/11-APIs-REST-CRUD/07-Entrega-Projeto|API de Gestão Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença entre os métodos HTTP GET, POST, PUT e DELETE?
> ?
> [!question] O que é o formato JSON e por que ele é o padrão para a maioria das APIs modernas?
> ?
> [!question] O que significa o termo "Idempotência" em uma API REST?
> ?

## 🎯 Objetivo
> [!goal]
> Capacitar o aluno a construir e consumir interfaces de programação (APIs), permitindo que o pipeline de dados interaja com sistemas externos, consuma dados de serviços REST e exponha resultados de processamento via endpoints.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, as APIs são as "portas de entrada e saída". Muitas vezes, a fonte de dados não é um CSV ou Banco de Dados, mas uma API de terceiros (ex: API do Google Analytics, Stripe, Shopify). Da mesma forma, após processar dados em um Data Lake, você pode precisar expô-los via API para que um Dashboard ou App Front-end os consuma. Dominar o ciclo CRUD (Create, Read, Update, Delete) via HTTP é fundamental para a orquestração de dados.

## 📚 Teoria

### 1. O Protocolo HTTP e REST
REST (Representational State Transfer) é um estilo de arquitetura que utiliza o protocolo HTTP.

| Método | Ação CRUD | Descrição | Idempotente? |
| :--- | :--- | :--- | :---: |
| **GET** | Read | Recupera um recurso. | Sim |
| **POST** | Create | Cria um novo recurso. | Não |
| **PUT** | Update | Atualiza um recurso existente (substitui). | Sim |
| **PATCH** | Update | Atualiza parcialmente um recurso. | Não |
| **DELETE** | Delete | Remove um recurso. | Sim |

### 2. Consumindo APIs com `requests`
A biblioteca `requests` é o padrão para fazer chamadas HTTP em Python.

```python
import requests

# GET: Consumindo dados
response = requests.get("https://api.aurora.com/products/1")
if response.status_code == 200:
    product = response.json() # Converte resposta para dict Python

# POST: Enviando dados
payload = {"name": "Teclado", "price": 150.0}
response = requests.post("https://api.aurora.com/products", json=payload)
```

### 3. Construindo APIs com FastAPI
O FastAPI é a escolha moderna para DE devido à sua performance (assíncrono) e integração nativa com Type Hints e Pydantic.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ProductSchema(BaseModel):
    name: str
    price: float

@app.post("/products")
def create_product(product: ProductSchema):
    # Aqui integraria com SQLAlchemy para salvar no banco
    return {"message": f"Produto {product.name} criado!"}
```

### 4. Pydantic e a Validação de Dados
O Pydantic garante que os dados que entram na API estão no formato correto. Se o usuário enviar uma string onde deveria ser um `float`, o FastAPI retorna automaticamente um erro `422 Unprocessable Entity` com a explicação do erro.

## ⚠️ Armadilhas e Erros Comuns
- **Ignorar o Status Code:** Assumir que a requisição funcionou sem checar se o retorno foi `200 OK` ou `500 Internal Server Error`. Use `response.raise_for_status()`.
- **Expor Segredos na URL:** Passar chaves de API (`api_key`) como parâmetros na URL. Use Headers de Autenticação (`Authorization: Bearer <token>`).
- **Síncrono vs Assíncrono:** Usar `requests` (síncrono) dentro de rotas `async def` do FastAPI, o que bloqueia o loop de eventos do servidor. Use `httpx` para chamadas assíncronas.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `PUT` para qualquer atualização de dado."
> **Por que está errado:** O `PUT` substitui o objeto inteiro. Se você quiser alterar apenas o preço de um produto sem enviar o nome e a categoria novamente, deve usar `PATCH`.
> **Correto:** Use `PUT` para substituição total e `PATCH` para atualizações parciais.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Rate Limiting:** APIs profissionais limitam a quantidade de requisições por minuto. Em pipelines de dados, implemente a lógica de "Exponential Backoff" (esperar tempos crescentes entre tentativas) para evitar ser banido pelo servidor.

## 📖 Fonte
Fonte: [FastAPI Documentation](https://fastapi.tiangolo.com/) e [Requests Documentation](https://requests.readthedocs.io/)

---
← [[Python/10-SQLAlchemy-Sessoes/01-Aula]] · [[MOC-Python]] · [[Python/11-APIs-REST-CRUD/02-Lab]] →
