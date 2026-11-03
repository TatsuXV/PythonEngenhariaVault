---
tipo: lab
trilha: estruturas-dados
capitulo: 03
titulo: "Lab: Hash Maps & Sets na Prática"
nivel: 3
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-27
tags: [lab, hash-maps, sets, leetcode]
---
# Lab: Hash Maps & Sets na Prática

> [!abstract] Capítulo 03 · Lab: Hash Maps & Sets
> ⏱ 3h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/03-HashMaps-Sets/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/03-HashMaps-Sets/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido (Padrão LeetCode)

> [!question] Problema: Two Sum (O Clássico)
> Dado um array de números `nums` e um valor `target`, retorne os índices dos dois números que somam o target.
> **Exemplo:** `nums = [2, 7, 11, 15], target = 9` $\rightarrow$ `[0, 1]`.
> > [!success] Solução com Hash Map (O(n))
> > Em vez de dois loops, usamos um dicionário para guardar o "complemento" necessário.
> > 1. Crie um dicionário vazio `prev_map`.
> > 2. Percorra o array: para cada `num`, calcule `diff = target - num`.
> > 3. Se `diff` já estiver no `prev_map`, encontramos o par! Retorne `[prev_map[diff], index]`.
> > 4. Caso contrário, salve `prev_map[num] = index`.
> > **Complexidade:** $O(n)$ tempo, $O(n)$ espaço.

```python
def two_sum(nums, target):
    prev_map = {} # valor : indice
    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return []
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função para verificar se duas strings são **Anagramas** (possuem as mesmas letras na mesma quantidade).

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    # TODO: Usar um Hash Map (ou Counter) para contar letras de s
    # TODO: complete aqui
    count_s = Counter(s)
    
    # TODO: Usar um Hash Map para contar letras de t
    # TODO: complete aqui
    count_t = Counter(t)
    
    # TODO: Comparar se os dois dicionários são iguais
    # TODO: complete aqui
    return count_s == count_t
```

## 🚀 3. Do Zero (Desafio DE)
**Enunciado:** Você está processando um arquivo de logs de acesso a um servidor. Cada linha contém um `user_id` e um `ip_address`. Você precisa identificar a "Lista Negra" (Blacklist) de usuários que acessaram o servidor de **mais de 3 IPs diferentes**.

**Tarefa:** Crie uma função que receba uma lista de tuplas `(user_id, ip)` e retorne um `set` com os IDs dos usuários suspeitos.

**Critério de Aceite:**
- Use um dicionário onde a chave é o `user_id` e o valor é um `set` de IPs.
- Complexidade temporal deve ser $O(n)$.
- O resultado final deve ser um `set` para garantir unicidade e busca rápida posterior.

## 🧪 Quebre de Propósito
Tente as seguintes alterações e explique o erro:
1. **Tente resolver o "Two Sum" usando apenas Two Pointers em um array desordenado** $\rightarrow$ Erro: O resultado será incorreto. Two Pointers exige ordenação; para arrays desordenados, o Hash Map é a única forma de manter $O(n)$.
2. **Tente usar uma lista como chave do dicionário: `my_dict[[1,2]] = "valor"`** $\rightarrow$ Erro: `TypeError: unhashable type: 'list'`. Explique por que tuplas funcionam e listas não.
3. **Use um loop aninhado para contar a frequência de palavras em um texto de 1M de palavras** $\rightarrow$ Erro: O script levará horas para terminar ($O(n^2)$). Substitua por um `dict` para cair para milissegundos ($O(n)$).

---
← [[Estruturas-Dados/03-HashMaps-Sets/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/03-HashMaps-Sets/03-Tickets]] →
