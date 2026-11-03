---
tipo: gabarito
trilha: python
capitulo: 11
titulo: "Gabarito: APIs & REST"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [gabarito, api, fastapi, requests]
---
# Gabarito: APIs & REST

## 💡 Solução do Lab (Item 2 - Complete)
```python
import requests
from sqlalchemy.orm import Session
from models import Product

def sync_external_products(session: Session):
    url = "https://api.aurora-provider.com/products"
    response = requests.get(url)
    
    # Validar status 200
    if response.status_code != 200:
        print(f"Erro ao acessar API: {response.status_code}")
        return
    
    products_data = response.json()
    
    for item in products_data:
        # Buscar produto no banco pelo ID
        prod = session.get(Product, item['id'])
        
        if prod:
            # Atualizar preço
            prod.price = item['price']
        else:
            # Criar novo produto
            new_prod = Product(name=item['name'], price=item['price'])
            session.add(new_prod)
            
    session.commit()
```
**Raciocínio:** A sincronização de dados é um padrão comum em DE. A lógica de "buscar $\rightarrow$ atualizar ou criar" (conhecida como Upsert) garante que o banco de dados local seja um espelho fiel da fonte externa.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, Product # Suposições

app = FastAPI()

class ProductSchema(BaseModel):
    name: str
    quantity: int

@app.get("/inventory")
def get_inventory(db: Session = SessionLocal()):
    return db.query(Product).all()

@app.post("/inventory", status_code=status.HTTP_201_CREATED)
def add_to_inventory(prod: ProductSchema, db: Session = SessionLocal()):
    new_prod = Product(name=prod.name, quantity=prod.quantity)
    db.add(new_prod)
    db.commit()
    return {"message": "Produto adicionado!"}

@app.patch("/inventory/{prod_id}")
def update_quantity(prod_id: int, prod_data: ProductSchema, db: Session = SessionLocal()):
    prod = db.get(Product, prod_id)
    if not prod:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    prod.quantity = prod_data.quantity
    db.commit()
    return {"message": "Quantidade atualizada!"}
```
**Raciocínio:** O FastAPI automatiza a validação via Pydantic. O uso de `HTTPException` permite que a API comunique erros de forma padronizada para o cliente.

## 🎫 Soluções dos Tickets

### P11-01: O Colapso da API
```python
import asyncio
import httpx

async def fetch_order(client, order_id):
    url = f"https://api.aurora.com/orders/{order_id}"
    response = await client.get(url)
    return response.json()

async def main():
    order_ids = range(1, 1001)
    # Semaphore para limitar concorrência a 10 requisições simultâneas
    sem = asyncio.Semaphore(10)
    
    async with httpx.AsyncClient() as client:
        async def limited_fetch(oid):
            async with sem:
                return await fetch_order(client, oid)
        
        tasks = [limited_fetch(oid) for oid in order_ids]
        results = await asyncio.gather(*tasks)
        print(f"Processados {len(results)} pedidos.")

asyncio.run(main())
```
**Resultado esperado:** O tempo de execução cai drasticamente pois o Python não espera a resposta de cada requisição para iniciar a próxima.

### P11-02: A Chave Exposta
```python
import os
from dotenv import load_dotenv
import requests

load_dotenv() # Carrega variáveis do arquivo .env

API_KEY = os.getenv("AURORA_API_KEY")

if not API_KEY:
    raise EnvironmentError("Erro: AURORA_API_KEY não configurada no arquivo .env")

headers = {"Authorization": f"Bearer {API_KEY}"}
response = requests.get("https://api.aurora.com/data", headers=headers)
```
**Raciocínio:** Separar configuração (ambiente) de código (lógica) é a base da segurança em produção. O `.env` nunca deve ser versionado.

### P11-03: O Endpoint "Lento"
**Análise:** Fazer agregação massiva (`sum`, `count`) em tempo real em tabelas de milhões de linhas é inviável.
**Solução:** Implementar Cache.
- **Opção Simples:** `functools.lru_cache` para cache em memória no servidor.
- **Opção Profissional:** Redis. O resultado da query é salvo no Redis com um TTL de 15 minutos. A API checa o Redis primeiro; se não houver o dado, consulta o banco e salva no Redis.
**Resultado:** Respostas de 5 segundos passam a ser de milissegundos.

---
← [[Python/11-APIs-REST-CRUD/03-Tickets]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/01-Aula]] →
