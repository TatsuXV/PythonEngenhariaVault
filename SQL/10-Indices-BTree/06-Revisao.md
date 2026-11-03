---
tipo: revisao
trilha: SQL
capitulo: 10
titulo: "Revisão: Índices B-Tree"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Índices B-Tree

## 📌 Pontos Chave
- **B-Tree:** Estrutura de árvore balanceada que reduz a complexidade de busca de $O(N)$ para $O(\log N)$.
- **Clustered vs Secundário:** A PK organiza a tabela; índices secundários são ponteiros para a PK.
- **Regra do Prefixo:** Índices compostos exigem a presença da primeira coluna para serem ativados.
- **Custo de Escrita:** Cada novo índice torna o `INSERT` e `UPDATE` mais lentos. Equilíbrio é a chave.

## 🛠 Checklist de Domínio
- [ ] Sei explicar a diferença entre Clustered e Non-Clustered Index.
- [ ] Consigo projetar um índice composto eficiente para uma query específica.
- [ ] Sei identificar e remover índices redundantes.
- [ ] Entendo o conceito de Covering Index para performance máxima.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[11-Particionamento]] →
