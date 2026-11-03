---
tipo: aula
trilha: python
capitulo: 04
titulo: "Coleções: Listas, Dicionários e Conjuntos"
nivel: 2
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [colecoes, lists, dicts, sets]
---
# Coleções: Listas, Dicionários e Conjuntos

> [!abstract] Capítulo 04 · Coleções: Listas, Dicionários e Conjuntos
> ⏱ 6h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/03-Controle-Fluxo/01-Aula]] · 📦 Entrega: [[Python/04-Colecoes/07-Entrega-Projeto|Agregador de Vendas por Categoria]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença de complexidade temporal para buscar um elemento em uma `list` vs em um `set`?
> ?
> [!question] Quando você deve usar um `tuple` em vez de uma `list` em um pipeline de dados?
> ?
> [!question] O que acontece se você tentar usar uma `list` como chave de um `dict`? Por quê?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar as principais estruturas de dados do Python, escolhendo a coleção correta para cada cenário de manipulação de dados para maximizar a performance e minimizar o uso de memória.

## ⚙️ No Pipeline
> [!pipeline]
> Em engenharia de dados, a escolha da coleção define se o seu script termina em 10 segundos ou em 10 horas. Por exemplo, para remover duplicatas de 1 milhão de IDs, converter a lista para um `set` é instantâneo ($O(1)$ por elemento), enquanto fazer um loop `if id not in unique_list` é catastrófico ($O(n^2)$).

## 📚 Teoria

### 1. Listas (`list`) - Sequências Ordenadas
As listas são dinâmicas e permitem duplicatas.
- **Uso:** Quando a ordem dos elementos importa.
- **Performance:** Acesso por índice é $O(1)$, mas busca por valor é $O(n)$.

### 2. Conjuntos (`set`) - Coleções Únicas
Conjuntos não permitem duplicatas e não possuem ordem. São implementados via Hash Tables.
- **Uso:** Remoção de duplicatas, operações de álgebra de conjuntos (união, intersecção).
- **Performance:** Busca, inserção e remoção são $O(1)$ (estatisticamente).

### 3. Dicionários (`dict`) - Pares Chave-Valor
A estrutura mais poderosa do Python. Mapeia chaves únicas para valores.
- **Uso:** Indexação de dados, cache (memoization), contagem de ocorrências.
- **Performance:** Acesso via chave é $O(1)$.

### 4. Tuplas (`tuple`) - Sequências Imutáveis
Semelhantes a listas, mas não podem ser alteradas após a criação.
- **Uso:** Retorno de múltiplas funções, chaves de dicionários (pois são *hashable*).
- **Vantagem:** Mais leves em memória e mais rápidas que listas.

## ⚖️ Tabela Comparativa de Performance

| Operação | List (`list`) | Set (`set`) | Dict (`dict`) | Complexidade |
| :--- | :---: | :---: | :---: | :---: |
| Acesso por Índice/Chave | ✅ | ❌ | ✅ | $O(1)$ |
| Busca por Valor | ❌ (Lento) | ✅ (Rápido) | ✅ (Rápido) | $O(1)$ vs $O(n)$ |
| Inserção (fim) | ✅ | ✅ | ✅ | $O(1)$ |
| Remoção de Duplicatas | ❌ | ✅ | ✅ (chaves) | $O(n)$ |

## ⚠️ Armadilhas e Erros Comuns
- **Uso de Listas para Busca:** Usar `if item in lista` dentro de um loop. Se a lista for grande, o script trava. **Solução:** Converta para `set`.
- **Mutabilidade de Chaves:** Tentar usar uma lista como chave de dicionário. `dicts` exigem chaves imutáveis (*hashable*). **Solução:** Use tuplas.
- **Confundir `dict.keys()` com `dict.values()`:** Tentar iterar sobre valores usando a sintaxe de chaves.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Dicionários em Python são desordenados."
> **Por que está errado:** Desde o Python 3.7+, os dicionários preservam a ordem de inserção por padrão.
> **Correto:** Dicionários preservam a ordem de inserção, mas não devem ser usados para ordenação lógica (use `sorted()` ou `collections.OrderedDict` se precisar de funcionalidades explícitas).

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **`collections.defaultdict`:** Evita a necessidade de verificar se uma chave existe antes de incrementar um valor. Essencial para contadores de dados.
> **`collections.Counter`:** Especializado em contar ocorrências de elementos.

## 📖 Fonte
Fonte: [Python Docs - Data Structures](https://docs.python.org/3/tutorial/datastructures.html) (Versão 3.12)

---
← [[Python/03-Controle-Fluxo/01-Aula]] · [[MOC-Python]] · [[Python/05-Funcoes-TypeHints/01-Aula]] →
