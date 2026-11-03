---
tipo: lab
trilha: python
capitulo: 04
titulo: "Lab: Manipulação de Coleções e Performance"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, lists, dicts, sets]
---
# Lab: Manipulação de Coleções e Performance

> [!abstract] Capítulo 04 · Lab: Manipulação de Coleções e Performance
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/04-Colecoes/01-Aula]] · 📦 Entrega: [[Python/04-Colecoes/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontece ao executar o código abaixo?
> ```python
> ids = [1, 2, 2, 3, 4, 4, 5]
> unique_ids = set(ids)
> print(len(unique_ids))
> ```
> > [!success] Resposta
> > `5`
> > **Explicação:** O `set` remove automaticamente todas as duplicatas da lista original.

```python
# Problema: Contar ocorrências de categorias de produtos da Loja Aurora
produtos = [
    {"id": 1, "cat": "Eletrônicos"},
    {"id": 2, "cat": "Casa"},
    {"id": 3, "cat": "Eletrônicos"},
    {"id": 4, "cat": "Livros"},
    {"id": 5, "cat": "Casa"},
]

# Abordagem 1: Ineficiente (Nested Loop)
contagem_lenta = {}
for p in produtos:
    cat = p["cat"]
    if cat not in contagem_lenta:
        contagem_lenta[cat] = 0
    contagem_lenta[cat] += 1

# Abordagem 2: Pythônica (defaultdict)
from collections import defaultdict
contagem_rapida = defaultdict(int)
for p in produtos:
    contagem_rapida[p["cat"]] += 1

print(dict(contagem_rapida)) # {'Eletrônicos': 2, 'Casa': 2, 'Livros': 1}
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a lógica para encontrar a intersecção entre duas listas de IDs de clientes (clientes que compraram no mês de Janeiro E Fevereiro).

```python
jan = [101, 102, 103, 104, 105]
fev = [103, 104, 106, 107, 108]

# TODO: Converter as listas para sets
set_jan = # TODO: complete aqui
set_fev = # TODO: complete aqui

# TODO: Realizar a intersecção (&)
comuns = # TODO: complete aqui

print(list(comuns)) # Esperado: [103, 104]
```

## 🚀 3. Do Zero
**Enunciado:** Crie um "Agregador de Pedidos". A função deve receber uma lista de itens de pedido `(product_id, quantity)` e retornar um dicionário onde a chave é o `product_id` e o valor é a soma total de quantidades.

**Critério de Aceite:** 
- `agregar([(1, 2), (2, 1), (1, 5)])` $\rightarrow$ `{1: 7, 2: 1}`.
- O código deve ser $O(n)$.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente usar uma lista como chave de um dicionário** $\rightarrow$ Erro esperado: `TypeError: unhashable type: 'list'`.
2. **Tente acessar uma chave inexistente em um dict comum** $\rightarrow$ Erro esperado: `KeyError`.
3. **Tente adicionar um item a uma tupla** $\rightarrow$ Erro esperado: `AttributeError: 'tuple' object has no attribute 'append'`.

---
← [[Python/04-Colecoes/01-Aula]] · [[MOC-Python]] · [[Python/04-Colecoes/03-Tickets]] →
