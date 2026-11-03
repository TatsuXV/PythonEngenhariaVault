---
tipo: ticket
trilha: SQL
capitulo: 09
titulo: "Otimização de Query de Relatório Mensal"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, explain, performance, optimization]
---
# Ticket: SQL-09-01 - Otimização de Query de Relatório Mensal

> [!todo] ID: SQL-09-01 | Prioridade: Alta | Tipo: Performance | Tempo: 3h
> **Contexto (Sprints/Jira):** O relatório de faturamento mensal está levando mais de 30 segundos para rodar em produção. O time de infra reportou que a CPU do banco de dados dispara para 100% durante a execução. A query atual usa filtros de data com funções.
> **Entrada (Raw Data):** Tabela `fact_sales`.
> **Saída Esperada (Target):** Reduzir o tempo de execução para menos de 1 segundo utilizando a técnica de SARGability.

## ✅ Critério de Aceite
- [ ] Utilizar o `EXPLAIN` para provar que a query original estava fazendo um `Full Table Scan` (`type: ALL`).
- [ ] Refatorar a cláusula `WHERE` para remover funções da coluna de data (SARGable).
- [ ] Utilizar o `EXPLAIN` novamente para provar que a query agora utiliza um índice (`type: range` ou `ref`).
- [ ] A coluna `Extra` não deve conter `Using filesort` para a ordenação final.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Evite `WHERE MONTH(data) = 5`. O MySQL não consegue usar índices em colunas transformadas por funções.
> 
> [!tip] Nível 2 (Direta)
> Use intervalos: `WHERE data >= '2023-05-01' AND data <= '2023-05-31'`.

## 🧪 Como Verificar (Teste de Aceitação)
Compare a coluna `type` e `rows` do `EXPLAIN` antes e depois da alteração. O número de `rows` deve cair drasticamente.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de SARGability).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
