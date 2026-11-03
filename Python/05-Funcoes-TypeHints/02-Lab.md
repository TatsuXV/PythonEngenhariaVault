---
tipo: lab
trilha: python
capitulo: 05
titulo: "Lab: Modularização e Tipagem"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, functions, type-hints]
---
# Lab: Modularização e Tipagem

> [!abstract] Capítulo 05 · Lab: Modularização e Tipagem
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/01-Aula]] · 📦 Entrega: [[Python/05-Funcoes-TypeHints/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que será impresso no console?
> ```python
> def add_item(item, box=[]):
>     box.append(item)
>     return box
> 
> print(add_item("Maçã"))
> print(add_item("Banana"))
> ```
> > [!success] Resposta
> > `['Maçã']`
> > `['Maçã', 'Banana']`
> > **Explicação:** Ocorre o erro do "Default Mutável". A lista `box` é criada apenas uma vez na definição da função e compartilhada entre todas as chamadas.

```python
from typing import List, Optional, Union

def clean_text(text: Optional[str], uppercase: bool = False) -> Optional[str]:
    """Limpa e formata texto de colunas de dados."""
    if text is None:
        return None
    
    cleaned = text.strip().lower()
    return cleaned.upper() if uppercase else cleaned

# Testes
print(clean_text("  SÃO PAULO  ", uppercase=True)) # "SÃO PAULO"
print(clean_text(None)) # None
print(clean_text("  curitiba  ")) # "curitiba"
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente uma função que processe uma lista de valores, aplicando um desconto e retornando apenas os valores que permanecem acima de um limite.

```python
from typing import List

def filter_prices(prices: List[float], discount: float, limit: float) -> List[float]:
    # TODO: Criar uma nova lista para os resultados (evitar alterar a original)
    results = # TODO: complete aqui
    
    for p in prices:
        # TODO: Calcular o valor com desconto
        final_price = # TODO: complete aqui
        
        # TODO: Adicionar à lista se for maior que o limite
        # TODO: complete aqui
        
    return results

# Teste
print(filter_prices([100.0, 50.0, 200.0], 0.1, 60.0)) # [90.0, 180.0]
```

## 🚀 3. Do Zero
**Enunciado:** Crie uma função chamada `summarize_data` que aceite:
1. Uma lista de dicionários (registros de vendas).
2. Uma função de agregação via argumento (`Callable`) para definir como a soma deve ser feita.
3. Retorne um dicionário com a soma total e a média.

**Critério de Aceite:** 
- A função deve ser genérica (funcionar para qualquer campo numérico do dicionário).
- Deve usar Type Hints rigorosos (`Callable`, `List`, `Dict`).

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Altere a assinatura para `def func(data=[])` e chame a função duas vezes** $\rightarrow$ Erro esperado: Acúmulo de dados entre chamadas (Default Mutável).
2. **Tente passar uma string onde a função espera `List[float]` e execute com `mypy`** $\rightarrow$ Erro esperado: `mypy` reportará erro de tipo, embora o Python rode (estático vs dinâmico).
3. **Altere uma lista dentro de uma função sem criar cópia** $\rightarrow$ Erro esperado: A lista original fora da função foi alterada inesperadamente.

---
← [[Python/05-Funcoes-TypeHints/01-Aula]] · [[MOC-Python]] · [[Python/06-Arquivos-Pathlib/01-Aula]] →
