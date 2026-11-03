---
tipo: aula
trilha: estruturas-dados
capitulo: 06
titulo: "Grafos & Linhagem: Orquestração de Dados"
nivel: 5
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [graphs, dag, data-lineage, topological-sort, leetcode]
---
# Grafos & Linhagem: Orquestração de Dados

> [!abstract] Capítulo 06 · Grafos & Linhagem
> ⏱ 8h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/05-Arvores-Indices/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/06-Grafos-Linhagem/07-Entrega-Projeto|Orquestrador de DAGs Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença entre um Grafo Direcionado (Directed) e um Não-Direcionado?
> ?
> [!question] O que é um DAG (Directed Acyclic Graph) e por que ele é a estrutura fundamental de orquestradores como Airflow e Prefect?
> ?
> [!//question] O que é a Ordenação Topológica (Topological Sort) e para que ela serve em um pipeline de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Compreender a representação de grafos e a implementação de algoritmos de busca (BFS e DFS). O objetivo é ser capaz de modelar a linhagem de dados (Data Lineage) e garantir que as tarefas de um pipeline sejam executadas na ordem correta de dependência.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, um pipeline não é apenas uma lista de passos, é um **Grafo**. Cada tabela é um nó e cada transformação é uma aresta. Se a Tabela C depende da Tabela A e B, temos uma dependência. O conceito de **DAG (Directed Acyclic Graph)** garante que não existam ciclos (ex: A depende de B, que depende de A), o que causaria um loop infinito no orquestrador. Saber manipular grafos permite que você depure a linhagem de dados e otimize a execução paralela de tarefas.

## 📚 Teoria

### 1. Representação de Grafos
- **Matriz de Adjacência:** Uma tabela onde `1` indica conexão. Rápida para checar se dois nós estão ligados, mas consome muita memória ($O(V^2)$).
- **Lista de Adjacência:** Um dicionário onde cada chave é um nó e o valor é uma lista de seus vizinhos. É o padrão para Big Data por ser eficiente em memória ($O(V + E)$).

### 2. Algoritmos de Busca
- **BFS (Breadth-First Search):** Visita nível por nível usando uma **Queue**. Ideal para encontrar o caminho mais curto em grafos não ponderados.
- **DFS (Depth-First Search):** Vai o mais fundo possível antes de retroceder, usando uma **Stack**. Ideal para detectar ciclos e explorar todas as possibilidades.

### 3. Ordenação Topológica (Kahn's Algorithm)
É o processo de ordenar os nós de um DAG de forma que, para toda aresta $u \rightarrow v$, o nó $u$ venha antes de $v$.
- **Aplicação:** Definir a ordem de execução de scripts SQL em um banco de dados para que as tabelas "pai" sejam criadas antes das tabelas "filhas".

## ⚠️ Armadilhas e Erros Comuns (Foco LeetCode)
- **Ciclos Infinitos:** Tentar fazer DFS em um grafo com ciclos sem marcar os nós como "visitados" $\rightarrow$ `RecursionError`.
- **Confundir Árvore com Grafo:** Uma árvore é apenas um tipo especial de grafo (conectada e sem ciclos). Nem todo grafo é uma árvore.
- **Escolha errada de Busca:** Usar DFS para achar o caminho mais curto $\rightarrow$ O resultado será um caminho válido, mas raramente o mais curto. Use BFS.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Para detectar ciclos em qualquer grafo, basta usar DFS."
> **Por uma explicação técnica:** Em grafos direcionados, você precisa de três estados de marcação (Não visitado, Visitando, Visitado) para diferenciar um ciclo de um caminho convergente.
> **Correto:** Use o algoritmo de detecção de ciclos com a pilha de recursão para DAGs.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Dica de Entrevista:** Problemas de "Linhagem de Dados" ou "Ordem de Dependências" são a aplicação direta de Grafos. Se o problema menciona "Pré-requisitos" ou "Hierarquia de Tarefas", a solução é quase sempre Ordenação Topológica.

## 📖 Fonte
Fonte: [NeetCode - Graphs](https://neetcode.io/courses/algorithm-basics/graphs) e [Introduction to Algorithms (CLRS)](https://mitpress.mit.edu/9780262033848/introduction-to-algorithms/)

---
← [[Estruturas-Dados/05-Arvores-Indices/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/06-Grafos-Linhagem/02-Lab]] →
