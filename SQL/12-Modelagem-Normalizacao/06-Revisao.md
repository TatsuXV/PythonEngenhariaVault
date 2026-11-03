---
tipo: revisao
trilha: SQL
capitulo: 12
titulo: "Revisão: Modelagem e Normalização"
nivel: 5
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, revisao]
---
# Revisão: Modelagem e Normalização

## 📌 Pontos Chave
- **Normalização (1NF, 2NF, 3NF):** A base para sistemas transacionais eficientes. Elimina redundâncias e garante que cada dado seja armazenado em um único lugar.
- **Modelagem Dimensional:** A base para BI. O uso de Fatos e Dimensões permite que queries de agregação sejam performáticas.
- **Star vs Snowflake:** Star é mais rápido (menos joins); Snowflake é mais organizado (menos redundância).
- **Integridade:** O uso de Foreign Keys e Constraints é a única forma de garantir que o banco não se torne um "cemitério de dados" inconsistentes.

## 🛠 Checklist de Domínio
- [ ] Sei converter uma tabela "flat" em um modelo normalizado (3NF).
- [ ] Consigo projetar um Star Schema para um cenário de vendas.
- [ ] Entendo a diferença entre chaves naturais e chaves substitutas (Surrogate Keys).
- [ ] Sei quando desnormalizar para ganhar performance analítica.

## 🔗 Links Rápidos
- [[01-Aula]] $\rightarrow$ Teoria
- [[02-Lab]] $\rightarrow$ Prática
- [[03-Tickets]] $\rightarrow$ Aplicação Real

---
← [[05-Flashcards]] · [[MOC-SQL]] · [[Simulado-SQL]] →
