---
tipo: revisao
trilha: SQL
capitulo: 09
titulo: "Revisão: Ordem de Execução e EXPLAIN"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Ordem de Execução e EXPLAIN

## 📌 Pontos Chave
- **Ordem Lógica:** O `WHERE` roda antes do `SELECT`. Por isso aliases não funcionam no filtro.
- **Técnica SARGable:** Mantenha a coluna do índice "limpa". Não use funções nela.
- **Diagnóstico via EXPLAIN:** O `type: ALL` é o sinal vermelho. O `type: ref` ou `range` é o sinal verde.
- **Índices Compostos:** São a cura para o `Using filesort` quando há filtragem e ordenação simultâneas.

## 🛠 Checklist de Domínio
- [ ] Consigo ler um plano de execução básico do MySQL.
- [ ] Sei identificar um Full Table Scan.
- [ ] Consigo refatorar uma query para torná-la SARGable.
- [ ] Entendo por que o `ORDER BY` é a penúltima coisa a ser executada.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[10-Indices-BTree]] →
