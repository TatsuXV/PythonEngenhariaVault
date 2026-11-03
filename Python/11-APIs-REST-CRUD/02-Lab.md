---
tipo: lab
trilha: python
capitulo: 11
titulo: "Lab: Integração de APIs e CRUD"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [lab, api, fastapi, requests]
---
# Lab: Integração de APIs e CRUD

> [!abstract] Capítulo 11 · Lab: Integração de APIs e CRUD
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/11-APIs-REST-CRUD/01-Aula]] · 📦 Entrega: [[Python/11-APIs-REST-CRUD/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> Qual a diferença entre `response.text` e `response.json()` ao consumir uma API?
> > [!success] Resposta
> > `response.text` retorna o corpo da resposta como uma **string bruta**.
> > `response.json()` tenta converter essa string em um **dicionário ou lista Python**.
> > **Explicação:** Como a maioria das APIs retorna JSON, o `.json()` é a forma mais prática de manipular os dados.

```python
import requests

# Simulando consumo de API de preços de Cripto
response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
data = response.json()
print(f"Preço do BTC: {data['bitcoin']['usd']}")
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função de "Sincronização de Produtos". A função deve ler a lista de produtos de uma API externa e atualizar o banco de dados local.

```python
import requests
from sqlalchemy.orm import Session
from models import Product

def sync_external_products(session: Session):
    # 1. Consumir API Externa
    url = "https://api.aurora-provider.com/products"
    response = requests.get(url)
    
    # TODO: Validar se a requisição foi bem sucedida (status 200)
    # TODO: complete aqui
    if response.status_code != 200:
        print("Erro ao acessar API")
        return
    
    # 2. Converter para JSON
    products_data = response.json()
    
    for item in products_data:
        # TODO: Buscar produto no banco pelo ID
        # TODO: complete aqui
        prod = session.get(Product, item['id'])
        
        if prod:
            # Atualizar preço se for diferente
            prod.price = item['price']
        else:
            # Criar novo produto
            new_prod = Product(name=item['name'], price=item['price'])
            # TODO: Adicionar à sessão
            # TODO: complete aqui
            session.add(new_prod)
            
    session.commit()
```

## 🚀 3. Do Zero
**Enunciado:** Crie uma mini API de Gestão de Estoque usando **FastAPI**.
1. Crie um endpoint `GET /inventory` que retorne a lista de todos os produtos no banco de dados.
2. Crie um endpoint `POST /inventory` que receba um JSON com `name` e `quantity` e adicione ao banco.
3. Crie um endpoint `PATCH /inventory/{prod_id}` que permita atualizar apenas a quantidade de um produto.

**Critério de Aceite:**
- Uso de schemas Pydantic para validação de entrada.
- Retorno de status codes corretos (`201 Created` para POST, `200 OK` para GET).
- Integração com SQLAlchemy para persistência real.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente enviar um texto em um campo que o Pydantic definiu como `float`** $\rightarrow$ Erro esperado: `422 Unprocessable Entity` (Erro de validação).
2. **Tente fazer um GET em uma rota que não existe** $\rightarrow$ Erro esperado: `404 Not Found`.
3. **Tente fazer um POST sem enviar o corpo JSON (payload)** $\rightarrow$ Erro esperado: `422 Unprocessable Entity`.

---
← [[Python/11-APIs-REST-CRUD/01-Aula]] · [[MOC-Python]] · [[Python/11-APIs-REST-CRUD/03-Tickets]] →
