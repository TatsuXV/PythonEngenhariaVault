---
tipo: lab
trilha: estruturas-dados
capitulo: 04
titulo: "Lab: Sliding Window & Stack na Prática"
nivel: 3
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-28
tags: [lab, sliding-window, stack, leetcode]
---
# Lab: Sliding Window & Stack na Prática

> [!abstract] Capítulo 04 · Lab: Sliding Window & Stack
> ⏱ 3h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/04-SlidingWindow-Stack/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/04-SlidingWindow-Stack/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido (Padrão LeetCode)

> [!question] Problema: Valid Parentheses
> Dada uma string contendo apenas os caracteres '(', ')', '{', '}', '[' e ']', determine se a string é válida.
> **Exemplo:** `"{[]}"` $\rightarrow$ True | `"(]"` $\rightarrow$ False.
> > [!success] Solução com Stack
> > 1. Crie uma pilha `stack = []`.
> > 2. Para cada caractere `char` na string:
> >    - Se for abertura `( [ {`, dê `.append(char)`.
> >    - Se for fechamento `) ] }`:
> >      - Se a pilha estiver vazia $\rightarrow$ return `False`.
> >      - Desempilhe o topo `top = stack.pop()`.
> >      - Se `top` não for o par correspondente de `char` $\rightarrow$ return `False`.
> > 3. Ao final, se a pilha estiver vazia $\rightarrow$ return `True`.
> > **Complexidade:** $O(n)$ tempo, $O(n)$ espaço.

```python
def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    return not stack
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função para encontrar a **Soma Máxima de uma Janela Fixa** de tamanho `K`.

```python
from typing import List

def max_sum_subarray(nums: List[int], k: int) -> int:
    if len(nums) < k: return 0
    
    # 1. Calcular a soma da primeira janela
    current_window_sum = sum(nums[:k])
    max_sum = current_window_sum
    
    # 2. Deslizar a janela
    for i in range(len(nums) - k):
        # TODO: Subtrair o elemento que sai (i) e somar o que entra (i + k)
        # TODO: complete aqui
        current_window_sum = current_window_sum - nums[i] + nums[i + k]
        
        # TODO: Atualizar a soma máxima encontrada
        # TODO: complete aqui
        max_sum = max(max_sum, current_window_sum)
        
    return max_sum
```

## 🚀 3. Do Zero (Desafio DE)
**Enunciado:** Você está processando um stream de logs de erro. Você precisa encontrar o **menor intervalo de tempo (janela)** que contenha pelo menos 3 erros de nível "CRÍTICO".

**Tarefa:** Crie uma função que receba a lista de timestamps dos erros críticos e retorne a duração (diff) da menor janela.

**Critério de Aceite:**
- Deve usar a técnica de **Sliding Window de tamanho dinâmico**.
- Complexidade temporal $O(n)$.
- Se não houver 3 erros, retorne `None`.

## 🧪 Quebre de Propósito
Tente as seguintes alterações e explique o erro:
1. **Use `sum(nums[i:i+k])` dentro do loop em vez de atualizar a soma** $\rightarrow$ Erro: A complexidade vira $O(n \cdot k)$, tornando o processamento lento em janelas grandes.
2. **Tente dar `.pop()` em uma stack vazia sem checar `if stack`** $\rightarrow$ Erro: `IndexError: pop from empty list`.
3. **Tente usar uma fila (Queue) para validar parênteses aninhados** $\rightarrow$ Erro: Lógica incorreta. Filas processam FIFO, mas parênteses exigem LIFO (o último aberto deve ser o primeiro fechado).

---
← [[Estruturas-Dados/04-SlidingWindow-Stack/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/04-SlidingWindow-Stack/03-Tickets]] →
