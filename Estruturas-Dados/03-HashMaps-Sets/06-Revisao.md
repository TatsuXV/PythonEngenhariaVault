---
tipo: revisao
trilha: estruturas-dados
capitulo: 03
titulo: "Revisão: Hash Maps & Sets"
---
# 🔄 Revisão: Hash Maps & Sets

## 📌 Conceitos Chave
- **Hash Table:** Transforma uma chave em um índice de array usando uma função de hash.
- **Sets:** Implementações de Hash Tables que armazenam apenas chaves (valores únicos).
- **Dicionários:** Mapeamento Chave $\rightarrow$ Valor.

## 🚀 Padrões de Implementação
1. **Frequency Counter:** Usar `dict` ou `collections.Counter` para contar ocorrências.
2. **Lookup Table:** Substituir loops aninhados por um `dict` para transformar $O(n^2)$ em $O(n)$.
3. **Unicidade:** Usar `set()` para remover duplicatas de uma lista rapidamente.
4. **Interseção/Diferença:** Usar operadores `&` e `-` para comparar conjuntos de IDs.

## ⚠️ Check-list de Erros (LeetCode)
- [ ] Estou usando `in` em uma lista dentro de um loop? (Mude para `set`).
- [ ] Preciso de ordem? (Lembre-se que sets não preservam ordem. Se precisar, use `OrderedDict` ou mantenha uma lista auxiliar).
- [ ] A chave do meu dicionário é mutável? (Chaves de dicts devem ser **hashable** / imutáveis, como strings, ints ou tuples).

## 🔗 Conexão DE
Em Engenharia de Dados, esses padrões são usados em:
- **Deduplicação de Dataset:** Remover IDs repetidos de um arquivo CSV gigante.
- **Joins em Memória:** Implementar um *Hash Join* simples para unir dois datasets pequenos.
- **Validação de Esquema:** Verificar se todas as colunas obrigatórias (set) estão presentes no arquivo de entrada.
