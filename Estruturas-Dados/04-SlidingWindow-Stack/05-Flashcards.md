---
tipo: flashcard
trilha: estruturas-dados
capitulo: 04
titulo: "Flashcards: Sliding Window & Stack"
---
# 🗂️ Flashcards: Sliding Window & Stack

> [!question] Quando utilizar uma **Stack** (Pilha) em problemas de algoritmia?
> ?
> Quando o problema exigir a ordem **LIFO (Last-In, First-Out)**. Exemplos típicos: validação de parênteses, navegação de "voltar" no browser, ou recursão (Call Stack).

> [!question] Qual a diferença entre **Sliding Window Fixa** e **Sliding Window Dinâmica**?
> ?
> **Fixa:** O tamanho $K$ é constante. Você apenas desliza a janela mantendo o tamanho (ex: média dos últimos 60 segundos).
> **Dinâmica:** O tamanho da janela expande e contrai dependendo de uma condição (ex: menor substring que contenha todos os caracteres de X).

> [!question] Por que usar `collections.deque` para implementar janelas deslizantes em Python?
> ?
> Porque o `deque` permite adicionar e remover elementos das extremidades em **$O(1)$**, enquanto remover o primeiro elemento de uma `list` comum (`pop(0)`) é **$O(n)$**.

> [!question] Como funciona a técnica de "Salto" (Jump) na Sliding Window Dinâmica?
> ?
> Em vez de mover o ponteiro `left` um por um, você usa um mapa para guardar a última posição de cada caractere e "salta" o `left` diretamente para a posição seguinte ao caractere repetido.

> [!question] Qual a complexidade de tempo de um algoritmo de validação de parênteses usando Stack?
> ?
> **$O(n)$**, onde $n$ é o comprimento da string, pois cada caractere é empilhado e desempilhado no máximo uma vez.
