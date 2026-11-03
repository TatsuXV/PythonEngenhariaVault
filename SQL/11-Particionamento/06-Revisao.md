---
tipo: revisao
trilha: SQL
capitulo: 11
titulo: "Revisão: Particionamento"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Particionamento

## 📌 Pontos Chave
- **Escalabilidade:** O particionamento evita a degradação de performance em tabelas de escala de Terabytes.
- **Gestão de Ciclo de Vida:** Facilitar o arquivamento de dados históricos através de `DROP PARTITION`.
- **Sintonia do Otimizador:** A eficácia do particionamento depende inteiramente do **Partition Pruning**. Se a query não filtrar pela chave de partição, o banco fará a varredura em todas as partições.
- **Custo de Modelagem:** Exige a alteração da Primary Key para incluir a coluna de partição.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre Range, List e Hash partitioning.
- [ ] Consigo implementar uma tabela particionada por data.
- [ ] Entendo por que o `DELETE` é lento e o `DROP PARTITION` é rápido.
- [ ] Sei identificar se uma query está utilizando o Partition Pruning via `EXPLAIN`.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[12-Modelagem-Normalizacao]] →
