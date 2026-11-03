---
tipo: gabarito
trilha: estruturas-dados
capitulo: 06
titulo: "Gabarito: Grafos & Linhagem"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [gabarito, graphs, dag, topological-sort]
---
# Gabarito: Grafos & Linhagem

## 💡 Solução do Lab (Item 2 - BFS Min Hops)
```python
from collections import deque

def find_min_hops(graph, start, end):
    if start == end: return 0
    
    queue = deque([(start, 0)])
    visited = {start}
    
    while queue:
        node, dist = queue.popleft()
        
        for neighbor in graph.get(node, []):
            if neighbor == end:
                return dist + 1
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
                
    return -1 
```
**Raciocínio:** A BFS (Busca em Largura) é a ferramenta ideal para encontrar o caminho mais curto em grafos sem peso, pois ela explora todos os nós de distância 1, depois distância 2, e assim por diante.

## 🚀 Solução do Lab (Item 3 - Orquestrador de Tarefas)
```python
class CycleDetectedError(Exception): pass

def get_execution_order(tasks):
    # Construir in_degree e lista de adjacência
    in_degree = {u: 0 for u in tasks}
    adj = {u: [] for u in tasks}
    
    for task, deps in tasks.items():
        for dep in deps:
            adj[dep].append(task)
            in_degree[task] += 1
            
    # Fila de nós sem dependências
    queue = deque([u for u in in_degree if in_degree[u] == 0])
    order = []
    
    while queue:
        u = queue.popleft()
        order.append(u)
        for v in adj[u]:
            in_degree[v] -= 1
            if in_//degree[v] == 0:
                queue.append(v)
                
    if len(order) != len(tasks):
        raise CycleDetectedError("Dependência circular detectada!")
        
    return order
```
**Raciocínio:** Utilizamos o Algoritmo de Kahn. Ele remove sistematicamente as tarefas "folhas" (sem dependências), liberando as tarefas subsequentes. Se restarem tarefas não processadas, significa que há um ciclo.

## 🎫 Soluções dos Tickets

### DSA-06-01: A Dependência Circular
```python
def has_cycle(graph):
    visited = {} # 0: não visitado, 1: visitando, 2: visitado
    
    def dfs(u):
        visited[u] = 1 # Marcando como visitando
        for v in graph.get(u, []):
            if visited.get(v, 0) == 1: return True # Ciclo!
            if visited.get(v, 0) == 0 and dfs(v): return True
        visited[u] = 2 # Marcando como visitado
        return False

    for node in graph:
        if visited.get(node, 0) == 0 and dfs(node): return True
    return False
```

### DSA-06-02: O Caminho Crítico
```python
def longest_path(graph, weights):
    # 1. Ordenação Topológica
    order = get_execution_order(graph) # Reutiliza a função do lab
    dist = {node: 0 for node in graph}
    
    for u in order:
        for v in graph.get(u, []):
            weight = weights.get((u, v), 0)
            if dist[v] < dist[u] + weight:
                dist[v] = dist[u] + weight
                
    return max(dist.values())
```

### DSA-06-03: A Linhagem de Impacto
**Análise:** A abordagem BFS é a correta. Ao começar no nó X e visitar todos os alcançáveis, você encontra todo o "downstream" (tabelas impactadas). A complexidade $O(V+E)$ é ótima. A única sugestão é remover a tabela de origem do resultado para evitar confusão no relatório de impacto.

---
← [[Estruturas-Dados/06-Grafos-Linhagem/03-Tickets]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/06-Grafos-Linhagem/07-Entrega-Projeto]] →
