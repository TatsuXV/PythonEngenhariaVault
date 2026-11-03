---
tipo: aula
trilha: python
capitulo: 08
titulo: "OOP e Encapsulamento: Modelagem de Domínio"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [oop, dataclasses, encapsulamento]
---
# OOP e Encapsulamento: Modelagem de Domínio

> [!abstract] Capítulo 08 · OOP e Encapsulamento: Modelagem de Domínio
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/01-Aula]] · 📦 Entrega: [[Python/08-OOP-Encapsulamento/07-Entrega-Projeto|Modelo de Domínio da Loja Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença fundamental entre uma Classe comum e uma `@dataclass` em Python?
> ?
> [!question] Por que usar `@property` (getters/setters) em vez de acessar atributos diretamente, mesmo que o Python não tenha modificadores `private` reais como o Java?
> ?
> [!question] O que é a herança múltipla e por que ela deve ser usada com cautela em pipelines de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Migrar a manipulação de dados de dicionários genéricos para Objetos de Domínio, utilizando classes e dataclasses para garantir integridade, tipagem e organização estrutural do pipeline.

## ⚙️ No Pipeline
> [!pipeline]
> Em pipelines profissionais, passar dicionários (`dict`) entre funções é perigoso porque você não sabe quais chaves existem sem olhar o código. Ao usar **Objetos de Domínio** (ex: uma classe `Order`), você tem autocompletar no IDE, validação de tipos no construtor e a garantia de que cada "Pedido" no seu sistema possui as mesmas propriedades. Isso reduz drasticamente a incidência de `KeyError` em produção.

## 📚 Teoria

### 1. OOP: Java vs Python
Para quem vem do Java, a principal diferença é que o Python é **dinâmico**. Não precisamos de interfaces explícitas para tudo; usamos *Duck Typing* ("se anda como pato e grasna como pato, então é um pato").

| Conceito | Java | Python |
| :--- | :--- | :--- |
| Modificadores | `private`, `protected`, `public` | Convenção `_` (protegido), `__` (privado) |
| Construtor | `public ClassName()` | `def __init__(self):` |
| Interfaces | `interface` | `abc.ABC` (Abstract Base Classes) |
| Modelos de Dados | POJOs / Records | `@dataclass` |

### 2. Data Classes (`@dataclass`)
Introduzidas no Python 3.7, as dataclasses automatizam a criação de métodos repetitivos como `__init__`, `__repr__` e `__eq__`.

**Exemplo Profissional:**
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True) # frozen=True torna o objeto imutável (estilo Record do Java)
class Product:
    product_id: int
    name: str
    price: float
    category: str
```

### 3. Encapsulamento e `@property`
Como o Python não tem `private` real, usamos a convenção do underscore `_` para indicar que um atributo é interno. Para controlar o acesso, usamos o decorador `@property`.

```python
class Order:
    def __init__(self, total: float):
        self._total = total # Atributo protegido

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        if value < 0:
            raise ValueError("Total não pode ser negativo")
        self._//total = value
```

### 4. Herança e Polimorfismo
Podemos criar classes base para comportamentos comuns em pipelines (ex: uma classe `BaseIngestor` que define o método `extract()`).

## ⚠️ Armadilhas e Erros Comuns
- **Abuso de Herança:** Criar hierarquias profundas (`ClasseA` $\rightarrow$ `B` $\rightarrow$ `C` $\rightarrow$ `D`). Em DE, prefira a **Composição** (uma classe que contém outra).
- **Esquecer o `self`:** Diferente do `this` implícito do Java, no Python o `self` deve ser explicitamente o primeiro argumento de todos os métodos da classe.
- **Usar Classes para tudo:** Não transforme cada dado em uma classe. Se for apenas um par chave-valor simples, um `dict` ou `NamedTuple` é mais eficiente.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use classes comuns para representar linhas de tabelas de banco de dados."
> **Por que está errado:** Classes comuns têm overhead de memória alto para milhões de instâncias.
> **Correto:** Use `@dataclass` com `__slots__` ou `NamedTuple` para representar registros de dados em massa, reduzindo drasticamente o consumo de RAM.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Métodos de Classe vs Estáticos:** 
> - `@classmethod`: Recebe a própria classe (`cls`) como primeiro argumento. Útil para *Factory Methods* (ex: `Product.from_csv(line)`).
> - `@staticmethod`: Não recebe nem `self` nem `cls`. É apenas uma função organizada dentro de uma classe.

## 📖 Fonte
Fonte: [Python Docs - Classes](https://docs.python.org/3/tutorial/classes.html) e [Python Docs - Dataclasses](https://docs.python.org/3/library/dataclasses.html) (Versão 3.12)

---
← [[Python/07-Logging-Decoradores/01-Aula]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/01-Aula]] →
