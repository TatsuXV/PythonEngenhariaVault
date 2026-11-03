---
tipo: revisao
trilha: estruturas-dados
capitulo: 05
titulo: "Revisão: Árvores & Índices"
---
# 🔄 Revisão: Árvores & Índices

## 📌 Conceitos Chave
- **BST (Binary Search Tree):** Esquerda < Raiz < Direita.
- **Busca Binária:** Divide o espaço de busca ao meio a cada passo.
- **Recursão:** Ferramenta principal para navegar em árvores.
- **Balanceamento:** Essencial para evitar que a árvore vire uma lista.

## 🚀 Padrões de Implementação
1. **Busca Binária:** Use `low`, `high` e `mid` para buscar em arrays ordenados.
2. **Travessia In-Order:** Visita a BST em ordem crescente.
3. **Travessia Post-Order:** Calcula agregações de baixo para cima (folhas $\rightarrow$ raiz).
4. **Índices de Banco de Dados:** B-Trees para acesso rápido a disco.

## ⚠️ Check-list de Erros (LeetCode)
- [ ] Estou tentando fazer busca binária em array desordenado? (Ordene primeiro).
- [ ] Verifiquei a condição de parada da recursão? (Evite `RecursionError`).
- [ ] A árvore está balanceada? (Se for problema de performance, considere AVL ou Red-Black).

## 🔗 Conexão DE
Em Engenharia de Dados, esses padrões são usados em:
- **Índices de Tabelas (SQL):** O índice de uma tabela no Postgres/MySQL é, no fundo, uma B-Tree.
- **Sistemas de Arquivos (Parquet/Avro):** Metadados de arquivos costumam ser armazenados em estruturas de árvore para filtrar colunas e partições rapidamente.
- **Partition Pruning:** Otimizador de query usa a estrutura de partições (árvore) para ignorar pastas inteiras de dados.
