---
tipo: ticket
trilha: SQL
capitulo: 03
titulo: "Análise de Churn de Clientes"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, joins, business, churn]
---
# Ticket: SQL-03-01 - Análise de Churn de Clientes

> [!todo] ID: SQL-03-01 | Prioridade: Alta | Tipo: Auditoria | Tempo: 2h
> **Contexto (Sprints/Jira):** O time de Growth precisa identificar a lista de clientes que estão na base, mas que nunca realizaram um único pedido. Esses clientes são considerados "Churn" (estão inativos).
> **Entrada (Raw Data):** Tabelas `lab_customers_j` e `lab_orders_j`.
> **Saída Esperada (Target):** Colunas `customer_name` e `city`.

## ✅ Critério de Aceite
- [ ] Retornar apenas clientes que **NÃO** possuem correspondência na tabela de pedidos.
- [ ] Utilizar obrigatoriamente um `LEFT JOIN`.
- [ ] Filtrar os resultados onde a chave da tabela de pedidos seja `NULL`.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Pense: "Quero todos da esquerda, mas apenas aqueles que não encontraram ninguém na direita".
> 
> [!tip] Nível 2 (Direta)
> Use `LEFT JOIN` e no `WHERE` coloque `orders.order_id IS NULL`.

## 🧪 Como Verificar (Teste de Aceitação)
O resultado deve retornar apenas Daniel Oliveira e Eduarda Lima.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de LEFT JOIN).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
