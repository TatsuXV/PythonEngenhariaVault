---
tipo: gabarito
trilha: estruturas-dados
capitulo: 02
titulo: "Gabarito: Arrays & Two Pointers"
---
# Gabarito: Arrays & Two Pointers

## 🎫 DSA-02-01: O Filtro de Duplicatas em Stream
**Problema:** Remover duplicatas adjacentes em array ordenado in-place.
**Solução:** Two Pointers (Leitura e Escrita).

```python
def remove_duplicates(nums):
    if not nums:
        return 0
    
    # Ponteiro de escrita (i)
    i = 0
    
    # Ponteiro de leitura (j)
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
            
    return i + 1 # Novo tamanho do array

# Teste
arr = [1, 1, 2, 2, 2, 3, 4, 4]
size = remove_duplicates(arr)
print(f"Novo tamanho: {size}, Array: {arr[:size]}") 
# Saída: Novo tamanho: 4, Array: [1, 2, 3, 4]
```
**Complexidade:** Tempo $O(n)$, Espaço $O(1)$.

---

## 🎫 DSA-02-02: O Buffer de Janela Deslizante
**Problema:** Calcular soma de janelas de tamanho K sem recalcular tudo.
**Solução:** Sliding Window (Soma Incremental).

```python
def calculate_window_sums(latencies, k):
    if len(latencies) < k:
        return []
    
    # 1. Calcular a primeira janela
    current_window_sum = sum(latencies[:k])
    result = [current_window_sum]
    
    # 2. Deslizar a janela
    for i in range(k, len(latencies)):
        # Soma = Soma anterior - elemento que sai + elemento que entra
        current_window_sum = current_window_sum - latencies[i-k] + latencies[i]
        result.append(current_window_sum)
        
    return result

# Teste
lat = [10, 20, 30, 40, 50]
k = 3
print(calculate_window_sums(lat, k)) 
# Saída: [60, 90, 120]
```
**Complexidade:** Tempo $O(n)$, Espaço $O(n)$ para o resultado.

---

## 🎫 DSA-02-03: O Pareamento de Logs (REVIEW)
**Análise do Erro:**
O código original falha porque a técnica de **Two Pointers Opostos** (um no início, outro no fim) assume que o array está **ordenado**. 
Se `arr = [3, 1, 4, 2]` e `target = 5`:
- `l=0 (3), r=3 (2)` $\rightarrow$ $3+2 = 5$. (Nesse caso específico funcionou, mas se `target = 3`, ele nunca acharia `1+2` porque `l` e `r` se moveriam erraticamente).

**Correção Sugerida:**
```python
def find_pair_fixed(arr, target):
    # PASSO CRUCIAL: Ordenar o array primeiro
    arr.sort() # O(n log n)
    
    l, r = 0, len(arr) - 1
    while l < r:
        current_sum = arr[l] + arr[r]
        if current_sum == target: return True
        elif current_sum < target: l += 1
        else: r -= 1
    return False
```
**Complexidade Final:** Tempo $O(n \log n)$ devido ao sort. Para manter $O(n)$, deve-se usar um **Hash Map** (Capítulo 03).
