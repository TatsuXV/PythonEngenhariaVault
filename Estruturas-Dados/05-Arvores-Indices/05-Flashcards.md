---
tipo: flashcard
trilha: estruturas-dados
capitulo: 05
titulo: "Flashcards: Árvores & Índices"
---
# 🗂️ Flashcards: Árvores & Índices

> [!question] Qual a complexidade de busca em uma **Binary Search Tree (BST)** balanceada vs degenerada?
> ?
> **Balanceada:** $O(\log n)$.
> **Degenerada (Lista):** $O(n)$.

> [!question] O que é a travessia **Post-Order** e em que caso de uso ela é essencial?
> ?
> É a travessia onde visitamos os filhos antes da raiz ($\text{Esquerda} \rightarrow \text{Direita} \rightarrow \text{Raiz}$). É essencial para deletar árvores ou calcular tamanhos de pastas (onde o total do pai depende do total dos filhos).

> [!question] Qual a diferença entre a busca binária em um **Array** vs em uma **BST**?
> ?
> No **Array**, acessamos o meio via índice $O(1)$. Na **BST**, acessamos o meio seguindo os ponteiros da raiz. Ambos têm tempo $O(\log n)$, mas a BST permite inserções e remoções mais rápidas que o array.

> [!question] O que é um **Índice B-Tree** (como usado em Bancos de Dados) e por que ele é preferido sobre BSTs para disco?
> ?
> B-Trees são árvores "largas" (mais de 2 filhos por nó). Elas minimizam a quantidade de acessos ao disco (I/O) ao carregar centenas de chaves em um único bloco de memória.

> [!question] Se você tem 1 milhão de registros, qual a diferença aproximada de iterações entre Busca Linear e Busca Binária?
> ?
> **Linear:** Até 1.000.000 de iterações.
> **Binária:** $\approx 20$ iterações ($\log_2(1.000.000) \approx 19.9$).
