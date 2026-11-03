---
tipo: gabarito
trilha: python
capitulo: 05
titulo: "Gabarito: Funções e Tipagem"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, functions, type-hints]
---
# Gabarito: Funções e Tipagem

## 💡 Solução do Lab (Item 2 - Complete)
```python
from typing import List

def filter_prices(prices: List[float], discount: float, limit: float) -> List[float]:
    # Criando nova lista via List Comprehension para evitar mutação da original
    # e garantir performance
    return [p * (1 - discount) for p in prices if (p * (1 - discount)) > limit]

# Teste
print(filter_prices([100.0, 50.0, 200.0], 0.1, 60.0)) # [90.0, 180.0]
```
**Raciocínio:** O uso de List Comprehension aqui é a forma mais Pythônica e eficiente de filtrar e transformar dados simultaneamente. A criação de uma nova lista protege a integridade dos dados de entrada.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
from typing import List, Dict, Callable, Any

def summarize_data(data: List[Dict[str, Any]], aggregator: Callable[[List[float]], float], field: str) -> Dict[str, float]:
    # Extrair apenas os valores do campo desejado
    values = [item[field] for item in data if field in item]
    
    if not values:
        return {"total": 0.0, "average": 0.0}
    
    total = aggregator(values)
    average = total / len(values)
    
    return {"total": total, "average": average}

# Exemplo de uso com função lambda como aggregator
vendas = [{"id": 1, "valor": 100.0}, {"id": 2, "valor": 200.0}]
res = summarize_data(vendas, lambda x: sum(x), "valor")
print(res) # {'total': 300.0, 'average': 150.0}
```
**Raciocínio:** O uso de `Callable` permite que a função `summarize_data` seja agnóstica à forma de agregação (pode ser soma, média ponderada, etc.), tornando o código altamente reutilizável.

## 🎫 Soluções dos Tickets

### P05-01: A Função "Canivete Suíço"
**Refatoração sugerida:**
```python
def clean_data(data): ...
def filter_data(data): ...
def aggregate_data(data): ...
def export_data(data): ...

def process_data(data, **options):
    if options.get('clean'): data = clean_data(data)
    if options.get('filter'): data = filter_data(data)
    # ... orquestração simplificada
    return data
```
**Análise:** A separação em funções puras permite que cada etapa seja testada individualmente via `pytest`, facilitando a identificação de onde ocorre um erro de transformação.

### P05-02: O Mistério do None
```python
from typing import Optional, Dict

def get_price(prices: Optional[Dict[int, float]], product_id: int) -> Optional[float]:
    if prices is None:
        return None
    return prices.get(product_id)

# Testes
print(get_price({1: 10.5}, 1)) # 10.5
print(get_price({1: 10.5}, 2)) # None
print(get_price(None, 1))      # None
```

### P05-03: Auditoria de Mutabilidade
**Falha:** A função `apply_tax` altera a lista `prices` original. Se essa lista for usada posteriormente em outro lugar do pipeline, os valores estarão errados (imposto aplicado duas vezes, por exemplo).
**Solução:**
```python
def apply_tax(prices: List[float], tax: float) -> List[float]:
    return [p * (1 + tax) for p in prices]
```
**Vantagem:** a função agora é "pura", não gera efeitos colaterais e é muito mais fácil de debugar.

---
← [[Python/05-Funcoes-TypeHints/03-Tickets]] · [[MOC-Python]] · [[Python/06-Arquivos-Pathlib/01-Aula]] →
