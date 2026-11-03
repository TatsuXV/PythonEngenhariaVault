---
tipo: aula
trilha: estruturas-dados
capitulo: 05
titulo: "Árvores & Índices: A Anatomia da Busca Rápida"
nivel: 4
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-29
tags: [trees, binary-search-tree, indices, b-tree, leetcode, performance]
---
# Árvores & Índices: A Anatomia da Busca Rápida

> [!abstract] Capítulo 05 · Árvores & Índices
> ⏱ 8h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/01-Big-O/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/05-Arvores-Indices/07-Entrega-Projeto|Simulador de Indexação de Banco de Dados]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Por que uma busca em uma Árvore Binária de Busca (BST) é mais rápida do que em um Array ordenado se ambos usam a lógica de dividir ao meio?
> ?
> [!question] O que acontece com a performance de uma BST se inserirmos os dados já ordenados?
> ?
> [!//question] Qual a diferença entre a travessia In-Order, Pre-Order e Post-Order?
> ?

## 🎯 Objetivo
> [!goal]
> Compreender a estrutura de árvores, especificamente Binary Search Trees (BST), e como elas são a base dos índices de bancos de dados (B-Trees). O objetivo é ser capaz de implementar buscas, inserções e travessias, entendendo como a estrutura dos dados dita a velocidade da query.

## ⚙️ No Pipeline
> [!pipeline]
> Para um Engenheiro de Dados, a árvore não é apenas um conceito de algoritmo; é a razão pela qual o seu banco de dados não trava ao buscar um cliente entre 100 milhões. Quando você cria um `INDEX` em uma coluna SQL, o banco cria internamente uma **B-Tree**. Entender como a árvore funciona permite que você desenhe esquemas de dados que evitam o "Full Table Scan" (leitura de toda a tabela), que é o maior inimigo da performance em Big Data.

## 📚 Teoria

### 1. Binary Search Tree (BST)
Uma BST é uma árvore onde:
- O filho à **esquerda** é sempre menor que o nó pai.
- O filho à **direita** é sempre maior que o nó pai.
- **Resultado:** A busca torna-se $O(\log n)$.

### 2. Travessias (Tree Traversals)
Como "visitar" todos os nós da árvore:
- **In-Order (Esquerda, Raiz, Direita):** Retorna os elementos em ordem crescente.
- **Pre-Order (Raiz, Esquerda, Direita):** Útil para clonar a árvore.
- **Post-Order (Esquerda, Direita, Raiz):** Útil para deletar a árvore ou calcular tamanhos de pastas.

### 3. De BST para B-Tree (O mundo real do SQL)
BSTs podem ficar "desbalanceadas" (virar uma lista). Bancos de dados usam **B-Trees**, que são árvores balanceadas com múltiplos filhos por nó. Isso reduz a "altura" da árvore, minimizando a quantidade de leituras no disco (I/O), que é a operação mais lenta de um computador.

## ⚠️ Armadilhas e Erros Comuns (Foco LeetCode)
- **Recursão Infinita:** Esquecer o caso base (`if node is None`) em funções recursivas $\rightarrow$ `RecursionError`.
- **BST Desbalanceada:** Inserir dados já ordenados em uma BST simples cria uma "árvore degenerada" (uma linha), transformando $O(\log n)$ em $O(n)$.
- **Confundir BFS com DFS:**
    - **DFS (Depth First Search):** Usa **Stack** (vai até o fundo primeiro).
    - **BFS (Breadth First Search):** Usa **Queue** (visita nível por nível).

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Sempre use recursão para percorrer árvores por ser mais simples."
> **Por que está errado:** Em árvores muito profundas, a recursão pode estourar a pilha de chamadas (`Stack Overflow`).
> **Correto:** Para árvores massivas, implemente a travessia de forma iterativa usando a sua própria `Stack` ou `Queue`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Dica de Entrevista:** Se o problema envolve "hierarquias", "dependências" ou "busca eficiente em dados ordenados", pense em Árvores. Pratique a implementação de `insert`, `search` e `delete` em BSTs.

## 📖 Fonte
Fonte: [NeetCode - Trees](https://neetcode.io/courses/algorithm-basics/trees) e [GeeksforGeeks - B-Tree](https://www.geeksforgeeks.org/introduction-of-b-tree/)

---
← [[Estruturas-Dados/04-SlidingWindow-Stack/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/05-Arvores-Indices/02-Lab]] →
