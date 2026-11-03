---
tipo: aula
trilha: SQL
capitulo: 06
titulo: "Stored Procedures: Automatizando o Banco"
nivel: 4
tempo_estimado_h: 8
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, procedures, automation]
comparativo_dialecto: true
---
# Stored Procedures: Automatizando o Banco

> [!abstract] Capítulo 06 · Stored Procedures: Automatizando o Banco
> ⏱ 8h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[05-CTE-Views-Tabelas]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença entre uma Function e uma Procedure?
> ?
> [!question] Pergunta 2: Para que servem os parâmetros `IN`, `OUT` e `INOUT`?
> ?
> [!question] Pergunta 3: Por que devemos usar o comando `DELIMITER` ao criar procedures no MySQL?
> ?

## 🎯 Objetivo
> [!goal]
> Aprender a encapsular lógica de negócio complexa dentro do próprio servidor de banco de dados, reduzindo o tráfego de rede e automatizando tarefas repetitivas através de rotinas programáveis.

## ⚙️ No Pipeline
> [!pipeline]
> Como Engenheiro de Dados, você usará Procedures para criar a orquestração de pipelines dentro do banco. Por exemplo, uma procedure pode limpar a tabela de staging, carregar novos dados, validar a integridade e atualizar a tabela final. Tudo isso disparado por um único comando `CALL`.

## 📚 Teoria

### 1. O que são Stored Procedures?
São blocos de código SQL salvos no servidor que podem ser executados repetidamente. Diferente de uma query simples, elas permitem lógica de programação (variáveis, loops, condicionais).

### 2. Parâmetros de Entrada e Saída
- `IN`: O valor entra na procedure, mas não pode ser alterado para quem a chamou.
- `OUT`: A procedure calcula um valor e o "devolve" para quem a chamou.
- `INOUT`: O valor entra, pode ser modificado e é devolvido.

### 3. Lógica de Controle (Flow Control)
- `IF ... THEN ... ELSE`: Decisões lógicas.
- `WHILE ... DO`: Loops baseados em condição.
- `REPEAT ... UNTIL`: Loops que executam ao menos uma vez.
- `CASE`: Escolhas múltiplas.

### 4. Variáveis Locais
Usamos `DECLARE` para criar variáveis que existem apenas enquanto a procedure está rodando.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Linguagem** | Usa PL/pgSQL (muito poderoso, similar a Oracle). | Usa a sintaxe procedural do MySQL (mais simples). | Se você migrar de Postgres, sentirá falta de algumas funções avançadas de manipulação de arrays. |
> | **Retorno de Dados** | Procedures podem retornar conjuntos de resultados facilmente. | Procedures retornam resultados via `SELECT` simples ou parâmetros `OUT`. | No MySQL, para retornar um valor único, prefira criar uma `FUNCTION`. |
> | **Delimitadores** | Geralmente usa `$$` ou `'` para envolver o bloco. | Exige a alteração do `DELIMITER` (ex: para `//`). | No MySQL, você deve mudar o delimitador para que o banco não ache que a procedure acabou no primeiro `;` interno. |

## ⚠️ Armadilhas e Erros Comuns
- **Performance:** Colocar lógica excessiva no banco pode sobrecarregar a CPU do servidor SQL. Lógicas pesadas de transformação devem ficar no Python/Spark.
- **Debug:** Debugar procedures é difícil. A dica é criar tabelas de log para inserir mensagens de status durante a execução.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `CREATE PROCEDURE update_salaries() BEGIN UPDATE emp SET salary = salary * 1.1; END;`
> **Por que está errado:** Falta o `DELIMITER`. O MySQL vai tentar executar a query no primeiro `;` do `UPDATE` e dará erro de sintaxe no `END;`.
> **Correto:** 
> `DELIMITER //`
> `CREATE PROCEDURE update_salaries() BEGIN UPDATE emp SET salary = salary * 1.1; END //`
> `DELIMITER ;`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude a diferença entre **Deterministic** e **Non-deterministic** procedures. Isso afeta a replicação do banco de dados e a performance de cache.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Stored Objects](https://dev.mysql.com/doc/refman/8.0/en/stored-objects.html) (Versão 8.0)

---
← [[05-CTE-Views-Tabelas]] · [[MOC-SQL]] · [[07-Triggers]] →
