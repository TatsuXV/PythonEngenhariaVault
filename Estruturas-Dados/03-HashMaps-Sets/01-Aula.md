---
tipo: aula
trilha: estruturas-dados
capitulo: 03
titulo: "Hash Maps & Sets: O Poder do O(1)"
nivel: 3
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-27
tags: [hash-maps, sets, leetcode, o1-lookup, performance]
---
# Hash Maps & Sets: O Poder do O(1)

> [!abstract] Capítulo 03 · Hash Maps & Sets
> ⏱ 6h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/01-Big-O/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/03-HashMaps-Sets/07-Entrega-Projeto|Otimizador de Deduplicação de Dados]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Por que buscar um elemento em um `set` é mais rápido do que buscar em uma `list`?
> ?
> [!question] O que é uma "Colisão de Hash" e como as linguagens modernas lidam com isso?
> ?
> [!question] Em qual cenário o uso de um Hash Map aumenta a complexidade de espaço (Space Complexity) para ganhar tempo (Time Complexity)?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar o uso de Dicionários (`dict`) e Conjuntos (`set`) para transformar algoritmos lentos ($O(n^2)$) em algoritmos ultra rápidos ($O(n)$). Aprender a implementar "Frequency Counters" e a resolver problemas de busca instantânea, simulando a criação de índices de memória para pipelines de dados.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, o Hash Map é a base de quase tudo. Quando você faz um `JOIN` em SQL ou um `merge` no Pandas, o motor por baixo utiliza tabelas de Hash para encontrar correspondências rapidamente. Se você tentar fazer um "join" manual usando loops aninhados em Python, seu pipeline travará. Saber usar `sets` para remover duplicatas de bilhões de IDs é a diferença entre um processo de 10 segundos e um de 10 horas.

## 📚 Teoria

### 1. Como funciona o Hash Map (Dicionário)
Um Hash Map transforma uma chave (ex: "cliente_123") em um índice numérico através de uma **função de hash**. Isso permite que o computador vá direto ao endereço de memória onde o valor está guardado.
- **Busca, Inserção e Deleção:** Média de $O(1)$.

### 2. Sets (Conjuntos)
Um `set` é, essencialmente, um Hash Map que armazena apenas as chaves, sem valores.
- **Principal uso:** Garantir a unicidade dos elementos e operações de conjuntos (Interseção, União, Diferença).
- **Complexidade de busca (`in`):** $O(1)$.

### 3. Pattern: Frequency Counter (Contador de Frequência)
Um dos padrões mais comuns no LeetCode. Consiste em usar um dicionário para contar a ocorrência de cada elemento.

```python
# Exemplo: Contar frequência de palavras em um log
text = "erro aviso erro critico erro aviso"
counter = {}
for word in text.split():
    counter[word] = counter.get(word, 0) + 1
# Resultado: {'erro': 3, 'aviso': 2, 'critico': 1}
```

### 4. Trade-off: Time vs Space
Para obter a velocidade de $O(1)$, o Hash Map consome mais memória RAM do que um array simples, pois precisa de espaço extra para evitar colisões. Em Big Data, devemos monitorar se o nosso dicionário de "mapeamento" não está consumindo toda a memória do servidor.

## ⚠️ Armadilhas e Erros Comuns (Foco LeetCode)
- **Usar Listas para Busca:** Usar `if x in my_list` dentro de um loop $\rightarrow$ Resultado: $O(n^2)$. **Sempre converta para `set` primeiro.**
- **Chaves Mutáveis:** Tentar usar uma `list` como chave de um dicionário $\rightarrow$ Erro: `TypeError: unhashable type`. Chaves devem ser imutáveis (strings, ints, tuples).
- **Ignorar o `get()`:** Tentar acessar `dict[key]` sem verificar se a chave existe $\rightarrow$ Erro: `KeyError`. Use `.get(key, default)`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Sets são sempre a melhor forma de remover duplicatas."
> **Por que está errado:** Se a ordem dos elementos for importante, o `set` a destruirá.
> **Correto:** Se a ordem for necessária, use `dict.fromkeys(lista).keys()` ou `OrderedDict` para manter a sequência original enquanto remove duplicados.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Dica de Entrevista:** Quando o problema envolver "encontrar o primeiro elemento que se repete", "verificar se há anagramas" ou "mapear relações 1:1", a resposta quase sempre envolve um Hash Map.

## 📖 Fonte
Fonte: [NeetCode - Hash Maps](https://neetcode.io/courses/algorithm-basics/hash-maps) e [Python Official Docs - Mapping Types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)

---
← [[Estruturas-Dados/02-Arrays-TwoPointers/01-Aula]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/03-HashMaps-Sets/02-Lab]] →
