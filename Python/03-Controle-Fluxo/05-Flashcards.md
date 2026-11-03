---
tipo: flashcard
trilha: python
capitulo: 03
titulo: "Flashcards: Controle de Fluxo"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, loops, performance]
---
# Flashcards: Controle de Fluxo

## 🧠 Conceitos
Qual a diferença entre `break` e `continue`?::`break` interrompe o loop completamente. `continue` pula a iteração atual e vai para a próxima.
O que é uma List Comprehension?::Uma sintaxe concisa para criar novas listas baseadas em iteráveis existentes, geralmente mais rápida que loops `for` tradicionais.
Por que evitar loops aninhados em grandes volumes de dados?::Porque eles aumentam a complexidade temporal para $O(n^2)$, tornando o processamento proibitivamente lento conforme o volume de dados cresce.

## ⌨️ Código & Sintaxe
Como iterar sobre uma lista obtendo o índice e o valor simultaneamente?::Usando a função `enumerate()`. Ex: `for i, val in enumerate(lista):`.
Qual a sintaxe básica de uma list comprehension com filtro?::`[expressao for item in iteravel if condicao]`
Como interromper um loop `while True` internamente?::Usando a palavra-chave `break`.

## ⚠️ Erros e Correções
Erro: Modificar uma lista (`.remove()`) enquanto se itera sobre ela com `for`. Resultado?::Alguns itens são pulados porque o índice da lista muda dinamicamente. Correção: Iterar sobre uma cópia (`for item in lista[:]`).
Erro: Usar `for i in range(len(lista))` para acessar itens. Problema?::É menos legível e ligeiramente mais lento que `for item in lista`. Correção: Use a iteração direta.

## 🧩 Cloze (Preencher)
A complexidade de um loop simples é $O(n)$, mas dois loops aninhados resultam em uma complexidade de ==$O(n^2)==$?
resposta: O(n^2)
