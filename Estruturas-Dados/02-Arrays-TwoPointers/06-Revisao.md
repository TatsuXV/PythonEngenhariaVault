---
tipo: revisao
trilha: estruturas-dados
capitulo: 02
titulo: "Revisão: Arrays & Two Pointers"
---
# 🔄 Revisão: Arrays & Two Pointers

## 📌 Conceitos Chave
- **Arrays:** Acesso $O(1)$ por índice, mas inserção/remoção no meio é $O(n)$.
- **Two Pointers:** Técnica de otimização para reduzir loops aninhados ($O(n^2) \rightarrow O(n)$).
- **Sliding Window:** Otimização para problemas de sub-arrays contíguos.

## 🚀 Padrões de Implementação
1. **Opostos $\rightarrow$ Centro:** Usado em arrays ordenados para busca de pares (ex: Two Sum Ordenado).
2. **Lento $\rightarrow$ Rápido:** Usado para remoção de duplicatas in-place ou detecção de ciclos.
3. **Janela Fixa:** Soma/Média de $K$ elementos.
4. **Janela Dinâmica:** Menor sub-array com soma $\ge X$.

## ⚠️ Check-list de Erros (LeetCode)
- [ ] O array está ordenado? (Se não, Two Pointers Opostos não funciona).
- [ ] Estou criando um novo array? (Tente fazer in-place para $O(1)$ de espaço).
- [ ] Estou usando `sum()` dentro do loop? (Troque por soma incremental para evitar $O(n \cdot K)$).

## 🔗 Conexão DE
Em Engenharia de Dados, esses padrões são usados em:
- **Desduplicação de Streams:** Remover registros repetidos adjacentes em arquivos ordenados por timestamp.
- **Cálculo de Médias Móveis (Moving Average):** Monitorar a latência de APIs em janelas de tempo.
