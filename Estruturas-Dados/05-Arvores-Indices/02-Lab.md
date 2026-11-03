---
tipo: lab
trilha: estruturas-dados
capitulo: 05
titulo: "Lab: Árvores e Índices na Prática"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-29
tags: [lab, trees, bst, indices, leetcode]
---
# Lab: Árvores e Índices na Prática

> [!abstract] Capítulo 05 · Lab: Árvores e Índices
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/05-Arvores-Indices/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/05-Arvores-Indices/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido (Padrão LeetCode)

> [!question] Problema: Maximum Depth of Binary Tree
> Dada a raiz de uma árvore binária, encontre a sua profundidade máxima (número de nós do caminho da raiz até a folha mais distante).
> **Exemplo:** `[3, 9, 20, null, null, 15, 7]` $\rightarrow$ Profundidade 3.
> > [!success] Solução Recursiva (DFS)
> > 1. Caso base: Se o nó for `None`, a profundidade é 0.
> > 2. Calcule a profundidade da subárvore esquerda recursivamente.
> > 3. Calcule a profundidade da subárvore direita recursivamente.
> > 4. Retorne o maior valor entre os dois + 1 (o próprio nó atual).
> > **Complexidade:** $O(n)$ tempo, $O(h)$ espaço (onde $h$ é a altura da árvore).

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente a função de busca em uma Árvvore Binária de Busca (BST). Lembre-se de aproveitar a propriedade da BST para não percorrer a árvore inteira.

```python
def search_bst(root: TreeNode, target: int) -> TreeNode:
    # Caso base 1: Não encontrou ou a árvore está vazia
    if root is None:
        return None
        
    # Caso base 2: Encontrou o alvo
    if root.val == target:
        return root
    
    # TODO: Se o alvo for MENOR que o valor do nó atual, busque na esquerda
    # TODO: complete aqui
    if target < root.val:
        return search_bst(root.left, target)
    
    # TODO: Se o alvo for MAIOR que o valor do nó atual, busque na direita
    # TODO: complete aqui
    return search_bst(root.right, target)
```

## 🚀 3. Do Zero (Desafio DE)
**Enunciado:** Você está simulando um índice de banco de dados simplificado. Crie uma classe `DatabaseIndex` que:
1. Utilize uma BST para armazenar chaves de registros e seus respectivos endereços de memória (strings).
2. Implemente o método `insert(key, address)`.
3. Implemente o método `get_address(key)` que retorne o endereço em $O(\log n)$.
4. Implemente um método `get_all_sorted()` que utilize a travessia **In-Order** para retornar todas as chaves ordenadas.

**Critério de Aceite:**
- A busca deve ser estritamente logarítmica.
- O método `get_all_sorted` deve retornar a lista correta sem usar `sorted()`.

## 🧪 Quebre de Propósito
Tente as seguintes alterações e explique o erro:
1. **Insira os números [1, 2, 3, 4, 5] em sequência na BST** $\rightarrow$ Erro: A árvore vira uma lista. A busca deixa de ser $O(\log n)$ e vira $O(n)$.
2. **Tente fazer a travessia In-Order mas imprima a raiz primeiro** $\rightarrow$ Erro: Você acabou de fazer uma travessia Pre-Order; os dados não sairão ordenados.
3. **Remova o caso base `if not root` da recursão** $\rightarrow$ Erro: `AttributeError: 'NoneType' object has no attribute 'val'`.

---
← [[Estruturas-Dados/05-Arvores-Indices/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/05-Arvores-Indices/03-Tickets]] →
