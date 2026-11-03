---
tipo: ticket
trilha: estruturas-dados
capitulo: 04
titulo: "Tickets de Sliding Window & Stack"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-28
tags: [ticket, sliding-window, stack, leetcode, performance]
---
# Tickets: Sliding Window & Stack

> [!abstract] Capítulo 04 · Tickets de Sliding Window & Stack
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/04-SlidingWindow-Stack/02-Lab]] · 📦 Entrega: [[Estruturas-Dados/04-SlidingWindow-Stack/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET DSA-04-01: O Monitor de Picos de CPU (REFATORAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O sistema de monitoramento calcula a média de CPU a cada 10 segundos usando os últimos 60 segundos de dados. O código atual usa `sum(data[-60:]) / 60` a cada segundo. Em alta frequência, isso está consumindo CPU desnecessariamente.
> **Entrada:** Stream de valores de CPU.
> **Saída Esperada:** Implementação de uma Janela Deslizante Fixa.

**✅ Critério de Aceite:**
- [ ] Implementar a lógica de "Subtrai o antigo, Soma o novo".
- [ ] Complexidade temporal $O(1)$ por atualização de média.
- [ ] O código deve lidar com o estado inicial (quando a janela ainda não tem 60 elementos).

**💡 Dicas:**
> [!tip] Nível 1
> Mantenha uma variável `running_sum`. A cada novo dado, `running_sum += novo - antigo`.
> 
> [!tip] Nível 2
> Use `collections.deque` com `maxlen=60` para gerenciar a janela de forma eficiente.

**🧪 Como Verificar:**
Comparar o tempo de CPU do script original vs a versão com sliding window usando `timeit`.

---

## 🎫 TICKET DSA-04-02: O Validador de JSON Aninhado (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** O pipeline recebe arquivos JSON fragmentados. Precisamos de uma função que valide se a estrutura de chaves `{}` e colchetes `[]` está balanceada antes de tentar fazer o parse final.
> **Entrada:** String de texto representando um fragmento de JSON.
> **Saída Esperada:** Booleano (`True` se balanceado, `False` caso contrário).

**✅ Critério de Aceite:**
- [ ] Implementação rigorosa usando uma **Stack**.
- [ ] Deve validar pares correspondentes: `{` com `}`, `[` com `]`.
- [ ] Deve retornar `False` imediatamente se encontrar um fechamento sem abertura correspondente.

**💡 Dicas:**
> [!tip] Nível 1
> Use um dicionário de mapeamento para os pares: `mapping = {')': '(', '}': '{', ']': '['}`.
> 
> [!tip] Nível 2
> Lembre-se de verificar se a pilha está vazia ao final do processamento.

**🧪 Como Verificar:**
Testar com: `{"a": [1, 2, {"b": 3}]}` (True) e `{"a": [1, 2}` (False).

---

## 🎫 TICKET DSA-04-03: a Maior Substring Única (REVIEW)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou a busca pela maior substring sem caracteres repetidos usando dois loops aninhados ($O(n^2)$).
> **Código:**
> ```python
> def longest_unique(s):
>     max_len = 0
>     for i in range(len(s)):
>         seen = set()
>         for j in range(i, len(s)):
>             if s[j] in seen: break
>             seen.add(s[j])
>             max_len = max(max_len, j - i + 1)
>     return max_len
> ```
> **Pergunta:** Como transformar isso em $O(n)$ usando a técnica de Sliding Window Dinâmica?

**✅ Critério de Aceite:**
- [ ] Identificar que o loop interno é redundante.
- [ ] Sugerir o uso de dois ponteiros (`left`, `right`) e um `dict` para guardar a última posição de cada caractere.
- [ ] Explicar que, ao encontrar um repetido, o ponteiro `left` deve saltar diretamente para `posicao_do_repetido + 1`.

**💡 Dicas:**
> [!tip] Nível 1
> Este é um dos problemas mais comuns do LeetCode (Longest Substring Without Repeating Characters).
> 
> [!tip] Nível 2 the la l'idée est de "empurrar" a janela da esquerda apenas o necessário.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Estruturas-Dados/04-SlidingWindow-Stack/01-Aula]] ou [[Estruturas-Dados/04-SlidingWindow-Stack/02-Lab]].
