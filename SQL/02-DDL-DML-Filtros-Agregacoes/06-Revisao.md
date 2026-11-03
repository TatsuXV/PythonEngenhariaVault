---
tipo: revisao
trilha: SQL
capitulo: 02
titulo: "Revisão: DDL, DML e Agregações"
nivel: 2
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: DDL, DML e Agregações

## 📌 Pontos Chave
- **DDL vs DML:** DDL define a "caixa" (tabela), DML define o "conteúdo" (dados).
- **Agregações:** Sempre que houver um `SUM`, `COUNT` ou `AVG` junto com outras colunas no `SELECT`, use `GROUP BY`.
- **Filtro de Grupo:** Use `HAVING` para filtrar o resultado de uma soma ou média.
- **Portabilidade:** No MySQL, use `AUTO_INCREMENT` para chaves primárias numéricas.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre `TRUNCATE` e `DELETE`.
- [ ] Consigo criar tabelas com `PRIMARY KEY` e `FOREIGN KEY`.
- [ ] Consigo fazer um `UPDATE` seguro usando a cláusula `WHERE`.
- [ ] Domino a diferença entre `WHERE` (filtra linha) e `HAVING` (filtra grupo).

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[03-Join-Having]] →
