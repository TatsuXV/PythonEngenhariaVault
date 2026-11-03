---
tipo: lab
trilha: python
capitulo: 08
titulo: "Lab: Modelagem de Domínio com Dataclasses"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, oop, dataclasses]
---
# Lab: Modelagem de Domínio com Dataclasses

> [!abstract] Capítulo 08 · Lab: Modelagem de Domínio com Dataclasses
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/08-OOP-Encapsulamento/01-Aula]] · 📦 Entrega: [[Python/08-OOP-Encapsulamento/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que acontece ao comparar dois objetos de uma classe comum vs dois objetos de uma `@dataclass` com os mesmos valores?
> > [!success] Resposta
> > Classes comuns comparam a **identidade** (endereço de memória), resultando em `False`.
> > Dataclasses comparam os **valores** dos atributos, resultando em `True`.
> > **Explicação:** A `@dataclass` gera automaticamente o método `__eq__` baseado nos campos definidos.

```python
from dataclasses import dataclass

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str

# Teste de Igualdade
c1 = Customer(1, "Alice", "alice@email.com")
c2 = Customer(1, "Alice", "alice@email.com")

print(f"São iguais? {c1 == c2}") # True
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a classe `Order` usando a lógica de encapsulamento para garantir que o valor total do pedido nunca seja negativo.

```python
from dataclasses import dataclass

class Order:
    def __init__(self, order_id: int, total: float):
        self.order_id = order_id
        # TODO: Usar a propriedade para validar o total no construtor
        # TODO: complete aqui
        self.total = total

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        # TODO: Lançar ValueError se value < 0
        # TODO: complete aqui
        self._total = value

# Testes
o1 = Order(1, 150.0)
print(o1.total) # 150.0
# o2 = Order(2, -10.0) # Deve levantar ValueError
```

## 🚀 3. Do Zero
**Enunciado:** Crie um modelo de domínio para a Loja Aurora composto por três classes:
1. `Product` (Dataclass): `id`, `name`, `price`, `category`.
2. `OrderItem` (Dataclass): `product` (objeto Product), `quantity`.
3. `Order` (Classe Comum): `order_id`, `items` (lista de OrderItem). 
   - a classe `Order` deve ter um método `calculate_total()` que soma (price * quantity) de todos os itens.

**Critério de Aceite:** 
- O `OrderItem` deve receber a instância de `Product` como argumento, não apenas o ID.
- O método `calculate_total()` deve retornar um float preciso.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente alterar um atributo de uma dataclass marcada com `frozen=True`** $\rightarrow$ Erro esperado: `FrozenInstanceError`.
2. **Tente instanciar uma classe sem passar um argumento obrigatório** $\rightarrow$ Erro esperado: `TypeError` (falta de argumento posicional).
3. **Tente acessar `self.total` dentro do setter de `total`** $\rightarrow$ Erro esperado: `RecursionError` (loop infinito de chamadas ao setter).

---
← [[Python/08-OOP-Encapsulamento/01-Aula]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/01-Aula]] →
