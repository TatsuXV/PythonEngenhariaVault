---
tipo: lab
trilha: python
capitulo: 02
titulo: "Lab: Casting e Robustez de Dados"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [lab, casting, try-except]
---
# Lab: Casting e Robustez de Dados

> [!abstract] Capítulo 02 · Lab: Casting e Robustez de Dados
> ⏱ 2h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/02-Tipos-Conversao-Erros/01-Aula]] · 📦 Entrega: [[Python/02-Tipos-Conversao-Erros/03-Tickets]] · ✅ Verificado

## 💡 1. Exemplo Resolvido

> [!question] Preveja o resultado
> O que o seguinte bloco de código imprimirá?
> ```python
> dado = "123,45"
> try:
>     print(float(dado))
> except ValueError:
>     print("Erro de conversão")
> ```
> > [!success] Resposta
> > `Erro de conversão`
> > **Explicação:** O Python não reconhece a vírgula como separador decimal (padrão americano/IEEE 754). Ele espera o ponto.

```python
import logging

def clean_numeric_value(value: str) -> float:
    """Converte string suja para float com tratamento de erro."""
    try:
        # Tratando a vírgula comum em dados brasileiros
        sanitized = value.replace(",", ".")
        return float(sanitized)
    except (ValueError, AttributeError) as e:
        logging.warning(f"Valor inválido '{value}': {e}. Retornando 0.0")
        return 0.0

# Testes
print(clean_numeric_value("123.45")) # 123.45
print(clean_numeric_value("123,45")) # 123.45
print(clean_numeric_value("ABC"))   # 0.0 (com log de warning)
```

## 🛠 2. Complete (Fill-in-the-blanks)
Implemente uma função que tenta converter um valor para inteiro, mas se falhar, tenta converter para float. Se ambos falharem, retorna `None`.

```python
def smart_convert(value: str):
    try:
        # TODO: Tentar converter para int
        # TODO: complete aqui
        return # TODO: complete aqui
    except ValueError:
        try:
            # TODO: Tentar converter para float
            # TODO: complete aqui
            return # TODO: complete aqui
        except ValueError:
            # TODO: Retornar None se tudo falhar
            # TODO: complete aqui
            pass

# Testes
print(smart_convert("10"))    # Esperado: 10 (int)
print(smart_convert("10.5"))  # Esperado: 10.5 (float)
print(smart_convert("Erro"))  # Esperado: None
```

## 🚀 3. Do Zero
**Enunciado:** Crie um "Sanitizador de Preços". A função deve receber uma string e:
1. Remover símbolos de moeda (R$, $).
2. Remover espaços em branco.
3. Converter para float.
4. Se o valor for negativo, levantar uma exceção customizada chamada `PrecoNegativoError`.

**Critério de Aceite:** 
- `sanitizar(" R$ 1.200,50 ")` $\rightarrow$ `1200.50`
- `sanitizar("- R$ 10,00")` $\rightarrow$ Levanta `PrecoNegativoError`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. **Tente converter `None` para `float()`** $\rightarrow$ Erro esperado: `TypeError` (não `ValueError`).
2. **Coloque o `except Exception` ANTES do `except ValueError`** $\rightarrow$ Erro esperado: O `ValueError` nunca será capturado pelo bloco específico, pois o genérico "engole" tudo.
3. **Use `int("10.5")` diretamente** $\rightarrow$ Erro esperado: `ValueError: invalid literal for int() with base 10`.

---
← [[Python/02-Tipos-Conversao-Erros/01-Aula]] · [[MOC-Python]] · [[Python/02-Tipos-Conversao-Erros/03-Tickets]] →
