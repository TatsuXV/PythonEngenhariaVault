---
tipo: revisao
trilha: estruturas-dados
capitulo: 04
titulo: "Revisão: Sliding Window & Stack"
---
# 🔄 Revisão: Sliding Window & Stack

## 📌 Conceitos Chave
- **Stack (Pilha):** LIFO. Útil para aninhamentos e retrocessos.
- **Sliding Window:** Técnica para evitar recalcular sub-arrays.
- **Amortização:** A ideia de que, embora algumas operações demorem, a média por elemento processado é $O(1)$.

## 🚀 Padrões de Implementação
1. **Balanceamento:** Use Stack para validar pares `()`, `[]`, `{}`.
2. **Média Móvel:** Janela fixa com soma incremental.
3. **Busca de Substring:** Janela dinâmica com dois ponteiros e mapa de posições.
4. **Monotonic Stack:** Pilha onde os elementos estão sempre em ordem crescente/decrescente (usado para achar o "próximo maior elemento").

## ⚠️ Check-list de Erros (LeetCode)
- [ ] Estou usando `sum()` ou `max()` dentro do loop da janela? (Mude para soma/máximo incremental).
- [ ] Verifiquei se a pilha está vazia antes de fazer `.pop()`? (Evite `IndexError`).
- [ ] Verifiquei se a pilha ficou vazia ao final do processamento? (Importante para validação de parênteses).

## 🔗 Conexão DE
Em Engenharia de Dados, esses padrões são usados em:
- **Processamento de Streaming:** Janelas de tempo (Tumbling Windows e Sliding Windows) no Spark Streaming ou Flink.
- **Parsers de Arquivos:** Validar a integridade de arquivos JSON/XML antes do processamento.
- **Monitoramento de Métricas:** Cálculo de médias móveis de latência e throughput em dashboards de observabilidade.
