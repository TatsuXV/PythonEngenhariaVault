---
tipo: revisao
trilha: SQL
capitulo: 06
titulo: "Revisão: Stored Procedures"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Stored Procedures

## 📌 Pontos Chave
- **Encapsulamento:** Procedures transformam sequências de queries em comandos únicos (`CALL`).
- **Delimitadores:** `DELIMITER //` é a chave para criar blocos procedurais no MySQL.
- **Fluxo de Controle:** `IF`, `WHILE` e `CASE` permitem que o SQL tome decisões.
- **Custo de Processamento:** Lembre-se que a CPU do banco é mais cara que a CPU do servidor de aplicação. Use procedures para orquestração, não para cálculos matemáticos massivos.

## 🛠 Checklist de Domínio
- [ ] Consigo criar uma procedure com parâmetros `IN` e `OUT`.
- [ ] Sei usar `DECLARE` para criar variáveis locais.
- [ ] Domino o uso de `IF...THEN...ELSE` dentro de blocos procedurais.
- [ ] Sei a diferença entre `CALL` (para procedure) e a chamada de uma `FUNCTION`.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[07-Triggers]] →
