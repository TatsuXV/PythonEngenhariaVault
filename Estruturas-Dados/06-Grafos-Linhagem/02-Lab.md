---
tipo: lab
trilha: estruturas-dados
capitulo: 06
titulo: "Lab: Grafos & Linhagem na Prática"
nivel: 5
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [lab, graphs, dag, topological-sort, leetcode]
---
# Lab: Grafos & Linhagem na Prática

> [!abstract] Capítulo 06 · Lab: Grafos & Linhagem
> ⏱ 4h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/06-Grafos-Linhagem/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/06-Grafos-Linhagem/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido (Padrão LeetCode)

> [!question] Problema: Course Schedule (Dependências de Tarefas)
> Você tem uma lista de cursos e suas dependências (ex: para fazer o curso 1, você deve fazer o 0). Determine se é possível completar todos os cursos.
> **Exemplo:** `numCourses = 2, prerequisites = [[1,0]]` $\rightarrow$ True.
> **Exemplo:** `numCourses = 2, prerequisites = [[1,0], [0,1]]` $\rightarrow$ False (Ciclo!).
> > [!success] Solução com Ordenação Topológica (Algoritmo de Kahn)
> > 1. Criar a lista de adjacência e calcular o `in_degree` (quantas dependências cada curso tem).
> > 2. Colocar todos os cursos com `in_degree == 0` (sem dependências) em uma Queue.
> > 3. Enquanto a Queue não estiver vazia:
> >    - Remover um curso e incrementá-lo ao contador de processados.
> >    - Para cada vizinho desse curso, decrementar seu `in_degree`.
> >    - Se o `in_degree` do vizinho chegar a 0, adicioná-lo à Queue.
> > 4. Se o contador de processados == total de cursos $\rightarrow$ return `True`.
> > **Complexidade:** $O(V + E)$ tempo e espaço.

```python
from collections import deque

def canFinish(numCourses, prerequisites):
    adj = {i: [] for i in range(numCourses)}
    in_degree = {i: 0 for i in range(numCourses)}
    
    for dest, src in prerequisites:
        adj[src].append(dest)
        in_degree[dest] += 1
        
    queue = deque([i for i in in_degree if in_degree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        for neighbor in adj[node]:
            in_degree[neighbor] -= 1
            if in_//degree[neighbor] == 0:
                queue.append(neighbor)
                
    return count == numCourses
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função de **Busca em Largura (BFS)** para encontrar a distância mínima (número de saltos) entre duas tabelas em um grafo de linhagem de dados.

```python
from collections import deque

def find_min_hops(graph, start, end):
    if start == end: return 0
    
    # TODO: Inicializar a fila com o nó inicial e a distância 0
    # TODO: complete aqui
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        # TODO: Desenfileirar o nó atual e a distância
        # TODO: complete aqui
        node, dist = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return dist + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                # TODO: Enfileirar o vizinho com a distância incrementada
                # TODO: complete aqui
                queue.append((neighbor, dist + 1))
                
    return -1 # Não há caminho
```

## 🚀 3. Do Zero (Desafio DE)
**Enunciado:** Você está construindo um orquestrador de tarefas simplificado. Você recebe um dicionário de tarefas e suas dependências.
Exemplo: `{"Task_C": ["Task_A", "Task_B"], "Task_B": ["Task_A"], "Task_A": []}`.

**Tarefa:** Implemente a função `get_execution_order()` que retorne a sequência exata de execução das tarefas (Ordenação Topológica).

**Critério de Aceite:**
- Se houver um ciclo (Dependência Circular), a função deve levantar uma exceção `CycleDetectedError`.
- A ordem deve respeitar rigorosamente as dependências.
- Complexidade temporal deve ser $O(V + E)$.

## 🧪 Quebre de Propósito
Tente as seguintes alterações e explique o erro:
1. **Use DFS para a ordenação topológica mas esqueça de marcar os nós como "visitados"** $\rightarrow$ Erro: `RecursionError` ao encontrar o primeiro ciclo.
2. **Inverta a ordem da fila na BFS** $\rightarrow$ Erro: Você encontrará um caminho, mas não necessariamente o **mais curto**.
3. **Tente processar um grafo com ciclo usando o algoritmo de Kahn sem a verificação final de count** $\rightarrow$ Erro: O código retornará uma ordem parcial, omitindo os nós envolvidos no ciclo, o que causaria falha no pipeline de produção.

---
← [[Estruturas-Dados/06-Grafos-Linhagem/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/06-Grafos-Linhagem/03-Tickets]] →
