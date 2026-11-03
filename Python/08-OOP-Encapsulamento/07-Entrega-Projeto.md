---
tipo: entrega
trilha: python
capitulo: 08
titulo: "Entrega: Modelo de Domínio da Loja Aurora"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [entrega, projeto, oop, dataclasses]
---
# Entrega: Modelo de Domínio da Loja Aurora

> [!abstract] Capítulo 08 · Projeto de Modelagem de Domínio
> ⏱ 4h · 🎯 Nível 4/5 · 📦 Objetivo: Implementar a camada de domínios do ecossistema Aurora. · ✅ Verificado

## 🎯 Objetivo do Projeto
Substituir a manipulação de dados "solta" (via dicionários e tuplas) por uma arquitetura de **Objetos de Domínio**. Você deve criar a estrutura de classes que representará a Loja Aurora, garantindo que os dados sejam validados e imutáveis onde for necessário.

## 🛠 Requisitos Técnicos

### 1. Camada de Produtos (`Product`)
- Implementar como `@dataclass(frozen=True)`.
- Atributos: `product_id` (int), `name` (str), `price` (float), `category` (str).
- Implementar um `@classmethod` chamado `from_csv(csv_line: str)` que parseie uma linha de CSV e retorne a instância.

### 2. Camada de Itens do Pedido (`OrderItem`)
- Implementar como `@dataclass(frozen=True)`.
- Atributos: `product` (Instância de `Product`), `quantity` (int).
- Validar no construtor (via `__post_init__`) que a quantidade seja maior que zero.

### 3. Camada de Pedidos (`Order`)
- Implementar como Classe Comum (pois o estado do pedido pode mudar).
- Atributos: `order_id` (int), `items` (List[OrderItem]), `customer_id` (int).
- **Métodos Obrigatórios:**
    - `calculate_total()`: Retorna a soma de `product.price * quantity` de todos os itens.
    - `add_item(item: OrderItem)`: Adiciona um item à lista de pedidos.
- **Encapsulamento:** O atributo `items` deve ser protegido (`_items`), acessível apenas via getter `@property`.

## ✅ Critérios de Aceite
- [ ] O código deve ser validado pelo `mypy` sem erros de tipagem.
- [ ] Tentativas de alterar o preço de um `Product` devem lançar `FrozenInstanceError`.
- [ ] O método `calculate_total` deve retornar um valor `float` preciso.
- [ ] O sistema deve impedir a criação de `OrderItem` com quantidade $\le 0$.

## 🧪 Cenário de Teste Sugerido
```python
# 1. Criar produtos via CSV
p1 = Product.from_csv("1,Teclado Mecânico,250.0,Periféricos")
p2 = Product.from_csv("2,Mouse Gamer,120.0,Periféricos")

# 2. Montar pedido
pedido = Order(101, 50) # ID 101, Cliente 50
pedido.add_item(OrderItem(p1, 1))
pedido.add_item(OrderItem(p2, 2))

# 3. Validar Total
print(f"Total: {pedido.calculate_total()}") # Esperado: 490.0
```

## 🏁 Entrega
Submeta o arquivo `.py` contendo a implementação completa e um pequeno script de teste validando os critérios de aceite.

---
← [[Python/08-OOP-Encapsulamento/06-Revisao]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/01-Aula]] →
