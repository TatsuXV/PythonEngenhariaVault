---
tipo: projeto
trilha: SQL
capitulo: 04
titulo: "Projeto: Dashboard de Performance de Vendas"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, analytics]
---
# Projeto: Dashboard de Performance de Vendas

## 🚩 Cenário
A empresa Aurora Tech precisa de um relatório analítico avançado para a reunião de diretoria. Eles não querem apenas o total de vendas, mas sim entender a **dinâmica** de crescimento de cada vendedor.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL único que gere uma tabela final com as seguintes colunas:

1. **Identificação:** `seller_id` e `sale_date`.
2. **Valor:** `amount` (valor da venda atual).
3. **Soma Acumulada:** O total vendido por aquele vendedor desde a primeira venda até a data atual (`Running Total`).
4. **Ranking:** A posição daquela venda no ranking geral de valores do vendedor (`DENSE_RANK`).
5. **Comparativo Temporal:** A diferença de valor entre a venda atual e a venda anterior do mesmo vendedor (`Growth`).

## ✅ Critérios de Aceite
- [ ] Uso correto de `SUM() OVER (PARTITION BY ... ORDER BY ...)`.
- [ ] Uso de `DENSE_RANK()` para o ranking de valores.
- [ ] Implementação de `LAG()` para o cálculo de growth.
- [ ] A query deve ser única (pode usar uma CTE ou Subquery para organizar o resultado final).

## 🧪 Como Validar
Execute o script no MySQL 8.x e valide se para o vendedor com mais vendas, a coluna de "Soma Acumulada" cresce linearmente a cada linha.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[05-CTE-Views-Tabelas]] →
