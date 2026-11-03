---
tipo: reference
trilha: estruturas-dados
capitulo: 06
titulo: "Mapa de Padrões: Grafos $\rightarrow$ LeetCode $\rightarrow$ DE"
tags: [graphs, leetcode, data-engineering, patterns]
---
# 🗺️ Mapa de Padrões: Grafos para Engenharia de Dados

Este guia conecta a teoria de grafos do LeetCode com a aplicação real em pipelines de dados. Use-o para revisar antes de entrevistas técnicas ou para aprimorar a implementação do seu Orquestrador.

## 🎯 O Triângulo de Ouro dos Grafos em DE

| Padrão LeetCode | Algoritmo Chave | Aplicação em Engenharia de Dados | Exemplo Real |
| :--- | :--- | :--- | :--- |
| **Dependências & Ordem** | `Topological Sort` (Kahn's) | **Orquestração de Tarefas** | Definir que a `tabela_fato` só inicia após a `dim_cliente` e `dim_produto` estarem prontas. |
| **Conectividade & Impacto** | `BFS` / `DFS` | **Data Lineage (Linhagem)** | "Se eu alterar a coluna X na Tabela A, quais 15 tabelas downstream serão quebradas?" |
| **Validação de Fluxo** | `Cycle Detection` (DFS) | **Prevenção de Deadlocks** | Impedir que o Airflow tente rodar um pipeline onde A $\rightarrow$ B $\rightarrow$ A. |

---

## 💻 Guia de Implementação (Cheat Sheet)

### 1. Ordenação Topológica (O "Coração" do Airflow)
**Quando usar:** Quando o problema menciona "pré-requisitos", "ordem de execução" ou "dependências".
- **Lógica:** 
	1. Calcule o `in-degree` (quantas setas entram em cada nó).
	2. Coloque todos os nós com `in-degree == 0` em uma fila.
	3. Processe a fila, removendo as arestas dos vizinhos e adicionando novos nós com `in-degree == 0`.
- **Complexidade:** $O(V + E)$

### 2. Detecção de Ciclos (O "Seguro" do Pipeline)
**Quando usar:** Quando você precisa garantir que o grafo seja um **DAG**.
- **Lógica:** Use DFS com 3 cores:
	- `Branco`: Não visitado.
	- `Cinza`: Visitando (está na pilha de recursão atual).
	- `Preto`: Totalmente visitado.
- **Sinal de Alerta:** Se durante o DFS você encontrar um nó `Cinza`, você detectou um ciclo $\rightarrow$ `CircularDependencyError`.

### 3. Busca em Largura - BFS (O "Rastreador" de Impacto)
**Quando usar:** Para encontrar o "Blast Radius" (raio de impacto) de uma falha.
- **Lógica:** Use uma `Queue`. Visite todos os vizinhos imediatos, depois os vizinhos dos vizinhos.
- **Vantagem:** Garante que você encontrou o caminho mais curto da origem até o impacto.

---

## 🛠️ Desafios Recomendados (LeetCode)

Para dominar a Parte 6, resolva estes problemas nesta ordem:

1. **[Course Schedule](https://leetcode.com/problems/course-schedule/)** (Medium) 
   - *Foco:* Detecção de Ciclos e Topological Sort.
   - *Analogia DE:* "Posso rodar esse pipeline de tabelas sem entrar em loop?"

2. **[Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)** (Medium)
   - *Foco:* Retornar a ordem exata de execução.
   - *Analogia DE:* "Gere o script SQL de criação de tabelas na ordem correta."

3. **[Number of Islands](https://leetcode.com/problems/number-of-islands/)** (Medium)
   - *Foco:* DFS/BFS para encontrar componentes conectados.
   - *Analogia DE:* "Identificar clusters de tabelas que pertencem ao mesmo domínio de dados."

---
## 🔗 Conexão com Projeto Final
No seu **Orquestrador de DAGs Aurora**, você implementará:
- Uma classe `Graph` usando `Lista de Adjacência` (eficiência em memória).
- Um método `.validate()` que usa `Detecção de Ciclos`.
- Um método `.execute()` que usa `Topological Sort` para disparar os scripts na ordem correta.
