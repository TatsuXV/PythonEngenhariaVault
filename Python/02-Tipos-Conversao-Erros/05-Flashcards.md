---
tipo: flashcard
trilha: python
capitulo: 02
titulo: "Flashcards: Tipos e Erros"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, tipos, excecoes]
---
# Flashcards: Tipos e Erros

## 🧠 Conceitos
Qual a diferença entre `TypeError` e `ValueError`?::`TypeError` ocorre quando a operação é aplicada a um objeto de tipo inadequado (ex: `len(10)`). `ValueError` ocorre quando o tipo está correto, mas o valor é inadequado (ex: `int("abc")`).
O que é a filosofia EAFP?::"Easier to Ask Forgiveness than Permission" (É mais fácil pedir perdão do que permissão). Consiste em tentar executar o código e tratar a exceção, em vez de verificar todas as condições antes.
Por que evitar o "Bare Except" (`except:`)?::Porque ele captura todas as exceções, incluindo `SystemExit` e `KeyboardInterrupt`, impedindo o encerramento normal do programa.

## ⌨️ Código & Sintaxe
Qual a forma correta de converter `"10.5"` para `int`?::`int(float("10.5"))`
Como criar uma exceção customizada em Python?::`class MinhaErro(Exception): pass`
Qual a função do bloco `finally`?::Garantir que um bloco de código seja executado independentemente de ter ocorrido uma exceção ou não (útil para fechar conexões de banco).

## ⚠️ Erros e Correções
Erro: `int("10,5")` $\rightarrow$ `ValueError`. Causa?::O Python usa o ponto como separador decimal. A vírgula é interpretada como parte de uma string não numérica. Correção: `.replace(",", ".")`.
Erro: `float(None)` $\rightarrow$ `TypeError`. Causa?::Não é possível converter o tipo `NoneType` para `float`. Correção: Verificar `if value is not None` antes da conversão.

## 🧩 Cloze (Preencher)
A tipagem do Python é ==dinâmica==, o que significa que o tipo é associado ao valor/objeto e não à variável?
resposta: dinâmica
