---
tipo: revisao
trilha: python
capitulo: 02
titulo: "Revisão: Tipos e Gestão de Erros"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, tipos, excecoes]
---
# Revisão: Tipos e Gestão de Erros

## ⚪ Folha em Branco
**Desafio:** Escreva, sem consultar, uma função `safe_float(valor)` que:
1. Tenta converter a entrada para float.
2. Trata vírgulas decimais.
3. Retorna `0.0` se a conversão falhar.
4. Loga o erro usando `logging.warning`.

> [!success] Comparação
> ```python
> import logging
> def safe_float(valor):
>     try:
>         return float(str(valor).replace(",", "."))
>     except (ValueError, TypeError):
>         logging.warning(f"Erro ao converter {valor}")
>         return 0.0
> ```

## 🗣 Explique ao Júnior
Explique a diferença entre `TypeError` e `ValueError` usando o exemplo de uma função que soma dois números.
> [!tip] Resposta Sugerida
> "Se você passar um número e uma string para a função de soma, o Python dirá `TypeError` porque ele não sabe somar tipos diferentes. Agora, se você passar a string `'ABC'` para uma função que espera converter esse texto em número, o tipo está certo (é string), mas o conteúdo é inválido para a operação: isso é um `ValueError`."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/02-Tipos-Conversao-Erros/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/02-Tipos-Conversao-Erros/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/02-Tipos-Conversao-Erros/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Setup:** Como você garante que a versão do pandas seja a mesma em todas as máquinas?
2. **Tipos:** Por que `int("10.5")` falha mas `int(float("10.5"))` funciona?
3. **Gestão:** Qual a diferença entre `except Exception as e` e `except:`?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (faço casting seguro sem olhar a aula).
- [ ] 3: Consegui explicar EAFP vs LBYL para alguém.

## 📓 Registro de Erros
Sintoma: `float(None)` $\rightarrow$ `TypeError`.
Causa: Tentativa de converter o objeto `None` (NoneType) que não possui método de conversão numérica.
Regra: Sempre validar `if valor is not None` ou capturar `TypeError` junto com `ValueError` em conversões.
Tag: #erro/tipos
