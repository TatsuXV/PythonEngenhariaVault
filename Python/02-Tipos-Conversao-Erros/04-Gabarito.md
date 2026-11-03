---
tipo: gabarito
trilha: python
capitulo: 02
titulo: "Gabarito: Tipos e Gestão de Erros"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [gabarito, casting, excecoes]
---
# Gabarito: Tipos e Gestão de Erros

## 💡 Solução do Lab (Item 2 - Complete)
```python
def smart_convert(value: str):
    try:
        # Tentar converter para int
        return int(value)
    except (ValueError, TypeError):
        try:
            # Tentar converter para float
            return float(value)
        except (ValueError, TypeError):
            # Retornar None se tudo falhar
            return None

# Testes
print(smart_convert("10"))    # 10 (int)
print(smart_convert("10.5"))  # 10.5 (float)
print(smart_convert("Erro"))  # None
```
**Raciocínio:** A ordem de tentativa importa. Se tentarmos `float()` primeiro, `"10"` vira `10.0`. Tentando `int()` primeiro, preservamos o tipo inteiro.

## 🚀 Solução do Lab (Item 3 - Do Zero)
```python
class PrecoNegativoError(Exception):
    """Exceção customizada para preços negativos."""
    pass

def sanitizar(valor: str) -> float:
    # 1. Limpeza de strings
    limpo = valor.strip().replace("R$", "").replace("$", "").replace(" ", "").replace(",", ".")
    
    try:
        preco = float(limpo)
    except ValueError:
        raise ValueError(f"Valor '{valor}' não é um número válido.")
    
    if preco < 0:
        raise PrecoNegativoError(f"Preço não pode ser negativo: {preco}")
        
    return preco

# Testes
print(sanitizar(" R$ 1.200,50 ")) # 1200.5
# print(sanitizar("- R$ 10,00")) # Levanta PrecoNegativoError
```

## 🎫 Soluções dos Tickets

### P02-01: O Pipeline que Travou
```python
def process_amounts(amounts):
    results = []
    for val in amounts:
        try:
            results.append(float(val))
        except ValueError:
            results.append(0.0) # Imputação de valor
    return results

# Teste
entrada = ["100.50", "200.00", "N/A", "150.75"]
print(process_amounts(entrada)) # [100.5, 200.0, 0.0, 150.75]
```

### P02-02: Validador de Idade
```python
def valida_idade(valor):
    try:
        idade = int(valor)
        if idade < 0:
            raise ValueError("Idade Inválida")
        return idade
    except (ValueError, TypeError):
        raise ValueError("Idade Inválida")

# Testes
# print(valida_idade("25"))   # 25
# print(valida_idade("-10"))  # ValueError
# print(valida_idade("ABC"))  # ValueError
```

### P02-03: Auditoria de Tipos
**Falhas identificadas:**
1. **Bare Except (`except:`):** Captura inclusive sinais de interrupção do sistema (Ctrl+C), dificultando a parada do script.
2. **Falta de Logging:** O erro é silenciado e retorna `0.0`. Em produção, você nunca saberia que os dados estão vindo errados.
3. **Ambiguidade do Retorno:** Retornar `0.0` em caso de erro torna impossível distinguir um valor que era realmente zero de um valor que era inválido.

---
← [[Python/02-Tipos-Conversao-Erros/03-Tickets]] · [[MOC-Python]] · [[Python/03-Controle-Fluxo/01-Aula]] →
