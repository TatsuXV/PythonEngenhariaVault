---
tipo: ticket
trilha: estruturas-dados
capitulo: 02
titulo: "Tickets de Arrays & Two Pointers"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-26
tags: [ticket, arrays, two-pointers, leetcode, optimization]
---
# Tickets: Arrays & Two Pointers

> [!abstract] Capítulo 02 · Tickets de Arrays & Two Pointers
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/02-Arrays-TwoPointers/02-Lab]] · 📦 Entrega: [[Estruturas-Dados/02-Arrays-TwoPointers/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET DSA-02-01: O Filtro de Duplicatas em Stream (REFATORAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O pipeline de ingestão de logs recebe arrays ordenados de IDs de transação. O desenvolvedor anterior usou um loop aninhado para remover duplicatas adjacentes, resultando em $O(n^2)$ em casos de muitos duplicados.
> **Entrada:** Array ordenado de IDs: `[1, 1, 2, 2, 2, 3, 4, 4]`
> **Saída Esperada:** Array com duplicatas removidas in-place: `[1, 2, 3, 4]` e o novo tamanho do array.

**✅ Critério de Aceite:**
- [ ] Implementação usando **Two Pointers** (um ponteiro de escrita e um de leitura).
- [ ] Complexidade temporal $O(n)$ e complexidade espacial $O(1)$ (sem criar nova lista).
- [ ] O resultado deve ser modificado no array original (in-place).

**💡 Dicas:**
> [!tip] Nível 1
> Use um ponteiro `i` para rastrear a posição do último elemento único encontrado.
> 
> [!tip] Nível 2
> Percorra o array com um ponteiro `j`. Sempre que `arr[i] != arr[j]`, incremente `i` e atribua `arr[i] = arr[j]`.

**🧪 Como Verificar:**
Execute com um array de 1 milhão de elementos com muitos duplicados; o tempo de execução deve ser quase instantâneo.

---

## 🎫 TICKET DSA-02-02: O Buffer de Janela Deslizante (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Precisamos monitorar a média de latência de requisições em tempo real. O requisito é calcular a soma dos últimos `K` elementos de um array de latências sem recalculá-la do zero a cada novo elemento.
> **Entrada:** Array de latências `[10, 20, 30, 40, 50]` e `K=3`.
> **Saída Esperada:** Uma lista de somas das janelas: `[60, 90, 120]`.

**✅ Critério de Aceite:**
- [ ] Implementação do padrão **Sliding Window**.
- [ ] Complexidade temporal $O(n)$.
- [ ] A soma da nova janela deve ser calculada subtraindo o elemento que sai e somando o que entra (`Soma = Soma - arr[i-K] + arr[i]`).

**💡 Dicas:**
> [!tip] Nível 1
> Calcule a soma da primeira janela de tamanho `K` primeiro.
> 
> [!tip] Nível 2
> Evite usar `sum(arr[i:i+K])` dentro do loop, pois isso tornaria a complexidade $O(n \cdot K)$.

**🧪 Como Verificar:**
O código deve processar um array de 10 milhões de latências em menos de 1 segundo.

---

## 🎫 TICKET DSA-02-03: O Pareamento de Logs (REVIEW)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou a busca de "pares de transações com soma X" em um array desordenado usando Two Pointers, mas esqueceu de um passo crucial.
> **Código:**
> ```python
> def find_pair(arr, target):
>     l, r = 0, len(arr) - 1
>     while l < r:
>         if arr[l] + arr[r] == target: return True
>         elif arr[l] + arr[r] < target: l += 1
>         else: r -= 1
>     return False
> ```
> **Pergunta:** Por que este código falhará para a entrada `arr = [3, 1, 4, 2], target = 5`?

**✅ Criterío de Aceite:**
- [ ] Identificar que a técnica de Two Pointers (opostos) exige que o array esteja **ordenado**.
- [ ] Sugerir a adição de `arr.sort()` no início ou a substituição por um `Hash Map` (que será visto no Cap 03) para manter $O(n)$.
- [ ] Explicar a mudança na complexidade temporal se adicionar a ordenação ($O(n \log n)$).

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Estruturas-Dados/02-Arrays-TwoPointers/01-Aula]] ou [[Estruturas-Dados/02-Arrays-TwoPointers/02-Lab]].
