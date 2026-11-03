---
tipo: revisao
trilha: SQL
capitulo: 05
titulo: "Revisão: CTEs, Views e Tabelas Temporárias"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: CTEs, Views e Tabelas Temporárias

## 📌 Pontos Chave
- **CTEs (`WITH`):** Transformam subqueries aninhadas em blocos nomeados e sequenciais. Melhoram a legibilidade drasticamente.
- **Views:** São "atalhos" para queries complexas. Úteis para abstração e segurança, mas não melhoram a performance da query original.
- **Temp Tables:** Armazenamento físico temporário por sessão. Ideal para pipelines de ETL onde o mesmo dado é consumido por múltiplos passos.
- **MySQL vs Postgres:** A ausência de `MATERIALIZED VIEW` no MySQL exige que o DE crie tabelas de snapshot manualmente.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre CTE, View e Temporary Table.
- [ ] Consigo refatorar subqueries aninhadas para o padrão `WITH`.
- [ ] Sei criar e consultar uma View simples.
- [ ] Entendo o ciclo de vida de uma `TEMPORARY TABLE` (escopo de sessão).

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[06-Procedures]] →
