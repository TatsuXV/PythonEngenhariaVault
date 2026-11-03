---
tipo: gabarito
trilha: python
capitulo: 03
titulo: "Gabarito: Controle de Fluxo"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, loops, performance]
---
# Gabarito: Controle de Fluxo

## 💡 Solução do Lab (Item 2 - Complete)
```python
pedidos = [100.50, 200.00, -1.0, 150.75]
total = 0.0

for valor in pedidos:
    if valor < 0:
        print("Erro: Valor negativo encontrado!")
        break # Correção: interrompe o loop completamente
    
    total += valor # Correção: soma o valor ao total

print(f"Total processado: {total}") # Saída: 300.5
```
**Raciocínio:** O `break` é a ferramenta correta para interromper o processamento diante de um erro crítico. Se usássemos `continue`, o código ignoraria o `-1.0` e somaria o `150.75`, mascarando a falha.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
def filtrar_eventos(eventos):
    # Usando list comprehension para eficiência e concisão
    criticos = [e for e in eventos if e.get("level") == "CRITICAL"]
    
    return criticos if criticos else "Sistema Estável"

# Testes
print(filtrar_eventos([{"level": "INFO"}, {"level": "CRITICAL"}])) # [{'level': 'CRITICAL'}]
print(filtrar_eventos([{"level": "INFO"}])) # Sistema Estável
```
**Raciocínio:** O uso do método `.get()` em dicionários é uma boa prática para evitar `KeyError` caso a chave `"level"` esteja ausente em algum evento.

## 🎫 Soluções dos Tickets

### P03-01: O Filtro de Junk Data
```python
dados = ["Alice", "NULL", "Bob", "", "Charlie", "NULL"]
validos = [item for item in dados if item and item != "NULL"]
print(validos) # ['Alice', 'Bob', 'Charlie']
```

### P03-02: Alerta de Pico de Carga
```python
def monitor_cpu(valores):
    consecutive_high = 0
    for v in valores:
        if v >= 90:
            consecutive_high += 1
            if consecutive_high == 3:
                print("ALERTA: Pico de Carga!")
                consecutive_high = 0 # Reset após alerta
        else:
            consecutive_high = 0 # Reset se houver queda

# Teste
monitor_cpu([70, 85, 92, 95, 91, 60, 99])
```

### P03-03: Otimização de Busca
```python
import time

ids = list(range(1_000_000))
target = 999_999

# Abordagem Lenta
start = time.time()
found = -1
for i in range(len(ids)):
    if ids[i] == target:
        found = i
        break
print(f"Loop For: {time.time() - start:.4f}s")

# Abordagem Rápida (operador 'in')
start = time.time()
if target in ids:
    found = ids.index(target)
print(f"Operador In: {time.time() - start:.4f}s")
```
**Raciocínio:** O operador `in` e o método `.index()` são implementados internamente em C, evitando o overhead do interpretador Python em cada iteração do loop.

---
← [[Python/03-Controle-Fluxo/03-Tickets]] · [[MOC-Python]] · [[Python/04-Colecoes/01-Aula]] →
