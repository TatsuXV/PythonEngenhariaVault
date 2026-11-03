---
tipo: aula
trilha: python
capitulo: 03
titulo: "Controle de Fluxo: Lógica e Eficiência"
nivel: 2
tempo_estimado_h: 5
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [controle-fluxo, loops, performance]
---
# Controle de Fluxo: Lógica e Eficiência

> [!abstract] Capítulo 03 · Controle de Fluxo: Lógica e Eficiência
> ⏱ 5h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/02-Tipos-Conversao-Erros/01-Aula]] · 📦 Entrega: [[Python/03-Controle-Fluxo/07-Entrega-Projeto|Motor de Filtragem de Eventos]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença de performance entre um loop `for` tradicional e uma *List Comprehension* em Python?
> ?
> [!question] Quando você deve usar `while` em vez de `for` em um pipeline de dados?
> ?
> [!question] O que acontece se você usar `break` dentro de um loop aninhado? Ele sai de todos os loops ou apenas do interno?
> ?

## 🎯 Objetivo
> [!goal]
> Implementar lógicas de decisão e repetição eficientes, dominando a sintaxe de Python e entendendo como evitar gargalos de performance comuns em processamento de grandes volumes de dados.

## ⚙️ No Pipeline
> [!pipeline]
> Em engenharia de dados, loops são perigosos. Processar 10 milhões de linhas com um `for` loop tradicional no Python é ordens de magnitude mais lento do que usar operações vetorizadas (como as do pandas). No entanto, para orquestração, chamadas de API e tratamento de exceções linha a linha, o controle de fluxo clássico é essencial. O segredo é saber **onde** usar cada um.

## 📚 Teoria

### 1. Tomada de Decisão (`if`, `elif`, `else`)
A lógica é similar ao Java, mas Python usa `elif` em vez de `else if`.

**Operadores Lógicos:**
- `and` (E)
- `or` (OU)
- `not` (NÃO)

### 2. Loops de Repetição (`for` e `while`)
O `for` no Python é, na verdade, um *iterator*. Ele percorre qualquer objeto iterável (listas, strings, dicionários, arquivos).

**Exemplo de Iteração Eficiente:**
```python
# Evite:
for i in range(len(lista)):
    print(lista[i])

# Prefira:
for item in lista:
    print(item)

# Se precisar do índice, use enumerate:
for i, item in enumerate(lista):
    print(f"Linha {i}: {item}")
```

### 3. Controle de Interrupção (`break`, `continue`, `pass`)
- `break`: Sai do loop imediatamente.
- `continue`: Pula para a próxima iteração.
- `pass`: Operador nulo (usado como placeholder).

### 4. List Comprehensions (A "Magia" do Python)
Uma forma concisa e performática de criar listas. É a porta de entrada para a programação funcional em Python.

**Comparação:**
```python
# Tradicional
quadrados = []
for x in range(10):
    if x % 2 == 0:
        quadrados.append(x**2)

# List Comprehension
quadrados = [x**2 for x in range(10) if x % 2 == 0]
```

## ⚠️ Armadilhas e Erros Comuns
- **Loops Aninhados ($O(n^2)$):** Fazer um loop dentro de outro para comparar dados. Ex: Comparar cada linha de um CSV de 100k linhas com outro de 100k linhas resultaria em $10^{10}$ operações. **Solução:** Use Hash Maps (Dicionários).
- **Modificar a lista enquanto itera:** Remover itens de uma lista usando `remove()` dentro de um `for` causa a perda de elementos (o índice pula). **Solução:** Itere sobre uma cópia `for item in lista[:]`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Sempre use `while` para ler arquivos grandes."
> **Por que está errado:** Ler arquivos com `while` e `.readline()` manualmente é lento.
> **Correto:** O objeto de arquivo no Python já é um iterador. Use `for line in file:`, que implementa *buffering* interno e é muito mais eficiente.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Walrus Operator (`:=`):** Introduzido no Python 3.8, permite atribuir um valor a uma variável *dentro* de uma expressão (ex: dentro de um `while` ou `if`).
> `while (line := file.readline()):`

## 📖 Fonte
Fonte: [Python Docs - Control Flow](https://docs.python.org/3/tutorial/controlflow.html) (Versão 3.12)

---
← [[Python/02-Tipos-Conversao-Erros/01-Aula]] · [[MOC-Python]] · [[Python/04-Colecoes/01-Aula]] →
