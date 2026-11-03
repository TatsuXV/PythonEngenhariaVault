---
tipo: ticket
trilha: python
capitulo: 08
titulo: "Tickets de OOP e Encapsulamento"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, oop, dataclasses, refactoring]
---
# Tickets: OOP e Encapsulamento

> [!abstract] Capítulo 08 · Tickets de OOP e Encapsulamento
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/08-OOP-Encapsulamento/02-Lab]] · 📦 Entrega: [[Python/08-OOP-Encapsulamento/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P08-01: O Fim dos Dicionários Soltos (REFATORAR)
**Prioridade:** Alta | **Tipo:** Refatoração | **Tempo:** 60min
> **Contexto:** O módulo de cálculo de frete recebe um dicionário `{'id': 1, 'weight': 10.5, 'dim': 'large'}`. O código está cheio de verificações `if 'weight' in data:`.
> **Entrada:** Função que processa dicionários.
> **Saída Esperada:** Refatoração para usar uma `@dataclass` chamada `Shipment`.

**✅ Critério de Aceite:** 
- [ ] Criação da dataclass `Shipment` com tipagem rigorosa.
- [ ] A função de frete agora recebe um objeto `Shipment` em vez de um `dict`.
- [ ] O código deve eliminar todas as verificações de existência de chaves (`if 'key' in dict`).

**💡 Dicas:**
> [!tip] Nível 1
> Use o construtor da dataclass para validar os dados na entrada.
> 
> [!tip] Nível 2
> Lembre-se que ao usar a dataclass, você acessa os dados via `shipment.weight` (atributo) e não `shipment['weight']` (chave).

**🧪 Como Verificar:** 
O código deve passar nos testes unitários e o `mypy` deve validar a tipagem do argumento da função.

---

## 🎫 TICKET P08-02: O Factory de Produtos (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Os produtos da Loja Aurora vêm de fontes diferentes (CSV e JSON). Precisamos de um método centralizado para criar objetos `Product` a partir de diferentes formatos.
> **Entrada:** Uma string CSV `"1,Teclado,150.0,Eletrônicos"` ou um dict JSON.
> **Saída Esperada:** Implementação de um `@classmethod` chamado `from_csv` e `from_json` na classe `Product`.

**✅ Critério de Aceite:** 
- [ ] Uso correto de `@classmethod`.
- [ ] Validação de que a string CSV possui a quantidade correta de campos antes de instanciar o objeto.
- [ ] Retorno de uma instância válida de `Product`.

**💡 Dicas:**
> [!tip] Nível 1
> Um `@classmethod` recebe `cls` como primeiro argumento, permitindo que ele chame `cls(...)` para criar a instância.
> 
> [!tip] Nível 2
> Use `.split(',')` para processar a string CSV.

**🧪 Como Verificar:** 
`Product.from_csv("1,Teclado,150.0,Eletronicos")` deve retornar um objeto `Product`.

---

## 🎫 TICKET P08-03: Blindagem de Dados (REVISAR)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou a classe `Customer` mas deixou todos os atributos públicos. Qualquer parte do código pode alterar o `customer_id` do cliente, o que causaria caos no banco de dados.
> **Código:**
> ```python
> class Customer:
>     def __init__(self, customer_id, name):
>         self.customer_id = customer_id
>         self.name = name
> ```

**✅ Critério de Aceite:** 
- [ ] Identificar que `customer_id` não deve ser mutável.
- [ ] Sugerir o uso de `@property` (apenas getter) para o `customer_id`.
- [ ] Sugerir a mudança para `@dataclass(frozen=True)` se o objeto for puramente para transporte de dados.

**💡 Dicas:**
> [!tip] Nível 1
> Lembre-se da convenção de underscore `_customer_id`.
> 
> [!tip] Nível 2
> Explique por que a imutabilidade é preferível em pipelines de dados.

**🧪 Como Verificar:** 
Relatório de review descrevendo o risco de mutabilidade e a solução proposta.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/08-OOP-Encapsulamento/01-Aula]] ou [[Python/08-OOP-Encapsulamento/02-Lab]].
