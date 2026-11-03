---
tipo: aula
trilha: SQL
capitulo: 07
titulo: "Triggers: As Sentinelas do Banco"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, triggers, audit, integrity]
comparativo_dialecto: true
---
# Triggers: As Sentinelas do Banco

> [!abstract] Capítulo 07 · Triggers: As Sentinelas do Banco
> ⏱ 6h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[06-Procedures]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença fundamental entre uma Procedure e um Trigger?
> ?
> [!question] Pergunta 2: O que significam as palavras-chave `OLD` e `NEW` em um Trigger?
> ?
> [!question] Pergunta 3: É possível disparar um Trigger a partir de um comando `TRUNCATE`?
> ?

## 🎯 Objetivo
> [!goal]
> Implementar lógicas de automação reativas, onde o banco de dados reage automaticamente a alterações de dados, garantindo integridade, auditoria e sincronização sem a necessidade de intervenção manual ou de código externo.

## ⚙️ No Pipeline
> [!pipeline]
> Em Engenharia de Dados, Triggers são frequentemente usados para alimentar tabelas de auditoria (Logs) ou para atualizar tabelas de agregação em tempo real. Por exemplo: toda vez que uma venda é inserida na `fact_sales`, um Trigger pode atualizar automaticamente a `dim_vendedor_total_vendas`.

## 📚 Teoria

### 1. O que são Triggers?
Um Trigger (gatilho) é um objeto do banco de dados que "dispara" automaticamente quando ocorre um evento específico: `INSERT`, `UPDATE` ou `DELETE` em uma tabela.

### 2. Momentos de Disparo
No MySQL, você define quando o trigger deve agir:
- `BEFORE`: Executa **antes** da alteração ser gravada no disco. Ideal para validação e limpeza de dados.
- `AFTER`: Executa **depois** da alteração. Ideal para auditoria e sincronização de outras tabelas.

### 3. As Palavras-Chave `OLD` e `NEW`
Para saber o que mudou, o MySQL disponibiliza:
- `OLD`: Refere-se aos valores da linha **antes** da alteração. (Disponível em `UPDATE` e `DELETE`).
- `NEW`: Refere-se aos valores da linha **após** a alteração. (Disponível em `INSERT` e `UPDATE`).

### 4. Restrições Importantes
- **Recursividade:** Um Trigger não pode alterar a própria tabela que o disparou (isso causaria um loop infinito).
- **Performance:** Triggers adicionam um "overhead" a cada operação de escrita. Muitos triggers em tabelas de alta carga podem degradar a performance do sistema.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Implementação** | Exige a criação de uma `FUNCTION` separada que o Trigger então chama. | O código do Trigger é escrito **dentro** da definição do Trigger. | No MySQL, a sintaxe é mais direta, mas menos modular que no Postgres. |
> | **Tipos de Eventos** | Suporta `INSTEAD OF` (para Views). | **NÃO suporta** `INSTEAD OF`. | Se você precisa de lógica ao alterar uma View no MySQL, terá que usar INSTEAD OF via triggers em tabelas base ou mudar a arquitetura. |
> | **Tabelas de Transição** | Possui a tabela `NEW` e `OLD` como conjuntos de dados. | Possui `NEW` e `OLD` como referências a uma única linha. | O MySQL processa triggers linha a linha (row-level). |

## ⚠️ Armadilhas e Erros Comuns
- **Tentar atualizar a própria tabela:** O erro "Can't update table in stored function/trigger" é clássico. Use `BEFORE UPDATE` para mudar valores da mesma linha através de `SET NEW.coluna = valor`.
- **Ignorar o impacto no Bulk Insert:** Se você fizer um `INSERT` de 1 milhão de linhas, o trigger disparará 1 milhão de vezes.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `CREATE TRIGGER audit_update AFTER UPDATE ON users FOR EACH ROW INSERT INTO logs (user_id) VALUES (OLD.id);`
> **Por que está errado:** Falta o `DELIMITER`. Como em procedures, triggers usam blocos de código com `;`.
> **Correto:** 
> `DELIMITER //`
> `CREATE TRIGGER audit_update AFTER UPDATE ON users FOR EACH ROW BEGIN INSERT INTO logs (user_id) VALUES (OLD.id); END //`
> `DELIMITER ;`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude a diferença entre **Row-Level Triggers** (linha a linha) e **Statement-Level Triggers** (uma vez por comando). O MySQL suporta apenas Row-Level.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Triggers](https://dev.mysql.com/doc/refman/8.0/en/triggers.html) (Versão 8.0)

---
← [[06-Procedures]] · [[MOC-SQL]] · [[08-Transacoes-Isolamento]] →
