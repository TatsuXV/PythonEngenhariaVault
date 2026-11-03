---
tipo: aula
trilha: estruturas-dados
capitulo: 01
titulo: "Big O & Complexidade: A Ciência da Performance"
nivel: 1
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-25
tags: [big-o, complexity, leetcode, performance]
---
# Big O & Complexidade: A Ciência da Performance

> [!abstract] Capítulo 01 · Big O & Complexidade
> ⏱ 4h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[MOC-Python]] · 📦 Entrega: [[Estruturas-Dados/01-Big-O/07-Entrega-Projeto|Análise de Complexidade de Pipelines]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] O que acontece com o tempo de execução de um algoritmo $O(n)$ quando a entrada de dados dobra de tamanho?
> ?
> [!question] Qual a diferença entre Complexidade de Tempo (Time Complexity) e Complexidade de Espaço (Space Complexity)?
> ?
> [!question] Por que um algoritmo $O(1)$ é o "Santo Graal" da computação?
> ?

## 🎯 Objetivo
> [!goal]
> Compreender a notação Big O para analisar a eficiência de algoritmos. Ser capaz de olhar para um código e determinar se ele escalará para bilhões de linhas ou se causará um travamento por excesso de tempo/memória.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, a complexidade não é apenas teórica. Se você escreve um loop aninhado ($O(n^2)$) para cruzar dois datasets de 1 milhão de linhas, você terá $10^{12}$ operações. Mesmo em um computador rápido, isso levaria dias. Saber escolher entre um $O(n^2)$ e um $O(n \log n)$ é a diferença entre um pipeline que termina em segundos e um que nunca termina.

## 📚 Teoria

### 1. O que é Big O?
Big O é a linguagem matemática usada para descrever o limite superior do tempo de execução ou do uso de memória de um algoritmo conforme a entrada ($n$) cresce.

### 2. As Complexidades Mais Comuns (Da melhor para a pior)

| Notação | Nome | Descrição | Exemplo no Python |
| :--- | :--- | :--- | :--- |
| $O(1)$ | Constante | Tempo independente do tamanho da entrada. | Acessar um elemento de um `dict` por chave. |
| $O(\log n)$ | Logarítmica | O problema é dividido pela metade a cada passo. | Busca Binária em lista ordenada. |
| $O(n)$ | Linear | O tempo cresce proporcionalmente à entrada. | Percorrer uma lista com um `for` simples. |
| $O(n \log n)$ | Linearítmica | Comum em algoritmos de ordenação eficientes. | `sorted()` ou `.sort()` do Python (Timsort). |
| $O(n^2)$ | Quadrática | Loop aninhado (um loop dentro de outro). | Comparar cada item de uma lista com todos os outros. |
| $O(2^n)$ | Exponencial | O tempo dobra a cada novo elemento. | Recursão simples de Fibonacci. |

### 3. Time vs Space Complexity
- **Time Complexity:** Quantas operações o CPU executa.
- **Space Complexity:** Quanta memória RAM extra é necessária para rodar o algoritmo.
- **Trade-off:** Muitas vezes, podemos gastar mais memória (Space) para ganhar velocidade (Time), como acontece ao usar um `set` para evitar loops aninhados.

## ⚠️ Armadilhas e Erros Comuns (Foco LeetCode)
- **Ignorar a Pior Case:** No LeetCode, você deve sempre analisar o **Worst Case**. Se o código funciona para a maioria dos casos mas trava no pior, ele será reprovado.
- **Confundir $O(n)$ com "n segundos":** Big O não mede segundos, mede o *crescimento* do esforço.
- **Esquecer a complexidade de funções embutidas:** `.sort()` não é "grátis", é $O(n \log n)$. `in list` é $O(n)$, mas `in set` é $O(1)$.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Algoritmos $O(n \log n)$ são lentos para Big Data."
> **Por que está errado:** Na verdade, eles são o padrão ouro para ordenação. O problema é quando você cai para $O(n^2)$.
> **Correto:** Busque sempre reduzir a complexidade para $O(n)$ ou $O(n \log n)$. Evite a todo custo $O(n^2)$ em datasets massivos.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Dica para Entrevistas:** Sempre que resolver um problema no LeetCode, escreva a complexidade no topo do código:
> `Time: O(n) | Space: O(1)`. Isso mostra ao recrutador que você tem consciência de performance.

## 📖 Fonte
Fonte: [NeetCode - Big O](https://neetcode.io/courses/algorithm-basics/big-o) e [MIT Algorithm Course](https://ocw.mit.edu/)

---
← [[Python/Projeto-Final-Python]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/02-Arrays-TwoPointers/01-Aula]] →
