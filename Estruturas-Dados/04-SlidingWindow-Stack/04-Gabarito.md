---
tipo: gabarito
trilha: estruturas-dados
capitulo: 04
titulo: "Gabarito: Sliding Window & Stack"
---
# Gabarito: Sliding Window & Stack

## 🎫 DSA-04-01: O Monitor de Picos de CPU
**Problema:** Calcular média móvel de CPU em tempo real com $O(1)$.
**Solução:** Sliding Window com `deque`.

```python
from collections import deque

class CPUMonitor:
    def __init__(self, window_size=60):
        self.window_size = window_size
        self.data = deque(maxlen=window_size)
        self.running_sum = 0.0

    def add_value(self, val):
        # Se a janela já está cheia, subtraímos o valor que vai sair
        if len(self.data) == self.window_size:
            self.running_sum -= self.data[0]
        
        # Adicionamos o novo valor
        self.data.append(val)
        self.running_sum += val
        
        return self.running_sum / len(self.data)

# Teste
monitor = CPUMonitor(window_size=3)
print(monitor.add_value(10)) # 10.0
print(monitor.add_value(20)) # 15.0
print(monitor.add_value(30)) # 20.0
print(monitor.add_value(40)) # (20+30+40)/3 = 30.0
```
**Complexidade:** Tempo $O(1)$ por atualização, Espaço $O(K)$ onde $K$ é o tamanho da janela.

---

## 🎫 DSA-04-02: O Validador de JSON Aninhado
**Problema:** Verificar se chaves e colchetes estão balanceados.
**Solução:** Stack (LIFO).

```python
def is_balanced(text):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in text:
        if char in mapping.values():
            # Abre { [ ( -> Empilha
            stack.append(char)
        elif char in mapping.keys():
            # Fecha } ] ) -> Desempilha e verifica
            if not stack or stack.pop() != mapping[char]:
                return False
                
    return len(stack) == 0

# Teste
print(is_balanced('{"a": [1, 2, {"b": 3}]}')) # True
print(is_balanced('{"a": [1, 2}'))             # False
```
**Complexidade:** Tempo $O(n)$, Espaço $O(n)$.

---

## 🎫 DSA-04-03: a Maior Substring Única (REVIEW)
**Análise do Erro:**
O código original usa dois loops aninhados, resultando em $O(n^2)$. Para cada início `i`, ele tenta expandir `j` até encontrar um repetido.

**Solução Otimizada (Sliding Window Dinâmica):**
```python
def longest_unique_optimized(s):
    char_map = {} # guarda a última posição do caractere
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        char = s[right]
        # Se o caractere já existe na janela, movemos o 'left'
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
            
        char_map[char] = right
        max_len = max(max_len, right - left + 1)
        
    return max_len

# Teste
print(longest_unique_optimized("abcabcbb")) # 3 ("abc")
```
**Complexidade:** Tempo $O(n)$, Espaço $O(k)$ onde $k$ é o tamanho do alfabeto.
