---
tipo: ticket
trilha: estruturas-dados
capitulo: 06
titulo: "Tickets de Grafos & Linhagem"
nivel: 5
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [ticket, graphs, dag, topological-sort, leetcode]
---
# Tickets: Grafos & Linhagem

> [!abstract] Capítulo 06 · Tickets de Grafos & Linhagem
> ⏱ 2h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/06-Grafos-Linhagem/02-Lab]] · 📦 Entrega: [[Estruturas-Dados/06-Grafos-Linhagem/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET DSA-06-01: A Dependência Circular (DEBUG)
**Prioridade:** Alta | **Tipo:** Stability | **Tempo:** 60min
> **Contexto:** O orquestrador de dados entrou em loop infinito. A tabela `Vendas` depende da `Clientes`, mas alguém criou um gatilho onde `Clientes` agora depende de `Vendas`.
> **Entrada:** Um grafo de dependências com um ciclo: `A -> B -> C -> A`.
> **Saída Esperada:** Detecção imediata do ciclo e levantamento de erro `CircularDependencyError`.

**✅ Critério de Aceite:**
- [ ] Implementação de detecção de ciclo usando DFS com marcação de nós (estágios: não visitado, visitando, visitado).
- [ ] O código deve identificar exatamente qual é o ciclo (quais nós estão envolvidos).
- [ ] Complexidade temporal $O(V + E)$.

**💡 Dicas:**
> [!tip] Nível 1
> Use um dicionário ou array de cores (0=Branco, 1=Cinza, 2=Preto) para rastrear a pilha de recursão.
> 
> [!tip] Nível 2
> Se você encontrar um nó que está no estado "visitando" (Cinza), você encontrou um ciclo.

**🧪 Como Verificar:**
Testar com um grafo linear (Passa) e um grafo com ciclo (Falha com erro claro).

---

## 🎫 TICKET DSA-06-02: O Caminho Crítico do Pipeline (OPTIMIZE)
**Prioridade:** Média | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** Você tem várias tarefas de extração que podem rodar em paralelo, mas algumas dependem de outras. Você precisa encontrar o "Caminho Crítico" (a sequência mais longa de tarefas) para estimar o tempo total de execução do pipeline.
> **Entrada:** DAG com pesos nas arestas (tempo de cada tarefa).
> **Saída Esperada:** O tempo total do caminho mais longo da raiz até a folha.

**✅ Critério de Aceite:**
- [ ] Implementação de busca de caminho mais longo em um DAG.
- [ ] Uso de Ordenação Topológica para processar os nós na ordem correta.
- [ ] Complexidade temporal $O(V + E)$.

**💡 Dicas:**
> [!tip] Nível 1
> Em um DAG, o caminho mais longo pode ser encontrado eficientemente processando os nós na ordem topológica.
> 
> [!tip] Nível 2
> Use Programação Dinâmica: `distancia[v] = max(distancia[v], distancia[u] + peso(u, v))`.

**🧪 Como Verificar:**
Montar um grafo com 3 caminhos de comprimentos diferentes e verificar se o script retorna o maior deles.

---

## 🎫 TICKET DSA-06-03: A Linhagem de Impacto (REVIEW)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega implementou a função `find_impacted_tables(table_name)` que lista todas as tabelas que dependem da tabela X. Ele usou BFS para encontrar todos os nós alcançáveis.
> **Código:**
> ```python
> def find_impacted(graph, start):
>     visited = set()
>     queue = deque([start])
>     while queue:
>         node = queue.popleft()
>         if node not in visited:
>             visited.add(node)
>             queue.extend(graph[node])
>     return visited
> ```
> **Pergunta:** Esta abordagem é correta para linhagem de dados? Qual a complexidade?

**✅ Critério de Aceite:**
- [ ] Confirmar que a abordagem BFS é correta para encontrar todos os descendentes (impacto).
- [ ] Identificar a complexidade como $O(V + E)$.
- [ ] Sugerir a adição de um filtro para remover a própria `start_table` do resultado final.

**💡 Dicas:**
> [!tip] Nível 1
> Pense no grafo como a estrutura de "Downstream". Qualquer nó alcançável a partir de `start` será impactado por uma mudança em `start`.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Estruturas-Dados/06-Grafos-Linhagem/01-Aula]] ou [[Estruturas-Dados/06-Grafos-Linhagem/02-Lab]].
