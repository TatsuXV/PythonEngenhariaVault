---
tipo: revisao
trilha: python
capitulo: 03
titulo: "Revisão: Controle de Fluxo"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, loops, performance]
---
# Revisão: Controle de Fluxo

## ⚪ Folha em Branco
**Desafio:** Escreva um código que:
1. Gere uma lista de números de 1 a 100.
2. Use list comprehension para filtrar apenas os números múltiplos de 3 e 5.
3. Se a lista final estiver vazia, imprima "Nenhum encontrado". Caso contrário, imprima a soma dos valores.

> [!success] Comparação
> ```python
> nums = range(1, 101)
> filtrados = [n for n in nums if n % 3 == 0 and n % 5 == 0]
> print(sum(filtrados)) if filtrados else print("Nenhum encontrado")
> ```

## 🗣 Explique ao Júnior
Explique por que `[x for x in lista if cond]` é preferível a um loop `for` com `.append()` para a maioria dos casos.
> [!tip] Resposta Sugerida
> "Além de ser mais legível e conciso (estilo Pythônico), as list comprehensions são implementadas em nível de C no interpretador do Python, o que as torna significativamente mais rápidas do que chamar o método `.append()` repetidamente em cada iteração de um loop for."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/03-Controle-Fluxo/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/03-Controle-Fluxo/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/03-Controle-Fluxo/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Tipos:** Qual a diferença entre `TypeError` e `ValueError`?
2. **Setup:** Como ativar um venv no Windows PowerShell?
3. **Performance:** Por que loops aninhados são perigosos em Big Data?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (uso list comprehension naturalmente).
- [ ] 3: Consegui explicar a complexidade $O(n^2)$ para alguém.

## 📓 Registro de Erros
Sintoma: `IndexError: list index out of range`.
Causa: Tentar acessar `lista[i]` em um loop onde `i` foi incrementado além do tamanho da lista ou a lista foi reduzida durante a iteração.
Regra: Prefira a iteração direta `for item in lista` em vez de indexação manual.
Tag: #erro/loops
