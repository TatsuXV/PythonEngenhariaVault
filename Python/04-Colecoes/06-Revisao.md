---
tipo: revisao
trilha: python
capitulo: 04
titulo: "Revisão: Coleções"
nivel: 2
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, colecoes, performance]
---
# Revisão: Coleções

## ⚪ Folha em Branco
**Desafio:** Escreva, sem consultar, um script que:
1. Receba uma lista de vendas `(produto, valor)`.
2. Calcule o total de vendas por produto usando um `defaultdict`.
3. Retorne apenas os produtos que venderam mais de 500 reais.

> [!success] Comparação
> ```python
> from collections import defaultdict
> 
> def totalizar_vendas(vendas):
>     totais = defaultdict(float)
>     for prod, valor in vendas:
>         totais[prod] += valor
>     
>     return {prod: v for prod, v in totais.items() if v > 500}
> 
> # Teste
> v = [("A", 100), ("B", 600), ("A", 500)]
> print(totalizar_vendas(v)) # {'A': 600, 'B': 600}
> ```

## 🗣 Explique ao Júnior
Explique por que você não deve usar `if id not in lista_unicos: lista_unicos.append(id)` para processar 1 milhão de registros.
> [!tip] Resposta Sugerida
> "Esse padrão cria um loop aninhado invisível. Para cada novo ID, o Python precisa percorrer a lista inteira de únicos para checar se ele já está lá. Se tivermos 1 milhão de IDs, faremos trilhões de comparações. Usando um `set`, o Python vai direto ao endereço de memória do ID via hash, tornando a operação instantânea independentemente do volume de dados."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/04-Colecoes/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/04-Colecoes/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/04-Colecoes/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Controle de Fluxo:** Qual a diferença entre `break` e `continue`?
2. **Tipos:** Como converter `"10,5"` para float de forma segura?
3. **Setup:** Qual a vantagem de pinar versões no `requirements.txt`?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (escolho set vs list sem hesitar).
- [ ] 3: Consegui explicar a complexidade $O(1)$ para alguém.

## 📓 Registro de Erros
Sintoma: `TypeError: unhashable type: 'list'` ao tentar criar um `set` de listas.
Causa: Tentativa de colocar um objeto mutável dentro de uma estrutura baseada em hash.
Regra: Tudo que for chave de dicionário ou elemento de set deve ser imutável (use tuplas).
Tag: #erro/colecoes
