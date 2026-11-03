---
tipo: ticket
trilha: python
capitulo: 05
titulo: "Tickets de Funções e Tipagem"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, functions, type-hints]
---
# Tickets: Funções e Tipagem

> [!abstract] Capítulo 05 · Tickets de Funções e Tipagem
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/02-Lab]] · 📦 Entrega: [[Python/05-Funcoes-TypeHints/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P05-01: A Função "Canivete Suíço" (CONSERTAR)
**Prioridade:** Alta | **Tipo:** Bug | **Tempo:** 45min
> **Contexto:** Um desenvolvedor criou uma função que faz 5 coisas diferentes dependendo de flags booleanas. O código está ilegível e difícil de testar.
> **Entrada:** `process_data(data, clean=True, filter=True, aggregate=False, export=True, save=False)`.
> **Saída Esperada:** Refatorar a função em 4 funções menores e puras.

**✅ Critério de Aceite:** 
- [ ] Nenhuma função deve ter mais de 15 linhas.
- [ ] Cada função deve ter Type Hints e Docstrings.
- [ ] a função principal deve apenas orquestrar as chamoras.

**💡 Dicas:**
> [!tip] Nível 1
> Use o princípio de Responsabilidade Única (SRP).
> 
> [!tip] Nível 2
> Crie funções como `clean_data()`, `filter_data()`, etc.

**🧪 Como Verificar:** 
O código deve passar nos testes unitários para cada função individualmente.

---

## 🎫 TICKET P05-02: O Mistério do None (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Precisamos de uma função de busca de preço que possa retornar o preço (float) ou `None` se o produto não for encontrado.
> **Entrada:** Dicionário de preços e um `product_id`.
> **Saída Esperada:** O preço ou `None`, com a tipagem `Optional[float]`.

**✅ Critério de Aceite:** 
- [ ] Uso rigoroso de `Optional[float]` no retorno.
- [ ] Tratamento de erro caso o dicionário seja `None`.

**💡 Dicas:**
> [!tip] Nível 1
> Importe `Optional` de `typing`.
> 
> [!tip] Nível 2
> Use o método `.get()` do dicionário para retornar `None` automaticamente.

**🧪 Como Verificar:** 
`mypy` deve validar o código sem erros de tipo.

---

## 🎫 TICKET P05-03: Auditoria de Mutabilidade (REVISAR)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega escreveu a função abaixo para adicionar impostos a uma lista de preços.
> **Código:**
> ```python
> def apply_tax(prices: List[float], tax: float):
>     for i in range(len(prices)):
>         prices[i] = prices[i] * (1 + tax)
>     return prices
> ```

**✅ Critério de Aceite:** 
- [ ] Identificar que a função altera a lista original (efeito colateral).
- [ ] Sugerir a criação de uma nova lista (estilo funcional).
- [ ] Sugerir o uso de *list comprehension* para a mesma lógica.

**💡 Dicas:**
> [!tip] Nível 1
> Lembre-se que listas são mutáveis.
> 
> [!tip] Nível 2
> Uma função pura não deve alterar seus argumentos de entrada.

**🧪 Como Verificar:** 
Relatório de review descrevendo o efeito colateral e a solução sugerida.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/05-Funcoes-TypeHints/01-Aula]] ou [[Python/05-Funcoes-TypeHints/02-Lab]].
