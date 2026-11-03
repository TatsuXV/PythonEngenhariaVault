---
tipo: flashcard
trilha: python
capitulo: 05
titulo: "Flashcards: Funções e Tipagem"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, functions, type-hints]
---
# Flashcards: Funções e Tipagem

## 🧠 Conceitos
Qual a diferença entre `*args` e `**kwargs`?::`*args` recebe argumentos posicionais extras como uma tupla. `**kwargs` recebe argumentos nomeados extras como um dicionário.
O que é uma "Função Pura"?::Uma função que, para a mesma entrada, sempre produz a mesma saída e não causa efeitos colaterais (não altera variáveis globais ou argumentos mutáveis).
Para que serve o `Optional[T]` do módulo typing?::Indica que um valor pode ser do tipo `T` ou pode ser `None`, forçando o desenvolvedor a tratar o caso `None` para evitar `AttributeError`.

## ⌨️ Código & Sintaxe
Qual a sintaxe para definir uma função que recebe qualquer número de argumentos nomeados?::`def func(**kwargs):`
Como definir o tipo de retorno de uma função que pode retornar Int ou Float?::`def func() -> Union[int, float]:` ou `def func() -> int | float:` (Python 3.10+).
Como criar uma função anônima (Lambda) que soma dois números?::`soma = lambda x, y: x + y`

## ⚠️ Erros e Correções
Erro: `def func(data=[]):`. Qual o problema?::Default Mutável. A lista `[]` é criada apenas uma vez na definição da função, persistindo dados entre chamadas sucessivas. Correção: `def func(data=None): if data is None: data = []`.
Erro: `TypeError: 'NoneType' object is not subscriptable`. Causa?::Tentativa de acessar um índice `[0]` em algo que retornou `None`. Correção: Verificar `if result is not None` antes do acesso.

## 🧩 Cloze (Preencher)
Type hints não alteram o comportamento do Python em runtime, eles são usados por ferramentas de ==análise estática== (como o mypy) para detectar bugs?
resposta: análise estática
