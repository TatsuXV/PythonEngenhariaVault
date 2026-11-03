---
tipo: revisao
trilha: SQL
capitulo: 03
titulo: "Revisão: Joins e Having"
nivel: 3
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Joins e Having

## 📌 Pontos Chave
- **Tabelas de Dimensão vs Fato:** Joins são a ponte entre quem é o cliente (Dimensão) e o que ele comprou (Fato).
- **NULLs:** O `LEFT JOIN` é a principal ferramenta para encontrar dados faltantes ou orfãos.
- **Performance:** Sempre garanta que as colunas usadas no `ON` do Join possuam índices (B-Tree).
- **Having:** Sempre use `HAVING` para filtrar resultados de `SUM`, `COUNT` ou `AVG`.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre INNER, LEFT, RIGHT e CROSS JOIN.
- [ ] Consigo identificar e corrigir um "INNER JOIN acidental" causado por filtro no WHERE.
- [ ] Sei simular um FULL OUTER JOIN usando UNION no MySQL.
- [ ] Consigo escrever queries que relacionem 3 ou mais tabelas.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[04-Window-Functions]] →
