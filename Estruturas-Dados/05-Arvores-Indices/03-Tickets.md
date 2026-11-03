---
tipo: ticket
trilha: estruturas-dados
capitulo: 05
titulo: "Tickets de Árvores & Índices"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-29
tags: [ticket, trees, bst, indices, leetcode, optimization]
---
# Tickets: Árvores & Índices

> [!abstract] Capítulo 05 · Tickets de Árvores & Índices
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/05-Arvores-Indices/02-Lab]] · 📦 Entrega: [[Estruturas-Dados/05-Arvores-Indices/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET DSA-05-01: O Colapso da Busca Binária (REFATORAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O pipeline de busca de metadados utiliza uma lista ordenada de chaves. O desenvolvedor implementou a busca usando `if key in list:`, o que está causando lentidão extrema em tabelas com milhões de entradas.
> **Entrada:** Lista ordenada de chaves e uma chave alvo.
> **Saída Esperada:** Refatoração para usar a técnica de **Busca Binária (Binary Search)**.

**✅ Critério de Aceite:**
- [ ] Implementação de busca binária com complexidade $O(\log n)$.
- [ ] Uso de dois ponteiros (`low`, `high`) para dividir o espaço de busca.
- [ ] Redução do tempo de resposta de segundos para milissegundos.

**💡 Dicas:**
> [!tip] Nível 1
> A busca binária só funciona se a lista estiver ordenada. 
> 
> [!tip] Nível 2
> Lembre-se de atualizar o `mid = (low + high) // 2` a cada iteração.

**🧪 Como Verificar:**
Executar com uma lista de 10 milhões de IDs; a busca deve retornar o resultado instantaneamente.

---

## 🎫 TICKET DSA-05-02: O Rastreador de Hierarquias (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** A empresa possui uma estrutura de pastas de logs aninhadas. Precisamos de uma função que calcule o tamanho total de uma pasta, somando o tamanho de todos os arquivos e subpastas recursivamente.
> **Entrada:** Raiz de uma estrutura de árvore de pastas.
> **Saída Esperada:** Inteiro representando a soma total de bytes.

**✅ Critério de Aceite:**
- [ ] Implementação de travessia **Post-Order** (visitando os filhos antes da raiz).
- [ ] Uso de recursão para navegar nas subpastas.
- [ ] Tratamento de pastas vazias.

**💡 Dicas:**
> [!tip] Nível 1
> A travessia Post-Order é a ideal aqui porque você precisa saber o tamanho dos filhos para calcular o total do pai.
> 
> [!tip] Nível 2
> Cuidado com a profundidade da árvore para evitar `RecursionError`.

**🧪 Como Verificar:**
Testar com uma estrutura de pastas com 5 níveis de profundidade e verificar se a soma final bate com a soma manual dos arquivos.

---

## 🎫 TICKET DSA-05-03: O Índice Degenerado (REVIEW)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega criou uma BST para indexar IDs de clientes. No entanto, os IDs são inseridos em ordem crescente (`1, 2, 3, 4...`). Ele afirma que a busca ainda é $O(\log n)$.
> **Código:**
> ```python
> for id in sorted_ids:
>     bst.insert(id)
> ```
> **Pergunta:** Por que a afirmação do colega está errada e qual o impacto disso na performance?

**✅ Critério de Aceite:**
- [ ] Identificar que a árvore tornou-se "degenerada" (uma lista encadeada).
- [ ] Explicar que a complexidade de busca caiu de $O(\log n)$ para $O(n)$.
- [ ] Sugerir o uso de árvores balanceadas (como **AVL** ou **Red-Black Trees**) ou a inserção de dados em ordem aleatória.

**💡 Dicas:**
> [!tip] Nível 1
> Desenhe a árvore no papel inserindo 1, 2 e 3. Você verá que ela só cresce para a direita.
> 
> [!tip] Nível 2
> Lembre-se que o $\log n$ só existe se a árvore estiver balanceada.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Estruturas-Dados/05-Arvores-Indices/01-Aula]] ou [[Estruturas-Dados/05-Arvores-Indices/02-Lab]].
