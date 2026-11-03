---
tipo: gabarito
trilha: python
capitulo: 08
titulo: "Gabarito: OOP e Encapsulamento"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, oop, dataclasses]
---
# Gabarito: OOP e Encapsulamento

## 💡 Solução do Lab (Item 2 - Complete)
```python
from dataclasses import dataclass

class Order:
    def __init__(self, order_id: int, total: float):
        self.order_id = order_id
        # Usamos o setter da propriedade para validar inclusive no construtor
        self.total = total 

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value < 0:
            raise ValueError("O valor total do pedido não pode ser negativo.")
        self._total = value

# Testes
try:
    o2 = Order(2, -10.0)
except ValueError as e:
    print(e) # O valor total do pedido não pode ser negativo.
```
**Raciocínio:** O uso de `@property` permite que a classe mantenha a interface de um atributo simples (`order.total`), mas execute uma lógica de validação internamente, simulando o comportamento de getters/setters do Java.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Product:
    product_id: int
    name: str
    price: float
    category: str

@dataclass(frozen=True)
class OrderItem:
    product: Product
    quantity: int

class Order:
    def __init__(self, order_id: int, items: List[OrderItem]):
        self.order_id = order_id
        self.items = items

    def calculate_total(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)

# Teste de Fluxo
p1 = Product(1, "Teclado", 150.0, "Eletronicos")
p2 = Product(2, "Mouse", 80.0, "Eletronicos")

item1 = OrderItem(p1, 1)
item2 = OrderItem(p2, 2)

pedido = Order(101, [item1, item2])
print(f"Total do Pedido: {pedido.calculate_total()}") # 310.0
```
**Raciocínio:** O uso de `frozen=True` nas dataclasses de `Product` e `OrderItem` garante que os dados do produto não sejam alterados acidentalmente durante o cálculo do pedido, promovendo a imutabilidade.

## 🎫 Soluções dos Tickets

### P08-01: O Fim dos Dicionários Soltos
```python
from dataclasses import dataclass

@dataclass
class Shipment:
    shipment_id: int
    weight: float
    dimension: str

def calculate_shipping(shipment: Shipment) -> float:
    # Agora temos autocompletar e garantia de tipo
    base_rate = 10.0
    if shipment.dimension == "large":
        base_rate += 5.0
    return base_rate * shipment.weight

# Uso
s = Shipment(1, 10.5, "large")
print(calculate_shipping(s))
```

### P08-02: O Factory de Produtos
```python
@dataclass
class Product:
    product_id: int
    name: str
    price: float
    category: str

    @classmethod
    def from_csv(cls, csv_line: str):
        parts = csv_line.split(',')
        if len(parts) != 4:
            raise ValueError("Linha CSV inválida. Esperados 4 campos.")
        return cls(int(parts[0]), parts[1], float(parts[2]), parts[3])

    @classmethod
    def from_json(cls, data: dict):
        return cls(data['id'], data['name'], data['price'], data['category'])

# Teste
p = Product.from_csv("1,Teclado,150.0,Eletronicos")
print(p)
```

### P08-03: Blindagem de Dados
**Análise:** Para proteger o `customer_id`, a melhor abordagem em Python para modelos de dados é a `@dataclass(frozen=True)`. Isso torna a classe imutável, impedindo que qualquer atributo seja alterado após a criação. Se a classe precisar de mutabilidade em outros campos, utiliza-se a `@property` apenas para o ID.

---
← [[Python/08-OOP-Encapsulamento/03-Tickets]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/01-Aula]] →
