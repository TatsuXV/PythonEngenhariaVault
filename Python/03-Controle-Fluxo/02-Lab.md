---
tipo: lab
trilha: python
capitulo: 03
titulo: "Lab: Lógica de Filtros e Performance"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, loops, list-comprehension]
---
# Lab: Lógica de Filtros e Performance

> [!abstract] Capítulo 03 · Lab: Lógica de Filtros e Performance
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/03-Controle-Fluxo/01-Aula]] · 📦 Entrega: [[Python/03-Controle-Fluxo/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que será impresso no final deste código?
> ```python
> dados = [10, 20, 30, 40, 50]
> resultado = [x for x in dados if x > 25]
> print(resultado)
> ```
> > [!success] Resposta
> > `[30, 40, 50]`
> > **Explicação:** A list comprehension filtra a lista `dados`, mantendo apenas os elementos que satisfazem a condição `x > 25`.

```python
# Problema: Filtrar logs de erro de um sistema
logs = [
    {"id": 1, "level": "INFO", "msg": "User logged in"},
    {"id": 2, "level": "ERROR", "msg": "Database connection failed"},
    {"id": 3, "level": "INFO", "msg": "Page loaded"},
    {"id": 4, "level": "ERROR", "msg": "Timeout occurred"},
]

# Abordagem 1: For Tradicional
erros_tradicional = []
for log in logs:
    if log["level"] == "ERROR":
        erros_tradicional.append(log["msg"])

# Abordagem 2: List Comprehension (Pythônica)
erros_pythonic = [log["msg"] for log in logs if log["level"] == "ERROR"]

print(erros_pythonic) # ['Database connection failed', 'Timeout occurred']
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente um loop que percorra uma lista de pedidos e calcule o total, mas pare a execução se encontrar um pedido com valor negativo (indicando erro grave no dado).

```python
pedidos = [100.50, 200.00, -1.0, 150.75]
total = 0.0

for valor in pedidos:
    if valor < 0:
        print("Erro: Valor negativo encontrado!")
        # TODO: Interromper o loop imediatamente
        # TODO: complete aqui
    
    # TODO: Somar o valor ao total
    # TODO: complete aqui

print(f"Total processado: {total}")
```

## 🚀 3. Do Zero
**Enunciado:** Crie um "Filtro de Eventos de Log". A função deve receber uma lista de eventos (dicionários) e:
1. Retornar apenas os eventos do nível `"CRITICAL"`.
2. Se não houver nenhum evento crítico, retornar a mensagem `"Sistema Estável"`.
3. Use list comprehension para a filtragem.

**Critério de Aceite:** 
- `filtrar([{"level": "INFO"}, {"level": "CRITICAL"}])` $\rightarrow$ `[{"level": "CRITICAL"}]`.
- `filtrar([{"level": "INFO"}])` $\rightarrow$ `"Sistema Estável"`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente usar `continue` no lugar de `break` no exercício de pedidos** $\rightarrow$ Comportamento: O loop não para, ele apenas ignora o valor negativo e continua somando os próximos.
2. **Tente usar `for i in range(len(lista))` e deletar um item com `del lista[i]`** $\rightarrow$ Erro: O índice será deslocado e você pulará o item seguinte.
3. **Crie um loop `while True:` sem um `break` interno** $\rightarrow$ Erro: Loop infinito (travamento do terminal).

---
← [[Python/03-Controle-Fluxo/01-Aula]] · [[MOC-Python]] · [[Python/03-Controle-Fluxo/03-Tickets]] →
