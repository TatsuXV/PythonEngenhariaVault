---
tipo: revisao
trilha: SQL
capitulo: 04
titulo: "Revisão: Window Functions"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Window Functions

## 📌 Pontos Chave
- **Granularidade:** Window functions permitem calcular agregados sem perder a linha original (ao contrário do GROUP BY).
- **Séries Temporais:** `LAG` e `LEAD` são indispensáveis para análise de tendências.
- **Soma Acumulada:** `SUM(valor) OVER (ORDER BY data)` é o padrão para criar gráficos de crescimento.
- **Performance:** Window Functions exigem ordenação. Sempre use índices nas colunas de `PARTITION BY` e `ORDER BY`.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre `RANK`, `DENSE_RANK` e `ROW_NUMBER`.
- [ ] Consigo criar uma soma acumulada por categoria usando `OVER`.
- [ ] Sei calcular a diferença de valor entre a linha atual e a anterior usando `LAG`.
- [ ] Entendo a diferença entre `PARTITION BY` e `GROUP BY`.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[05-CTE-Views-Tabelas]] →
