---
tipo: flashcard
trilha: estruturas-dados
capitulo: 02
titulo: "Flashcards: Arrays & Two Pointers"
---
# 🗂️ Flashcards: Arrays & Two Pointers

> [!question] Quando utilizar a técnica de **Two Pointers Opostos** (um no início, outro no fim)?
> ?
> Quando o array está **ordenado** e você precisa encontrar um par de elementos que satisfaça uma condição (ex: soma alvo).

> [!question] Qual a complexidade de tempo e espaço de um algoritmo de **Two Pointers** simples?
> ?
> **Tempo:** $O(n)$ - percorremos o array apenas uma vez.
> **Espaço:** $O(1)$ - não utilizamos estruturas de dados extras.

> [!question] O que é o padrão **Sliding Window** (Janela Deslizante) e para que serve?
> ?
> É uma técnica para processar sub-arrays contíguos. Serve para calcular médias, somas ou encontrar a menor/maior janela que satisfaça um critério sem precisar recalcular a janela inteira a cada passo.

> [!question] Como evitar a complexidade $O(n \cdot K)$ ao calcular somas de janelas de tamanho $K$?
> ?
> Usando **Soma Incremental**: $\text{NovaSoma} = \text{SomaAnterior} - \text{ElementoQueSai} + \text{ElementoQueEntra}$.

> [!question] Qual a diferença fundamental entre **Two Pointers** e **Sliding Window**?
> ?
> **Two Pointers**: Geralmente foca em dois elementos específicos (podendo estar longe um do outro).
> **Sliding Window**: Foca em um **intervalo** (sub-array) de elementos e no comportamento desse intervalo enquanto ele "desliza".
