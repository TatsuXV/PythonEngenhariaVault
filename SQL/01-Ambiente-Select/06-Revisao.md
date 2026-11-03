---
tipo: revisao
trilha: SQL
capitulo: 01
titulo: "Revisão: Ambiente e SELECT"
nivel: 1
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Ambiente e SELECT

## 📌 Pontos Chave
- **Ordem de Execução:** `FROM` $\rightarrow$ `WHERE` $\rightarrow$ `SELECT`. Nunca tente usar alias do SELECT no WHERE.
- **MySQL vs Postgres:** MySQL é mais flexível com aspas, mas o padrão ANSI (aspas simples) é o caminho para a portabilidade.
- **Case Sensitivity:** Cuidado com nomes de tabelas em Linux (case-sensitive) vs Windows (insensitive).

## 🛠 Checklist de Domínio
- [ ] Consigo instalar e conectar no MySQL 8.x.
- [ ] Sei a diferença entre `DISTINCT` e `SELECT *`.
- [ ] Consigo filtrar dados usando `BETWEEN`, `IN` e `LIKE`.
- [ ] Entendo por que meu código dá erro ao tentar usar alias no `WHERE`.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[02-DDL-DML-Filtros-Agregacoes]] →
