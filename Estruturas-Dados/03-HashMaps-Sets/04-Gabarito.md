---
tipo: gabarito
trilha: estruturas-dados
capitulo: 03
titulo: "Gabarito: Hash Maps & Sets"
---
# Gabarito: Hash Maps & Sets

## 🎫 DSA-03-01: O Gargalo do Join Manual
**Problema:** Encontrar a interseção de duas listas de IDs de forma performática.
**Solução:** Uso de `set` para busca $O(1)$.

```python
def find_intersection(lista_a, lista_b):
    # Converter para set: O(n + m)
    set_a = set(lista_a)
    set_b = set(lista_b)
    
    # Operação de interseção: O(min(n, m))
    return list(set_a & set_b)

# Teste
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]
print(find_intersection(a, b)) 
# Saída: [4, 5]
```
**Complexidade:** Tempo $O(n + m)$, Espaço $O(n + m)$.

---

## 🎫 DSA-03-02: O Detector de Anomalias
**Problema:** Encontrar IDs de pedidos sem correspondência de cliente.
**Solução:** Diferença de Sets.

```python
def find_orphan_orders(orders, customer_map):
    # Diferença de sets: retira do set de pedidos todos os que estão no set de chaves do mapa
    orphans = set(orders) - set(customer_map.keys())
    return list(orphans)

# Teste
orders = [101, 102, 103, 104]
customer_map = {101: 'A', 102: 'B', 103: 'C'}
print(find_orphan_orders(orders, customer_map)) 
# Saída: [104]
```
**Complexidade:** Tempo $O(n)$, Espaço $O(n)$.

---

## 🎫 DSA-03-03: O Problema do Primeiro Único (REVIEW)
**Análise do Erro:**
O código original usa `s.count(char)` dentro de um loop. O `count()` percorre a string inteira $O(n)$. Como está dentro de um loop de $n$ iterações, a complexidade é $O(n^2)$.

**Solução Otimizada (Frequency Counter):**
```python
from collections import Counter

def first_unique_optimized(s):
    # 1ª Passada: Contagem de frequência O(n)
    counts = Counter(s)
    
    # 2ª Passada: Encontrar o primeiro com frequência 1 O(n)
    for char in s:
        if counts[char] == 1:
            return char
    return None

# Teste
print(first_unique_optimized("deodataengineering")) 
# Saída: 'o'
```
**Complexidade Final:** Tempo $O(n)$, Espaço $O(k)$ onde $k$ é o tamanho do alfabeto.
