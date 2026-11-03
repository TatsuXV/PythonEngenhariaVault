---
tipo: ticket
trilha: SQL
capitulo: 07
titulo: "Implementação de Auditoria de Segurança"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, triggers, audit, security]
---
# Ticket: SQL-07-01 - Implementação de Auditoria de Segurança

> [!todo] ID: SQL-07-01 | Prioridade: Crítica | Tipo: Segurança | Tempo: 3h
> **Contexto (Sprints/Jira):** O time de Compliance detectou que alterações em salários de funcionários estão ocorrendo sem rastreabilidade. Precisamos de um sistema automático que registre qualquer alteração na coluna `salary` da tabela `employees`.
> **Entrada (Raw Data):** Tabelas `employees` e `salary_audit_log`.
> **Saída Esperada (Target):** Registro automático de (employee_id, old_salary, new_salary, changed_by, changed_at).

## ✅ Critério de Aceite
- [ ] O trigger deve disparar apenas se o valor do salário for REALMENTE alterado (`OLD.salary <> NEW.salary`).
- [ ] O trigger deve ser do tipo `AFTER UPDATE`.
- [ ] O campo `changed_by` deve capturar o usuário atual do banco de dados (`USER()`).
- [ ] O registro deve ser inserido na tabela de auditoria automaticamente.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se de que para capturar o usuário do sistema no MySQL, usamos a função `USER()`.
> 
> [!tip] Nível 2 (Direta)
> Use a estrutura: `IF OLD.salary <> NEW.salary THEN ... END IF;`

## 🧪 Como Verificar (Teste de Aceitação)
Execute `UPDATE employees SET salary = salary + 100 WHERE emp_id = 101;`. Verifique se a tabela `salary_audit_log` recebeu a linha correspondente com os valores corretos.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de OLD e NEW).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
