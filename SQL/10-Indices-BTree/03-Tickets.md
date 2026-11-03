---
tipo: ticket
trilha: SQL
capitulo: 10
titulo: "Otimização de Ingestão vs Busca"
nivel: 4
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, indexing, performance, etl]
---
# Ticket: SQL-10-01 - Otimização de Ingestão vs Busca

> [!todo] ID: SQL-10-01 | Prioridade: Alta | Tipo: Performance | Tempo: 3h
> **Contexto (Sprints/Jira):** O Job de carga diária de logs está levando 4 horas para terminar. Foi descoberto que a tabela de destino possui 12 índices diferentes. O time de infra sugere que a escrita está lenta devido à atualização constante das B-Trees.
> **Entrada (Raw Data):** Tabela `fact_logs` com múltiplos índices.
> **Saída Esperada (Target):** Reduzir o tempo de carga em 50% mantendo a performance das queries de busca mais comuns.

## ✅ Critério de Aceite
- [ ] Analisar a lista de índices atuais (`SHOW INDEX FROM fact_logs`).
- [ ] Identificar índices redundantes (ex: um índice em `(A, B)` e outro apenas em `(A)`).
- [ ] Propor a remoção de índices de baixa cardinalidade.
- [ ] Implementar a estratégia de: **Drop Indexes $\rightarrow$ Bulk Load $\rightarrow$ Recreate Indexes** (se aplicável ao volume de dados).

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Lembre-se que índices compostos cobrem buscas pelas colunas à esquerda. Se você tem um índice em `(cliente_id, data)`, você não precisa de um índice separado apenas em `cliente_id`.
> 
> [!tip] Nível 2 (Direta)
> Use o `EXPLAIN` para ver quais índices realmente são usados pelas queries de produção e delete os "índices fantasmas".

## 🧪 Como Verificar (Teste de Aceitação)
Compare o tempo de execução de um `INSERT` de 10k linhas com e sem os índices redundantes.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de Over-Indexing).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
