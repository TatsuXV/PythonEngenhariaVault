---
tipo: flashcard
trilha: python
capitulo: 04
titulo: "Flashcards: Coleções"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, colecoes, performance]
---
# Flashcards: Coleções

## 🧠 Conceitos
Qual a complexidade temporal de buscar um elemento em um `set` vs em uma `list`?::`set` é $O(1)$ (tempo constante) via hash. `list` é $O(n)$ (tempo linear) via busca sequencial.
O que é a característica de ser "hashable" em Python?::É a capacidade de um objeto ter um valor de hash que nunca muda durante sua vida. Objetos imutáveis (strings, ints, tuplas) são hashable; listas não são.
Quando usar `defaultdict` em vez de `dict` comum?::Quando você precisa de um valor padrão para chaves inexistentes, evitando a necessidade de verificar `if key in dict` antes de operações como soma ou append.

## ⌨️ Código & Sintaxe
Como remover todas as duplicatas de uma lista `L` de forma rápida?::`unique_L = list(set(L))`
Qual a sintaxe para criar um dicionário a partir de duas listas (uma de chaves e uma de valores)?::`dict(zip(keys_list, values_list))`
Como criar uma tupla com apenas um elemento?::`t = (elemento,)` (A vírgula é obrigatória para diferenciar de parênteses de expressão).

## ⚠️ Erros e Correções
Erro: `TypeError: unhashable type: 'list'`. Causa?::Tentar usar uma lista como chave de um dicionário ou como elemento de um set. Correção: Converter a lista para tupla `tuple(lista)`.
Erro: `KeyError`. Causa?::Tentar acessar uma chave que não existe em um dicionário. Correção: Usar o método `.get("chave", default)` ou `defaultdict`.

## 🧩 Cloze (Preencher)
As tuplas são ==imutáveis==, o que as torna mais leves em memória e permite que sejam usadas como chaves de dicionários?
resposta: imutáveis
