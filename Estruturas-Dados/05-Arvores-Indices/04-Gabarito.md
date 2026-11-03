---
tipo: gabarito
trilha: estruturas-dados
capitulo: 05
titulo: "Gabarito: Árvores & Índices"
---
# Gabarito: Árvores & Índices

## 🎫 DSA-05-01: O Colapso da Busca Binária
**Problema:** Substituir busca linear $O(n)$ por Busca Binária $O(\log n)$ em lista ordenada.
**Solução:** Two Pointers (Low/High).

```python
def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid # Encontrado
        elif sorted_list[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 # Não encontrado

# Teste
ids = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(binary_search(ids, 70)) # Saída: 6
```
**Complexidade:** Tempo $O(\log n)$, Espaço $O(1)$.

---

## 🎫 DSA-05-02: O Rastreador de Hierarquias
**Problema:** Calcular tamanho total de pasta recursivamente.
**Solução:** Travessia Post-Order (Filhos $\rightarrow$ Pai).

```python
class Folder:
    def __init__(self, name, size=0, children=None):
        self.name = name
        self.size = size # Tamanho do arquivo se for folha, 0 se for pasta
        self.children = children or []

def calculate_total_size(folder):
    # Base: Se a pasta não tem filhos, retorna seu próprio tamanho
    if not folder.children:
        return folder.size
    
    # Recursão: Soma o tamanho de todos os filhos (Post-Order)
    total_children_size = sum(calculate_total_size(child) for child in folder.children)
    
    # Retorna o tamanho da pasta atual + soma dos filhos
    return folder.size + total_children_size

# Teste
# root (0) -> sub1 (0) -> file1 (100)
#               -> file2 (200)
#            -> file3 (50)
f1 = Folder("file1", 100)
f2 = Folder("file2", 200)
s1 = Folder("sub1", 0, [f1, f2])
f3 = Folder("file3", 50)
root = Folder("root", 0, [s1, f3])

print(calculate_total_size(root)) # Saída: 350
```
**Complexidade:** Tempo $O(n)$ (visita cada nó uma vez), Espaço $O(h)$ onde $h$ é a altura da árvore.

---

## 🎫 DSA-05-03: O Índice Degenerado (REVIEW)
**Análise do Erro:**
A afirmação do colega está errada porque a BST (Binary Search Tree) só mantém a complexidade $O(\log n)$ se estiver **balanceada**. Quando inserimos dados já ordenados (`1, 2, 3...`), cada novo nó é inserido à direita do anterior.
A árvore deixa de ser uma árvore e torna-se, na prática, uma **Lista Encadeada**.

**Impacto:**
- Busca: $O(n)$ em vez de $O(\log n)$.
- Inserção: $O(n)$ em vez de $O(\log n)$.

**Correção:**
1. Usar **Árvores Balanceadas** (AVL, Red-Black), que rotacionam os nós para manter a altura mínima.
2. Ou, se possível, **embaralhar os dados** antes da inserção.
