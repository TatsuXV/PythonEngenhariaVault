---
tipo: flashcard
trilha: python
capitulo: 08
titulo: "Flashcards: OOP e Encapsulamento"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, oop, dataclasses]
---
# Flashcards: OOP e Encapsulamento

## 🧠 Conceitos
Qual a principal vantagem de usar `@dataclass` em vez de uma classe comum para modelos de dados?::Ela gera automaticamente métodos essenciais como `__init__`, `__repr__` e `__eq__`, reduzindo o código repetitivo (boilerplate).
O que significa definir uma dataclass como `frozen=True`?::Torna a instância da classe imutável. Qualquer tentativa de alterar um atributo após a criação resultará em um `FrozenInstanceError`.
Qual a função do decorador `@property`?::Permite definir um método que pode ser acess도 como se fosse um atributo, permitindo a implementação de getters e setters para validação de dados.

## ⌨️ Código & Sintaxe
Como criar um Factory Method em uma classe Python?::Utilizando o decorador `@classmethod`, que recebe a própria classe (`cls`) como primeiro argumento.
Qual a convenção para indicar que um atributo é "privado" ou "protegido" em Python?::Adicionar um underscore no início do nome do atributo (ex: `_price`).
Como instanciar uma dataclass `Product(id, name)`?::`p = Product(1, "Teclado")`

## ⚠️ Erros e Correções
Erro: `TypeError: 'frozen instance of Product' object does not support item assignment`. Causa?::Tentativa de alterar um atributo de uma dataclass marcada com `frozen=True`. Correção: Criar um novo objeto com os valores alterados (usando `dataclasses.replace`).
Erro: `RecursionError` ao usar `@property.setter`. Causa?::Dentro do setter, o desenvolvedor usou `self.atributo = valor` em vez de `self._atributo = valor`, chamando o setter recursivamente.

## 🧩 Cloze (Preencher)
O conceito de ==Duck Typing== em Python permite que uma função aceite qualquer objeto que implemente os métodos necessários, independentemente da classe a qual ele pertença?
resposta: Duck Typing
