---
tipo: aula
trilha: SQL
capitulo: 08
titulo: "Transações e Isolamento: A Garantia de Integridade"
nivel: 4
tempo_estimado_h: 8
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, transactions, acid, isolation]
comparativo_dialecto: true
---
# Transações e Isolamento: A Garantia de Integridade

> [!abstract] Capítulo 08 · Transações e Isolamento: A Garantia de Integridade
> ⏱ 8h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[07-Triggers]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: O que significa a sigla ACID em bancos de dados?
> ?
> [!question] Pergunta 2: Qual a diferença entre `COMMIT` e `ROLLBACK`?
> ?
> [!question] Pergunta 3: O que é um "Deadlock" e como o MySQL reage a ele?
> ?

## 🎯 Objetivo
> [!goal]
> Compreender como agrupar múltiplas operações em uma única unidade de trabalho atômica, garantindo que o banco de dados nunca fique em um estado inconsistente, mesmo em caso de falhas de hardware ou concorrência de usuários.

## ⚙️ No Pipeline
> [!pipeline]
> Imagine um sistema bancário: você tira dinheiro de uma conta (UPDATE) e deposita em outra (UPDATE). Se o sistema cair entre as duas operações, o dinheiro desaparece. Transações impedem isso. Para um Engenheiro de Dados, transações são vitais em processos de carga (ETL) para garantir que a tabela final não seja populada parcialmente se o Job falhar no meio.

## 📚 Teoria

### 1. Propriedades ACID
Para ser considerada confiável, uma transação deve ser:
- **A (Atomicity - Atomicidade):** Ou tudo acontece, ou nada acontece. Se um passo falha, tudo volta ao estado anterior.
- **C (Consistency - Consistência):** A transação leva o banco de um estado válido a outro estado válido (respeitando constraints).
- **I (Isolation - Isolamento):** Transações simultâneas não devem interferir umas nas outras.
- **D (Durability - Durabilidade):** Uma vez confirmado (`COMMIT`), o dado está salvo permanentemente, mesmo que o servidor caia logo depois.

### 2. Controle de Transações no MySQL
Por padrão, o MySQL usa `autocommit = 1` (cada query é uma transação). Para agrupar operações, usamos:
- `START TRANSACTION` ou `BEGIN`: Inicia a transação.
- `COMMIT`: Salva todas as alterações permanentemente.
- `ROLLBACK`: Descarta todas as alterações desde o início da transação.

### 3. Níveis de Isolamento (Isolation Levels)
Controlam a visibilidade dos dados não confirmados entre diferentes sessões:
- **READ UNCOMMITTED:** Permite "Dirty Reads" (ler dados que ainda não foram confirmados). Perigoso.
- **READ COMMITTED:** Só lê dados confirmados. Evita Dirty Reads, mas permite "Non-repeatable Reads".
- **REPEATABLE READ (Padrão do MySQL):** Garante que se você ler a mesma linha duas vezes, verá o mesmo valor. Evita a maioria dos problemas, mas pode permitir "Phantom Reads".
- **SERIALIZABLE:** O nível mais alto. Executa as transações como se fossem em fila. Lento, mas totalmente seguro.

### 4. Locks (Bloqueios)
O MySQL usa locks para evitar conflitos:
- **Shared Lock (S):** Várias sessões podem ler, mas ninguém pode alterar.
- **Exclusive Lock (X):** Apenas uma sessão pode ler ou alterar. Outras devem esperar.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Default Isolation** | `READ COMMITTED` | `REPEATABLE READ` | O MySQL é mais "conservador" por padrão, o que pode causar mais Deadlocks em sistemas de alta concorrência do que o Postgres. |
> | **Transaction Control** | Suporta `SAVEPOINT` e `ROLLBACK TO`. | Também suporta `SAVEPOINT` e `ROLLBACK TO`. | Sintaxe quase idêntica. |
> | **MVCC** | Implementação robusta de Multi-Version Concurrency Control. | Implementação via `Undo Logs` no InnoDB. | Ambos evitam que leituras bloqueiem escritas, mas a gestão do Undo Log no MySQL pode impactar o disco em transações gigantescas. |

## ⚠️ Armadilhas e Erros Comuns
- **Transações Longas:** Manter uma transação aberta por horas bloqueia linhas e consome memória do `Undo Log`. Regra: Mantenha transações curtas e rápidas.
- **Esquecer o COMMIT:** Em ferramentas como Workbench, se você desativar o autocommit e esquecer o commit, seus dados não serão salvos e você poderá bloquear outros usuários.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `START TRANSACTION; UPDATE acc SET bal = bal - 100 WHERE id = 1; UPDATE acc SET bal = bal + 100 WHERE id = 2;` (Sem commit).
> **Por que está errado:** Sem o `COMMIT`, as alterações ficam "pendentes". Se a conexão cair, o MySQL fará rollback automático.
> **Correto:** Adicionar `COMMIT;` ao final da sequência.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude sobre **Deadlocks**: Quando a Transação A espera pela Transação B, que por sua vez espera pela Transação A. O MySQL detecta isso automaticamente e "mata" a transação menor para liberar o sistema.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - InnoDB Transactions](https://dev.mysql.com/doc/refman/8.0/en/innodb-transactions.html) (Versão 8.0)

---
← [[07-Triggers]] · [[MOC-SQL]] · [[09-Ordem-Execucao-Explain]] →
