---
tipo: ticket
trilha: SQL
capitulo: 06
titulo: "Automação de Fechamento de Lote"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, procedures, automation, pipeline]
---
# Ticket: SQL-06-01 - Automação de Fechamento de Lote

> [!todo] ID: SQL-06-01 | Prioridade: Alta | Tipo: Automatização | Tempo: 3h
> **Contexto (Sprints/Jira):** O processo de fechamento mensal de vendas é manual e propenso a erros. O time de DE precisa de uma Procedure que automatize as seguintes etapas: 
> 1. Mover as vendas do mês atual para uma tabela de histórico (`sales_history`).
> 2. Limpar a tabela de vendas atual para o novo mês.
> 3. Registrar a data e hora do fechamento em uma tabela de log.
> **Entrada (Raw Data):** Tabelas `sales` e `sales_history`.
> **Saída Esperada (Target):** Dados migrados e log de execução registrado.

## ✅ Critério de Aceite
- [ ] A procedure deve encapsular todas as três etapas em um único bloco.
- [ ] Uso de `INSERT INTO ... SELECT` para a migração.
- [ ] Uso de `TRUNCATE` para a limpeza da tabela original.
- [ ] Inclusão de um parâmetro `OUT` para retornar o número de linhas migradas.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se de usar o `DELIMITER` para criar a procedure.
> 
> [!tip] Nível 2 (Direta)
> Use a função `ROW_COUNT()` do MySQL para capturar a quantidade de linhas afetadas pelo último comando e atribuí-la ao parâmetro `OUT`.

## 🧪 Como Verificar (Teste de Aceitação)
Execute `CALL sp_monthly_closing(@rows_migrated); SELECT @rows_migrated;`. Verifique se a tabela de vendas ficou vazia e a de histórico foi populada.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Lógica de Controle).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
