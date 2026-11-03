---
tipo: revisao
trilha: python
capitulo: 08
titulo: "Revisão: OOP e Encapsulamento"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, oop, dataclasses]
---
# Revisão: OOP e Encapsulamento

> [!abstract] Capítulo 08 · Revisão de Modelagem de Domínio
> ⏱ 1h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/08-OOP-Encapsulamento/01-Aula]] · 📦 Entrega: [[Python/08-OOP-Encapsulamento/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **Dataclasses:** Sei a diferença entre uma classe comum e uma `@dataclass` e quando usar cada uma?
- [ ] **Imutabilidade:** Entendo o propósito de `frozen=True` e sei lidar com o `FrozenInstanceError`?
- [ ] **Encapsulamento:** Consigo implementar `@property` com getters e setters para validar dados (evitando valores negativos, etc)?
- [ ] **Factories:** Sei criar métodos `@classmethod` para instanciar objetos a partir de diferentes fontes (CSV, JSON)?
- [ ] **Memory Efficiency:** Compreendo por que dataclasses são preferíveis a dicionários em pipelines de larga escala?

## 🧠 Mapa Mental de Conceitos

**OOP em Python $\rightarrow$**
- **Modelagem $\rightarrow$** `@dataclass` (Boilerplate zero) $\rightarrow$ `frozen=True` (Imutabilidade/Records).
- **Acesso $\rightarrow$** Convenção `_` (Protegido) $\rightarrow$ `@property` (Blindagem/Validação).
- **Criação $\rightarrow$** `@classmethod` (Factory Methods) $\rightarrow$ `cls(...)`.
- **Filosofia $\rightarrow$** Duck Typing (Foco no comportamento, não na hierarquia).

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você precisa de uma classe `LogEntry` que registre o `timestamp`, o `level` (INFO, ERROR, WARN) e a `message`. O `timestamp` deve ser imutável e o `level` deve ser validado para aceitar apenas os três valores acima.

**Qual a melhor estratégia?**
1. Usar `@dataclass(frozen=True)`? (Sim, para a imutabilidade geral).
2. Ou usar `@property` para o `level`? (Sim, para a validação rigorosa).
3. **Solução Ideal:** Uma classe comum com `@property` para o level e atributos privados, ou uma dataclass com um método `__post_init__` para validação.

## 🔗 Links Rápidos
- Aula Teórica: [[Python/08-OOP-Encapsulamento/01-Aula]]
- Lab Prático: [[Python/08-OOP-Encapsulamento/02-Lab]]
- Tickets de Refatoração: [[Python/08-OOP-Encapsulamento/03-Tickets]]

---
← [[Python/08-OOP-Encapsulamento/05-Flashcards]] · [[MOC-Python]] · [[Python/08-OOP-Encapsulamento/07-Entrega-Projeto]] →
