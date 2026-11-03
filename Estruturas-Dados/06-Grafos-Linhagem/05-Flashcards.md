---
tipo: flashcard
trilha: estruturas-dados
capitulo: 06
titulo: "Flashcards: Grafos & Linhagem"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [flashcards, graphs, dag, topological-sort]
---
# Flashcards: Grafos & Linhagem

## 🧠 Conceitos
O que é um DAG (Directed Acyclic Graph) e por que ele é vital para orquestradores de dados?::É um Grafo Direcionado Acíclico. É vital porque garante que as tarefas de um pipeline tenham uma ordem de execução clara e que não existam dependências circulares que causariam loops infinitos.
Qual a diferença entre BFS (Busca em Largura) e DFS (Busca em Profundidade) em termos de estrutura de dados utilizada?::A BFS utiliza uma **Queue** (Fila) para explorar nível por nível; a DFS utiliza uma **Stack** (Pilha) ou Recursão para explorar um caminho até o fim antes de retroceder.
O que é a Ordenação Topológica?::É a ordenação linear dos nós de um DAG tal que para toda aresta direcionada $(u, v)$, o nó $u$ venha antes de $v$. É a base para definir a sequência de execução de jobs.

## ⌨️ Código & Sintaxe
Qual a complexidade temporal de percorrer um grafo usando a lista de adjacência com BFS ou DFS?::$O(V + E)$, onde $V$ é o número de vértices e $E$ o número de arestas.
Como detectar um ciclo em um grafo direcionado usando DFS?::Mantendo um estado de "visitando" (pilha de recursão). Se durante a exploração você encontrar um nó que já está no estado "visitando", um ciclo foi detectado.
Qual a complexidade de espaço de uma matriz de adjacência para um grafo com $V$ nós?::$O(V^2)$. Por isso é evitada em Big Data em favor da lista de adjacência.

## ⚠️ Erros e Correções
Erro: Tentar usar BFS para encontrar o caminho mais longo em um DAG. Causa?:: A BFS encontra o caminho mais curto (menor número de saltos). Para o caminho mais longo (Caminho Crítico), deve-se usar Ordenação Topológica e Programação Dinâmica.
Erro: `RecursionError` ao percorrer um grafo muito grande com DFS. Causa?:: Estouro da pilha de chamadas do Python. Correção: Implementar a DFS de forma iterativa usando uma lista como Stack explícita.
Erro: Orquestrador tentando rodar tarefas em paralelo que possuem dependência entre si. Causa?:: Falha na implementação da Ordenação Topológica ou erro na definição do DAG.

## 🧩 Cloze (Preencher)
O algoritmo de ==Kahn== é um dos métodos mais comuns para realizar a ordenação topológica de um grafo, baseando-se no cálculo do `in_degree` de cada nó?
resposta: Kahn
