---
tipo: revisao
trilha: SQL
capitulo: 08
titulo: "Revisão: Transações e Isolamento"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Transações e Isolamento

## 📌 Pontos Chave
- **ACID:** A base de qualquer banco confiável. Sem atomicidade e isolamento, a integridade dos dados é impossível em sistemas concorrentes.
- **Controle de Fluxo:** O uso consciente de `START TRANSACTION`, `COMMIT`, `ROLLBACK` e `SAVEPOINT` permite criar fluxos de carga seguros.
- **Níveis de Isolamento:** O MySQL usa `REPEATABLE READ` por padrão, o que é mais seguro que o `READ COMMITTED` do Postgres, mas exige mais atenção a Deadlocks.
- **Locks:** Entender que a escrita bloqueia a escrita (Exclusive Lock), mas leituras geralmente não bloqueiam leituras (MVCC).

## 🛠 Checklist de Domínio
- [ ] Consigo explicar as 4 propriedades do ACID.
- [ ] Sei a diferença entre `COMMIT` e `ROLLBACK`.
- [ ] Consigo implementar um `SAVEPOINT` para cancelamentos parciais.
- [ ] Sei por que não usar `TRUNCATE` dentro de transações críticas.
- [ ] Entendo como o nível de isolamento afeta a visibilidade dos dados.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[09-Ordem-Execucao-Explain]] →
