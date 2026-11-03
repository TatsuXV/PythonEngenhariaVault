---
tipo: ticket
trilha: python
capitulo: 02
titulo: "Tickets de Tipos e Gestão de Erros"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, casting, exceptions]
---
# Tickets: Tipos e Gestão de Erros

> [!abstract] Capítulo 02 · Tickets de Tipos e Gestão de Erros
> ⏱ 2h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/02-Tipos-Conversao-Erros/02-Lab]] · 📦 Entrega: [[Python/02-Tipos-Conversao-Erros/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P02-01: O Pipeline que Travou (CONSERTAR)
**Prioridade:** Alta | **Tipo:** Bug | **Tempo:** 30min
> **Contexto:** O pipeline de carga de pedidos está falhando com `ValueError` porque alguns campos de `total_amount` no CSV vieram como `"N/A"`.
> **Entrada:** Lista de strings `["100.50", "200.00", "N/A", "150.75"]`.
> **Saída Esperada:** Lista de floats `[100.5, 200.0, 0.0, 150.75]`.

**✅ Critério de Aceite:** 
- [ ] O código não deve travar ao encontrar `"N/A"`.
- [ ] Valores inválidos devem ser convertidos para `0.0`.

**💡 Dicas:**
> [!tip] Nível 1
> Use um loop `for` com um bloco `try...except ValueError`.
> 
> [!tip] Nível 2
> Use uma *list comprehension* com uma função auxiliar de conversão.

**🧪 Como Verificar:** 
Rodar o script com a lista de entrada e verificar se a saída é a lista de floats esperada.

---

## 🎫 TICKET P02-02: Validador de Idade (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 45min
> **Contexto:** Precisamos de uma função que valide a idade do cliente. A idade deve ser um inteiro positivo.
> **Entrada:** Qualquer valor (`"25"`, `-5`, `"ABC"`, `None`).
> **Saída Esperada:** Retornar a idade como `int` se válida, ou levantar `ValueError("Idade Inválida")` se for negativa ou não numérica.

**✅ Critério de Aceite:** 
- [ ] `valida("25")` $\rightarrow$ `25`.
- [ ] `valida("-10")` $\rightarrow$ `ValueError`.
- [ ] `valida("Texto")` $\rightarrow$ `ValueError`.

**💡 Dicas:**
> [!tip] Nível 1
> Converta para `int()` dentro de um `try`.
> 
> [!tip] Nível 2
> Após converter, verifique se `valor < 0`.

**🧪 Como Verificar:** 
`pytest` com casos de teste para positivo, negativo e não numérico.

---

## 🎫 TICKET P02-03: Auditoria de Tipos (REVISAR)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um colega escreveu a função abaixo para processar valores. Encontre 3 falhas técnicas.
> **Código:**
> ```python
> def process(val):
>     try:
>         return float(val)
>     except:
>         return 0.0
> ```

**✅ Critério de Aceite:** 
- [ ] Identificar o uso de *Bare Except*.
- [ ] Identificar a falta de logging do erro.
- [ ] Identificar que a função não trata `None` explicitamente (causaria `TypeError` capturado pelo bare except, mas sem rastro).

**💡 Dicas:**
> [!tip] Nível 1
> Olhe para a linha do `except`.
> 
> [!tip] Nível 2
> Pense no que acontece se o erro for um erro de sistema e não de dado.

**🧪 Como Verificar:** 
Lista de falhas escrita no arquivo de entrega.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/02-Tipos-Conversao-Erros/01-Aula]] ou [[Python/02-Tipos-Conversao-Erros/02-Lab]].
