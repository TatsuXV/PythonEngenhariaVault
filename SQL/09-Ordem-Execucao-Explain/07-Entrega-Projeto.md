---
tipo: projeto
trilha: SQL
capitulo: 09
titulo: "Projeto: Auditoria de Performance de Relatórios"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, performance, explain]
---
# Projeto: Auditoria de Performance de Relatórios

## 🚩 Cenário
A Aurora Tech possui um relatório de "Vendas por Vendedor e Produto" que está causando gargalos no servidor de produção. O relatório filtra por um período de datas, agrupa por vendedor e ordena pelo faturamento total. Atualmente, o banco está fazendo Full Table Scans em todas as execuções.

## 🎯 Requisitos da Entrega
Você deve entregar um relatório técnico de otimização contendo:

1. **Análise do Estado Atual:**
    - Escrever a query original (com filtros não SARGáveis).
    - Fornecer o print/texto do `EXPLAIN` original, destacando o `type: ALL` e o `Using filesort`.

2. **Plano de Otimização:**
    - Refatorar a query para ser SARGable.
    - Propor a criação de um índice composto estratégico (coluna de filtro + coluna de ordenação).

3. **Validação do Resultado:**
    - Fornecer o `EXPLAIN` da query otimizada.
    - Comparar a coluna `rows` (estimativa de linhas lidas) entre a query original e a otimizada.

## ✅ Critérios de Aceite
- [ ] Prova documental do `type: ALL` $\rightarrow$ `type: range/ref`.
- [ ] Eliminação do `Using filesort` através de índice composto.
- [ ] Redução drástica na estimativa de `rows` lidas.
- [ ] Justificativa técnica do porquê a mudança funcionou baseada na ordem de execução do SQL.

## 🧪 Como Validar
1. Use a tabela `lab_big_orders` do Lab 09.
2. Execute a versão lenta $\rightarrow$ `EXPLAIN`.
3. Aplique o índice $\rightarrow$ `EXPLAIN`.
4. Compare os tempos de execução reais com `EXPLAIN ANALYZE`.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[10-Indices-BTree]] →
