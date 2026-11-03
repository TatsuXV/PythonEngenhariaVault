---
tipo: ticket
trilha: estruturas-dados
capitulo: 03
titulo: "Tickets de Hash Maps & Sets"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-27
tags: [ticket, hash-maps, sets, leetcode, optimization]
---
# Tickets: Hash Maps & Sets

> [!abstract] Capítulo 03 · Tickets de Hash Maps & Sets
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/03-HashMaps-Sets/02-Lab]] · 📦 Entrega: [[Estruturas-Dados/03-HashMaps-Sets/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET DSA-03-01: O Gargalo do Join Manual (REFATORAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** Um script de limpeza de dados está comparando duas listas de IDs (`lista_a` e `lista_b`) para encontrar a interseção. O código atual usa: `for x in lista_a: if x in lista_b: result.append(x)`. Com 100k IDs em cada lista, o script trava.
> **Entrada:** Duas listas de IDs.
> **Saída Esperada:** Refatoração para usar a operação de interseção de `set`.

**✅ Critério de Aceite:**
- [ ] Converter as listas para `set`.
- [ ] Utilizar o operador `&` (interseção) ou o método `.intersection()`.
- [ ] Reduzir a complexidade de $O(n \cdot m)$ para $O(n + m)$.

**💡 Dicas:**
> [!tip] Nível 1
> A busca `in` em uma lista é $O(n)$, mas em um set é $O(1)$.
> 
> [!tip] Nível 2
> O custo de converter a lista para set é $O(n)$, mas isso é feito apenas uma vez.

**🧪 Como Verificar:**
O tempo de execução deve cair de minutos para milissegundos.

---

## 🎫 TICKET DSA-03-02: O Detector de Anomalias (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Você precisa identificar "IDs órfãos" em um sistema de pedidos. Você tem uma lista de `OrderIDs` e uma lista de `CustomerID`. Você deve encontrar todos os `OrderIDs` que não possuem um `CustomerID` correspondente no mapeamento de clientes.
> **Entrada:** `orders = [101, 102, 103, 104]` e `customer_map = {101: 'A', 102: 'B', 103: 'C'}`.
> **Saída Esperada:** `[104]`.

**✅ Critério de Aceite:**
- [ ] Implementação usando a técnica de "complemento de set" ou verificação de chaves em dicionário.
- [ ] Complexidade temporal $O(n)$.
- [ ] O resultado deve ser retornado como uma lista de IDs.

**💡 Dicas:**
> [!tip] Nível 1
> Use a diferença de sets: `set(orders) - set(customer_map.keys())`.
> 
> [!tip] Nível 2
> Lembre-se que a operação de diferença de sets é extremamente eficiente em Python.

**🧪 Como Verificar:**
Executar com 1 milhão de pedidos e 900k clientes; o resultado deve ser instantâneo.

---

## 🎫 TICKET DSA-03-03: O Problema do Primeiro Único (REVIEW)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou uma função para encontrar o primeiro caractere que não se repete em uma string de logs.
> **Código:**
> ```python
> def first_unique(s):
>     for char in s:
>         if s.count(char) == 1:
>             return char
>     return None
> ```
> **Pergunta:** Por que este código é ineficiente para strings gigantes (ex: 1M de caracteres)?

**✅ Critério de Aceite:**
- [ ] Identificar que `s.count(char)` percorre a string inteira a cada iteração do loop $\rightarrow$ $O(n^2)$.
- [ ] Sugerir o uso de um `Frequency Counter` (Hash Map) para contar tudo em uma única passada.
- [ ] Propor a solução: 1ª passada para contar $\rightarrow$ 2ª passada para encontrar o primeiro com count == 1. Complexidade final: $O(n)$.

**💡 Dicas:**
> [!tip] Nível 1
> Sempre que vir um método de contagem dentro de um loop, acenda o alerta de performance.
> 
> [!tip] Nível 2
> O uso do `collections.Counter` simplifica a implementação da primeira passada.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Estruturas-Dados/03-HashMaps-Sets/01-Aula]] ou [[Estruturas-Dados/03-HashMaps-Sets/02-Lab]].
