---
tipo: ticket
trilha: SQL
capitulo: 08
titulo: "Garantia de Carga Atômica (ETL)"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, transactions, etl, atomicidade]
---
# Ticket: SQL-08-01 - Garantia de Carga Atômica (ETL)

> [!todo] ID: SQL-08-01 | Prioridade: Crítica | Tipo: Data Integrity | Tempo: 3h
> **Contexto (Sprints/Jira):** Durante a carga diária de vendas, o sistema está falhando aleatoriamente no meio do processo. Isso resulta em tabelas parcialmente populadas, o que gera relatórios errados para a diretoria. O time de DE exige que a carga seja **atômica**.
> **Entrada (Raw Data):** Tabelas `stg_sales` (staging) e `fact_sales` (fato).
> **Saída Esperada (Target):** A `fact_sales` deve ser atualizada completamente ou permanecer intacta (estado anterior).

## ✅ Critério de Aceite
- [ ] Utilizar obrigatoriamente `START TRANSACTION` no início do processo.
- [ ] Implementar a lógica: `TRUNCATE fact_sales` $\rightarrow$ `INSERT INTO fact_sales SELECT * FROM stg_sales`.
- [ ] Garantir que o `COMMIT` só ocorra após o sucesso de todas as etapas.
- [ ] Simular um erro (ex: inserir um valor nulo em coluna NOT NULL) para validar que o `ROLLBACK` restaura a tabela `fact_sales`.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se que o `TRUNCATE` no MySQL causa um commit implícito (ele é DDL). Para ter rollback total, use `DELETE FROM` em vez de `TRUNCATE` dentro da transação.
> 
> [!tip] Nível 2 (Direta)
> Estrutura sugerida: `START TRANSACTION` $\rightarrow$ `DELETE FROM fact_sales` $\rightarrow$ `INSERT INTO ...` $\rightarrow$ `COMMIT`.

## 🧪 Como Verificar (Teste de Aceitação)
1. Popule `fact_sales` com 10 linhas.
2. Inicie a transação, delete as 10 linhas e tente inserir dados inválidos.
3. Execute `ROLLBACK`.
4. Verifique se as 10 linhas originais voltaram a existir.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Sessão de ACID).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
