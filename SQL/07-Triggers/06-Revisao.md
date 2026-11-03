---
tipo: revisao
trilha: SQL
capitulo: 07
titulo: "Revisão: Triggers"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Triggers

## 📌 Pontos Chave
- **Reatividade:** Triggers transformam o banco de dados em um sistema reativo, automatizando a auditoria sem depender da aplicação.
- **Integridade:** O uso de `BEFORE INSERT/UPDATE` é a última linha de defesa para garantir que dados inválidos não entrem no sistema.
- **Custo de Escrita:** Lembre-se que cada Trigger adiciona tempo ao comando de escrita. Em tabelas de alta frequência, prefira auditoria via binlogs ou CDC (Change Data Capture).
- **Escopo:** O MySQL utiliza triggers de linha (`FOR EACH ROW`), processando cada registro individualmente.

## 🛠 Checklist de Domínio
- [ ] Sei a diferença entre triggers `BEFORE` e `AFTER`.
- [ ] Consigo utilizar `OLD` e `NEW` para capturar mudanças de estado.
- [ ] Sei implementar um sistema de log de auditoria automático.
- [ ] Entendo a limitação de recursividade (não atualizar a própria tabela).

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[08-Transacoes-Isolamento]] →
