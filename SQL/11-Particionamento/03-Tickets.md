---
tipo: ticket
trilha: SQL
capitulo: 11
titulo: "Otimização de Arquivamento de Dados"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, partitioning, big-data, lifecycle]
---
# Ticket: SQL-11-01 - Otimização de Arquivamento de Dados

> [!todo] ID: SQL-11-01 | Prioridade: Alta | Tipo: Manutenção | Tempo: 3h
> **Contexto (Sprints/Jira):** A tabela de `event_logs` cresceu para 2TB. O processo de deleção de dados com mais de 2 anos (`DELETE FROM event_logs WHERE event_date < '2022-01-01'`) está causando travamentos no banco de dados e gerando logs de transação gigantescos (Undo Log).
> **Entrada (Raw Data):** Tabela `event_logs` não particionada.
> **Saída Esperada (Target):** Migrar a tabela para um modelo particionado por ano e remover os dados antigos de forma instantânea.

## ✅ Critério de Aceite
- [ ] Propor a estratégia de particionamento ideal (Range por Ano).
- [ ] Implementar a migração da tabela original para a nova tabela particionada.
- [ ] Demonstrar o uso do comando `DROP PARTITION` para remover os dados de 2021 e anteriores.
- [ ] Provar via `EXPLAIN` que as novas queries de busca por data utilizam o **Partition Pruning**.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se de que você não pode transformar uma tabela comum em particionada "no lugar". Você deve criar a nova tabela particionada e mover os dados (`INSERT INTO ... SELECT`).
> 
> [!tip] Nível 2 (Direta)
> Para evitar o erro de Primary Key, a coluna de data deve ser incluída na PK da nova tabela: `PRIMARY KEY (id, event_date)`.

## 🧪 Como Verificar (Teste de Aceitação)
1. Meça o tempo de um `DELETE` de 1 milhão de linhas.
2. Meça o tempo de um `DROP PARTITION` de 1 milhão de linhas.
3. Compare a diferença de performance.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de Manutenção de Dados).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
