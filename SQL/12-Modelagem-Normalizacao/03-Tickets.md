---
tipo: ticket
trilha: SQL
capitulo: 12
titulo: "Migração de Legado para Modelo Dimensional"
nivel: 5
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, modeling, star-schema, etl]
---
# Ticket: SQL-12-01 - Migração de Leggado para Modelo Dimensional

> [!todo] ID: SQL-12-01 | Prioridade: Alta | Tipo: Arquitetura | Tempo: 4h
> **Contexto (Sprints/Jira):** O sistema de faturamento antigo salva tudo em uma única tabela "flat" (`billing_flat`). Isso torna as queries de BI extremamente lentas e a manutenção de dados impossível. O time de Data Engineering precisa migrar essa estrutura para um **Star Schema** para alimentar o novo Dashboard de BI.
> **Entrada (Raw Data):** Tabela `billing_flat` (contendo dados de cliente, produto, data e valor).
> **Saída Esperada (Target):** Três tabelas: `dim_customer`, `dim_product` e `fact_billing`.

## ✅ Critério de Aceite
- [ ] Implementar a desduplicação de clientes e produtos durante a migração (1NF $\rightarrow$ 3NF).
- [ ] Criar as tabelas de dimensão com chaves substitutas (Surrogate Keys) via `AUTO_INCREMENT`.
- [ ] Popular a tabela de fato relacionando as chaves das dimensões.
- [ ] Provar que a query final de faturamento por categoria agora usa apenas 2 Joins simples em vez de varrer a tabela flat.

## 💡 Dicas
> [!tip] Nível 1 (Sutil)
> Use a técnica de `INSERT INTO ... SELECT DISTINCT` para criar as dimensões primeiro.
> 
> [!tip] Nível 2 (Direta)
> Para popular a tabela de fato, faça Joins entre a tabela flat e as novas dimensões para recuperar os IDs gerados.

## 🧪 Como Verificar (Teste de Aceitação)
Compare o `EXPLAIN` de uma query de soma total na tabela flat vs a query no Star Schema. Verifique a redução no volume de dados lidos.

## 🆘 Travei!
Se travar 2 vezes, revise: [[01-Aula#📚 Teoria]] (Seção de Modelagem Dimensional).

---
← [[02-Lab]] · [[MOC-SQL]] · [[04-Gabarito]] →
