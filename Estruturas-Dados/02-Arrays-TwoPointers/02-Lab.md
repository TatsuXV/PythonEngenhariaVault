---
tipo: lab
trilha: estruturas-dados
capitulo: 02
titulo: "Lab: Arrays & Two Pointers na Prática"
nivel: 2
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-26
tags: [lab, arrays, two-pointers, leetcode]
---
# Lab: Arrays & Two Pointers na Prática

> [!abstract] Capítulo 02 · Lab: Arrays & Two Pointers
> ⏱ 3h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/02-Arrays-TwoPointers/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/02-Arrays-TwoPointers/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido (Padrão LeetCode)

> [!question] Problema: Valid Palindrome
> Dada uma string, determine se ela é um palíndromo, ignorando letras maiúsculas/minúsculas e caracteres não alfanuméricos.
> **Exemplo:** "A man, a plan, a canal: Panama" $\rightarrow$ True.
> > [!success] Solução com Two Pointers
> > 1. Um ponteiro `L` no início, `R` no fim.
> > 2. Enquanto `L < R`:
> >    - Se `L` não for alfanumérico $\rightarrow$ `L++`
> >    - Se `R` não for alfanumérico $\rightarrow$ `R--`
> >    - Se `arr[L] != arr[R]` $\rightarrow$ return `False`
> >    - `L++` e `R--`
> > 3. Return `True`.
> > **Complexidade:** $O(n)$ tempo, $O(1)$ espaço.

```python
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum(): l += 1
        elif not s[r].isalnum(): r -= 1
        elif s[l].lower() != s[r].lower(): return False
        else:
            l += 1
            r -= 1
    return True
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função para encontrar dois números em um array **ordenado** que somem um valor alvo (`target`).

```python
from typing import List

def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
    l, r = 0, len(numbers) - 1
    
    while l < r:
        current_sum = numbers[l] + numbers[r]
        
        if current_sum == target:
            # TODO: Retornar os índices (1-based conforme padrão LeetCode)
            # TODO: complete aqui
            return [l + 1, r + 1]
        
        elif current_sum < target:
            # TODO: A soma está baixa, precisamos de um número maior
            # TODO: complete aqui
            l += 1
        else:
            # TODO: A soma está alta, precisamos de um número menor
            # TODO: complete aqui
            r -= 1
            
    return []
```

## 🚀 3. Do Zero (Desafio DE)
**Enunciado:** Você está processando um log de transações financeiras ordenadas por timestamp. Você precisa encontrar a maior janela de tempo onde a diferença entre a maior e a menor transação do período seja menor ou igual a `K`.

**Tarefa:** Crie uma função que receba a lista de valores das transações (ordenada) e o valor `K`, retornando o tamanho da maior janela encontrada.

**Critério de Aceite:**
- Deve usar a técnica de **Sliding Window** (uma variação de Two Pointers).
- Complexidade temporal deve ser $O(n)$.
- Não pode usar loops aninhados que resultem em $O(n^2)$.

## 🧪 Quebre de Propósito
Tente as seguintes alterações e explique o erro:
1. **Use `numbers.sort()` dentro do loop de Two Pointers** $\rightarrow$ Erro: A complexidade saltaria de $O(n)$ para $O(n^2 \log n)$, matando a performance.
2. **Tente resolver o "Two Sum" em array desordenado usando Two Pointers sem ordenar primeiro** $\rightarrow$ Erro: O resultado será incorreto porque a lógica de mover `L` e `R` baseia-se na ordenação.
3. **Esqueça a condição `while l < r` e use `while True`** $\rightarrow$ Erro: `IndexError` assim que os ponteiros ultrapassarem os limites do array.

---
← [[Estruturas-Dados/02-Arrays-TwoPointers/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/02-Arrays-TwoPointers/03-Tickets]] →
