---
tipo: ticket
trilha: SQL
capitulo: 02
titulo: "Consolidação de Vendas Mensais"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, agregacoes, business]
---
# Ticket: SQL-02-01 - Consolidação de Vendas Mensais

> [!todo] ID: SQL-02-01 | Prioridade: Média | Tipo: Transformação | Tempo: 2h
> **Contexto (Sprints/Jira):** O time de Finanças precisa de um relatório simplificado que mostre o valor total vendido por produto, mas apenas para produtos que somaram mais de 200.00 em vendas totais.
> **Entrada (Raw Data):** Tabela `lab_sales`.
> **Saída Esperada (Target):** Colunas `product_id` e `total_sales`.

## ✅ Critério de Aceite
- [ ] Usar `SUM()` para calcular o total.
- [ ] Agrupar por `product_id`.
- [ ] Filtrar o resultado da soma usando a cláusula `HAVING`.
- [ ] Não usar `WHERE` para filtrar a soma (pois o WHERE filtra linhas, não grupos).

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se da ordem de execução: `WHERE` $\rightarrow$ `GROUP BY` $\rightarrow$ `HAVING`.
> 
> [!tip] Nível 2 (Direta)
> O `HAVING` é como o `WHERE` do `GROUP BY`.

## 🧪 Como Verificar (Teste de Aceitação)
Execute a query e verifique se apenas o `product_id` que superou 200.00 aparece no resultado.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Ordem de Execução).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
