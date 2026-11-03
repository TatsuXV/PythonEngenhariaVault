---
tipo: aula
trilha: estruturas-dados
capitulo: 04
titulo: "Sliding Window & Stack: Processamento de Fluxos"
nivel: 3
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-28
tags: [sliding-window, stack, leetcode, streams, performance]
---
# Sliding Window & Stack: Processamento de Fluxos

> [!abstract] Capítulo 04 · Sliding Window & Stack
> ⏱ 6h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/03-HashMaps-Sets/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/04-SlidingWindow-Stack/07-Entrega-Projeto|Analisador de Picos de Tráfego]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] O que é a técnica de "Janela Deslizante" (Sliding Window) e como ela difere de um loop simples?
> ?
> [!question] Qual a característica principal de uma Pilha (Stack) em termos de ordem de acesso aos dados?
> ?
> [!question] Como uma Stack pode ser usada para validar se um arquivo JSON ou XML está com as tags fechadas corretamente?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a técnica de Sliding Window para processar sub-arrays/substrings de forma eficiente e a estrutura de Pilha (Stack) para gerenciar estados aninhados e ordens reversas.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, a **Sliding Window** é a base para a "Análise de Séries Temporais". Quando você calcula a média móvel de vendas dos últimos 7 dias, você não soma tudo do zero a cada dia; você "desliza" a janela, subtraindo o dia mais antigo e somando o novo. Já as **Stacks** são fundamentais para processar linguagens de marcação (JSON/XML) e para a implementação de recursão em algoritmos de busca em diretórios.

## 📚 Teoria

### 1. Sliding Window (Janela Deslizante)
Imagine uma "moldura" que se move sobre os dados. Ela evita que você precise re-processar elementos que já foram analisados.

**Tipos de Janela:**
- **Tamanho Fixo:** A janela tem sempre $K$ elementos. (Ex: Média móvel de 5 minutos).
- **Tamanho Dinâmico:** A janela cresce ou diminui dependendo de uma condição. (Ex: "Menor substring que contenha todos os caracteres X").

**Complexidade:** Quase sempre reduz $O(n^2)$ para $O(n)$.

### 2. Stack (Pilha - LIFO)
LIFO significa *Last In, First Out* (O último a entrar é o primeiro a sair). No Python, usamos a `list` com os métodos `.append()` e `.pop()`.

**Casos de Uso em DE:**
- **Validação de Parênteses/Tags:** Para cada tag aberta `<tag>`, empilhamos; para cada tag fechada `</tag>`, desempilhamos e comparamos.
- **Undo/Redo:** Armazenar estados anteriores de uma transformação de dados.
- **DFS (Depth First Search):** A base para percorrer árvores de dependências de tabelas.

## ⚠️ Armadilhas e Erros Comuns (Foco LeetCode)
- **Janela "Torta":** Esquecer de atualizar o ponteiro da esquerda (`left`) quando a condição da janela é quebrada.
- **Stack Vazia:** Tentar dar `.pop()` em uma pilha vazia $\rightarrow$ `IndexError`. Sempre verifique `if stack:`.
- **Confundir Queue com Stack:** Lembre-se: Stack é prato empilhado (topo), Queue é fila de banco (início).

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Para calcular a média móvel, use `sum(window)` a cada iteração."
> **Por que está errado:** Se a janela for grande, `sum()` torna o algoritmo $O(n \cdot k)$.
> **Correto:** Mantenha uma variável `current_sum`. Adicione o novo elemento e subtraia o que saiu da janela. Complexidade $O(1)$ por passo.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Dica de Entrevista:** Se o problema mencionar "maior substring", "menor subarray com soma X" ou "validar parênteses", comece pensando em Sliding Window ou Stack.

## 📖 Fonte
Fonte: [NeetCode - Sliding Window](https://neetcode.io/courses/algorithm-basics/sliding-window) e [GeeksforGeeks - Stack](https://www.geeksforgeeks.org/stack-data-structure/)

---
← [[Estruturas-Dados/03-HashMaps-Sets/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/04-SlidingWindow-Stack/02-Lab]] →
