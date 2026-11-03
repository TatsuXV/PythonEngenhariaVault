---
tipo: gabarito
trilha: python
capitulo: 04
titulo: "Gabarito: Coleções"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, lists, dicts, sets]
---
# Gabarito: Coleções

## 💡 Solução do Lab (Item 2 - Complete)
```python
jan = [101, 102, 103, 104, 105]
fev = [103, 104, 106, 107, 108]

# Conversão para sets para habilitar operações de álgebra de conjuntos
set_jan = set(jan)
set_fev = set(fev)

# Intersecção: elementos presentes em AMBOS
comuns = set_jan & set_fev # Ou set_jan.intersection(set_fev)

print(list(comuns)) # [103, 104]
```
**Raciocínio:** Operações de intersecção em `set` são implementadas de forma extremamente eficiente via hash, evitando a necessidade de dois loops aninhados.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
from collections import defaultdict

def agregar_pedidos(itens):
    # Uso de defaultdict(int) para evitar verificar se a chave existe
    agregador = defaultdict(int)
    
    for product_id, quantity in itens:
        agregador[product_id] += quantity
        
    return dict(agregador)

# Teste
print(agregar_pedidos([(1, 2), (2, 1), (1, 5)])) # {1: 7, 2: 1}
```
**Raciocínio:** A complexidade é $O(n)$ porque percorremos a lista de itens apenas uma vez e o acesso ao dicionário para soma é $O(1)$.

## 🎫 Soluções dos Tickets

### P04-01: O Filtro de Duplicatas
```python
import time

ids = [i for i in range(100000)] + [i for i in range(50000)] # 150k itens, 50k duplicados

# Abordagem Ineficiente O(n^2)
start = time.time()
unicos_lento = []
for i in ids:
    if i not in unicos_lento:
        unicos_lento.append(i)
print(f"Lento: {time.time() - start:.4f}s")

# Abordagem Eficiente O(n)
start = time.time()
unicos_rapido = list(set(ids))
print(f"Rápido: {time.time() - start:.4f}s")
```

### P04-02: Mapeamento de Preços
```python
names = {1: "Teclado", 2: "Mouse"}
prices = {1: 150.0, 2: 80.0}

# Usando Dict Comprehension
produto_final = {pid: {"name": names[pid], "price": prices[pid]} for pid in names}
print(produto_final)
```

### P04-03: Auditoria de Memória
**Análise Técnica:**
A busca `if "id500" in chaves_busca` em uma lista de 1 milhão de itens exige que o Python percorra, no pior caso, todos os 1 milhão de itens (**Busca Linear $O(n)$**). Ao converter para `set`, o Python usa a função de hash do ID para saltar diretamente para a posição da memória onde o item deveria estar (**Busca Hash $O(1)$**), tornando a busca instantânea independentemente do tamanho da lista.

---
← [[Python/04-Colecoes/03-Tickets]] · [[MOC-Python]] · [[Python/05-Funcoes-TypeHints/01-Aula]] →
