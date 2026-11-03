---
tipo: ticket
trilha: SQL
capitulo: 04
titulo: "Análise de Growth e Performance de Vendedores"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, window-functions, business, growth]
---
# Ticket: SQL-04-01 - Análise de Growth e Performance de Vendedores

> [!todo] ID: SQL-04-01 | Prioridade: Alta | Tipo: Analytics | Tempo: 3h
> **Contexto (Sprints/Jira):** O time de Operações quer identificar a volatilidade das vendas. Eles precisam de um relatório que mostre a venda do dia e a diferença (em valor) para a venda do dia anterior de cada vendedor.
> **Entrada (Raw Data):** Tabela `lab_sales_wf`.
> **Saída Esperada (Target):** Colunas `seller_id`, `sale_date`, `amount`, `diff_previous_day`.

## ✅ Critério de Aceite
- [ ] Usar a função `LAG()` para acessar o valor anterior.
- [ ] Calcular a diferença: `amount - LAG(amount)`.
- [ ] Garantir que o cálculo seja reiniciado a cada vendedor (`PARTITION BY`).
- [ ] Ordenar os resultados por vendedor e data.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> O primeiro registro de cada vendedor terá o valor da venda anterior como `NULL`. Isso é normal.
> 
> [!tip] Nível 2 (Direta)
> Use: `amount - LAG(amount) OVER (PARTITION BY seller_id ORDER BY sale_date)`.

## 🧪 Como Verificar (Teste de Aceitação)
O resultado deve mostrar que para o vendedor 1, a segunda linha tem uma diferença de +50.00 (150 - 100).

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de Value Functions - LAG).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
