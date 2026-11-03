---
tipo: ticket
trilha: python
capitulo: 04
titulo: "Tickets de Coleções"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, lists, dicts, sets]
---
# Tickets: Coleções

> [!abstract] Capítulo 04 · Tickets de Coleções
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/04-Colecoes/02-Lab]] · 📦 Entrega: [[Python/04-Colecoes/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P04-01: O Filtro de Duplicatas (PREDIZER)
**Prioridade:** Alta | **Tipo:** Bug | **Tempo:** 30min
> **Contexto:** O relatório de clientes únicos está levando minutos para rodar. O código atual usa um loop `for` com `if item not in lista_unicos: lista_unicos.append(item)`.
> **Entrada:** Lista com 100 mil IDs, metade duplicados.
> **Saída Esperada:** Lista de IDs únicos processada em milissegundos.

**✅ Critério de Aceite:** 
- [ ] Substituir a lista de controle por um `set`.
- [ ] Tempo de execução reduzido drasticamente.

**💡 Dicas:**
> [!tip] Nível 1
> Converta a lista original para `set` e depois volte para `list`.
> 
> [!tip] Nível 2
> A complexidade cai de $O(n^2)$ para $O(n)$.

**🧪 Como Verificar:** 
Medir o tempo de execução com `time.time()` antes e depois da alteração.

---

## 🎫 TICKET P04-02: Mapeamento de Preços (ESCREVER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Temos dois arquivos: um com `product_id, name` e outro com `product_id, price`. Precisamos de um único dicionário `product_id: {name, price}`.
> **Entrada:** 
> `names = {1: "Teclado", 2: "Mouse"}`
> `prices = {1: 150.0, 2: 80.0}`
> **Saída Esperada:** `{1: {"name": "Teclado", "price": 150.0}, 2: {"name": "Mouse", "price": 80.0}}`

**✅ Critério de Aceite:** 
- [ ] Usar a iteração sobre as chaves de um dos dicionários.
- [ ] Resultado final deve ser um dicionário de dicionários.

**💡 Dicas:**
> [!tip] Nível 1
> Itere sobre `names.keys()` e monte o novo dicionário.
> 
> [!tip] Nível 2
> Use a sintaxe de *dict comprehension*.

**🧪 Como Verificar:** 
Comparar o resultado final com o exemplo esperado.

---

## 🎫 TICKET P04-03: Auditoria de Memória (REVISAR)
**Prioridade:** Baixa | **Tipo:** Review | **Tempo:** 30min
> **Contexto:** Um desenvolvedor usou uma `list` para armazenar 1 milhão de chaves de busca rápida.
> **Código:**
> ```python
> chaves_busca = ["id1", "id2", ...] # 1M de itens
> if "id500" in chaves_busca:
>     print("Encontrado")
> ```

**✅ Critério de Aceite:** 
- [ ] Identificar que a busca em lista é $O(n)$.
- [ ] Sugerir a conversão para `set` para busca $O(1)$.
- [ ] Explicar a diferença de memória (sets consomem mais memória que listas, mas ganham em velocidade).

**💡 Dicas:**
> [!tip] Nível 1
> O operador `in` em listas percorre item por item.
> 
> [!tip] Nível 2
> Lembre-se de mencionar a Hash Table.

**🧪 Como Verificar:** 
Relatório de review com a sugestão de `set`.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/04-Colecoes/01-Aula]] ou [[Python/04-Colecoes/02-Lab]].
