---
tipo: flashcard
trilha: estruturas-dados
capitulo: 03
titulo: "Flashcards: Hash Maps & Sets"
---
# 🗂️ Flashcards: Hash Maps & Sets

> [!question] Qual a complexidade de tempo média para Inserção, Busca e Remoção em um **Hash Map** (Python `dict`) ou **Set**?
> ?
> **$O(1)$**. É a estrutura mais eficiente para buscas rápidas.

> [!question] Qual a principal diferença entre um **Set** e uma **Lista** em termos de performance de busca (`if x in container`)?
> ?
> **Lista:** Busca linear $O(n)$.
> **Set:** Busca via hash $O(1)$.

> [!question] O que acontece em caso de **Colisão de Hash**?
> ?
> Ocorre quando duas chaves diferentes geram o mesmo índice no array interno. O Python resolve isso usando **Open Addressing** (procura o próximo espaço vazio), mas em geral, isso pode degradar a performance para $O(n)$ no pior caso extremo.

> [!question] Quando utilizar um `dict` em vez de um `set`?
> ?
> Use `set` quando precisar apenas de **unicidade** ou operações de conjuntos (união, interseção).
> Use `dict` quando precisar associar uma **chave a um valor** (ex: ID do cliente $\rightarrow$ Objeto Cliente).

> [!question] Qual a complexidade de tempo para a operação de interseção de dois sets de tamanho $n$ e $m$?
> ?
> **$O(\min(n, m))$**. O Python percorre o menor set e checa a existência de cada elemento no maior.
