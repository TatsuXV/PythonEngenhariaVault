---
tipo: ticket
trilha: SQL
capitulo: 05
titulo: "Refatoração de Query de Faturamento"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, cte, refactoring, business]
---
# Ticket: SQL-05-01 - Refatoração de Query de Faturamento

> [!todo] ID: SQL-05-01 | Prioridade: Média | Tipo: Manutenção | Tempo: 2h
> **Contexto (Sprints/Jira):** Existe uma query legada que utiliza três subqueries aninhadas para calcular o faturamento por região. O código está impossível de manter e qualquer alteração causa bugs. O time de DE solicitou a refatoração para o padrão de CTEs.
> **Entrada (Raw Data):** Tabelas de `vendas`, `clientes` e `regioes`.
> **Saída Esperada (Target):** Colunas `regiao_nome` e `total_faturamento`.

## ✅ Critério de Aceite
- [ ] Eliminar todas as subqueries aninhadas.
- [ ] Utilizar pelo menos duas CTEs sequenciais (ex: `vendas_limpas` $\rightarrow$ `faturamento_regiao`).
- [ ] A query final deve ser um simples `SELECT` a partir da última CTE.
- [ ] O resultado final deve ser idêntico ao da query legada.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Pense na query como um pipeline: Step 1 (Limpeza) $\rightarrow$ Step 2 (Agregação) $\rightarrow$ Step 3 (Apresentação).
> 
> [!tip] Nível 2 (Direta)
> Use a sintaxe: `WITH cte1 AS (...), cte2 AS (...) SELECT ...`

## 🧪 Como Verificar (Teste de Aceitação)
Execute a query refatorada e compare os valores com a query original. Os totais por região devem ser idênticos.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de CTEs).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
