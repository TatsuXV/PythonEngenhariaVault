---
tipo: revisao
trilha: python
capitulo: 05
titulo: "Revisão: Funções e Tipagem"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, functions, type-hints]
---
# Revisão: Funções e Tipagem

## ⚪ Folha em Branco
**Desafio:** Escreva uma função `calculate_metrics` que aceite uma lista de dicionários, um campo numérico e uma função de agregação. Ela deve retornar a média e o total, usando Type Hints rigorosos.

> [!success] Comparação
> ```python
> from typing import List, Dict, Callable, Tuple
> 
> def calculate_metrics(data: List[Dict], field: str, agg_func: Callable[[List[float]], float]) -> Tuple[float, float]:
>     values = [row[field] for row in data if field in row]
>     if not values: return 0.0, 0.0
>     
>     total = agg_func(values)
>     return total, total / len(values)
> ```

## 🗣 Explique ao Júnior
Explique por que devemos evitar o uso de `*args` e `**kwargs` em funções que são a base de um pipeline de dados, preferindo argumentos nomeados explícitos.
> [!tip] Resposta Sugerida
> "Embora `*args` e `**kwargs` sejam flexíveis, eles tornam a função uma 'caixa preta'. Em engenharia de dados, a clareza é vital. Argumentos nomeados explícitos servem como documentação viva: qualquer pessoa que ler a assinatura da função sabe exatamente o que ela precisa para funcionar, sem ter de adivinhar quais chaves devem estar dentro do dicionário de kwargs."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/05-Funcoes-TypeHints/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/05-Funcoes-TypeHints/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/05-Funcoes-TypeHints/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Coleções:** Qual a diferença de performance entre `set` e `list` para busca de IDs?
2. **Tipos:** Como tratar a conversão de `"10,5"` para float?
3. **Controle:** Quando usar `continue` em vez de `break`?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (uso type hints e funções puras naturalmente).
- [ ] 3: Consegui refatorar um script monólito em módulos testáveis.

## 📓 Registro de Erros
Sintoma: `TypeError: 'NoneType' object is not iterable`.
Causa: Passar o retorno de uma função que resultou em `None` para um loop `for`.
Regra: Sempre tipar retornos como `Optional` e validar antes de iterar.
Tag: #erro/funcoes
