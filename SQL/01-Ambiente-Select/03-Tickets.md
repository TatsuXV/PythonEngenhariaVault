---
tipo: ticket
trilha: SQL
capitulo: 01
titulo: "Extração de Leads para Marketing"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, select, business]
---
# Ticket: SQL-01-01 - Extração de Leads para Marketing

> [!todo] ID: SQL-01-01 | Prioridade: Alta | Tipo: Extração | Tempo: 1h
> **Contexto (Sprints/Jira):** O time de Marketing precisa de uma lista de emails de todos os clientes residentes na cidade de 'São Paulo' para uma campanha regional.
> **Entrada (Raw Data):** Tabela `lab_customers`.
> **Saída Esperada (Target):** Uma lista contendo apenas a coluna `email`.

## ✅ Critério de Aceite
- [ ] Retornar apenas a coluna `email`.
- [ ] Filtrar estritamente por `city = 'São Paulo'`.
- [ ] A query deve ser performática (não usar `SELECT *`).

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se de que strings em SQL são delimitadas por aspas simples.
> 
> [!tip] Nível 2 (Direta)
> Use a cláusula `WHERE` para filtrar a cidade.

## 🧪 Como Verificar (Teste de Aceitação)
O resultado deve retornar apenas os emails da Alice e da Diana.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]]

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
