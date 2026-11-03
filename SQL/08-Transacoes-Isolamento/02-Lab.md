---
tipo: lab
trilha: SQL
capitulo: 08
titulo: "Prática de Atomicidade e Controle de Concorrência"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, transactions, lab]
---
# Lab: Prática de Atomicidade e Controle de Concorrência

> [!abstract] Capítulo 08 · Prática de Atomicidade e Controle de Concorrência
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_bank_accounts (
    account_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    balance DECIMAL(10, 2)
);

INSERT INTO lab_bank_accounts VALUES 
(1, 'Alice', 1000.00), 
(2, 'Bob', 1000.00), 
(3, 'Charlie', 1000.00);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > O saldo de Alice será 900.00 e o de Bob 1100.00. A operação foi atômica: as duas atualizações foram confirmadas juntas.
> > **Explicação:** O `COMMIT` encerra a transação e torna as mudanças permanentes.

```sql
START TRANSACTION;
UPDATE lab_bank_accounts SET balance = balance - 100 WHERE account_id = 1;
UPDATE lab_bank_accounts SET balance = balance + 100 WHERE account_id = 2;
COMMIT;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Simular uma transferência que falha no meio do caminho. Você deve iniciar a transação, retirar dinheiro de uma conta, mas então desistir da operação para garantir que o dinheiro não "suma".

```sql
# TODO: Inicie a transação
START TRANSACTION;

UPDATE lab_bank_accounts 
SET balance = balance - 500 
WHERE account_id = 1;

-- Simulando um erro no sistema ou desistência do usuário
# TODO: Use o comando para desfazer todas as alterações da transação
ROLLBACK;
```

**Como verificar:** `SELECT * FROM lab_bank_accounts;` $\rightarrow$ O saldo de Alice deve continuar sendo 1000.00.

## 🚀 3. Do Zero
**Enunciado:** Crie um script que realize a seguinte sequência:
1. Inicie uma transação.
2. Retire 200.00 da conta 1.
3. Crie um `SAVEPOINT` chamado `depois_do_primeiro_passo`.
4. Tente retirar 200.00 da conta 2, mas perceba que houve um erro.
5. Volte para o `SAVEPOINT` (cancelando apenas a segunda retirada).
6. Confirme (`COMMIT`) a operação.
**Critério de Aceite:** Ao final, a conta 1 deve ter 800.00 e a conta 2 deve ter 1000.00.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Desative o autocommit (`SET autocommit = 0;`), faça um `UPDATE` e feche o MySQL Workbench sem dar `COMMIT`. $\rightarrow$ Resultado: O dado não foi salvo. Explique o comportamento do MySQL ao perder a conexão.
2. Abra duas abas no Workbench. Na aba A, inicie uma transação e dê um `UPDATE` na conta 1 (sem commit). Na aba B, tente dar um `UPDATE` na mesma conta 1. $\rightarrow$ Resultado: A aba B fica "carregando" (travada). Explique o conceito de **Exclusive Lock**.
3. Altere o nível de isolamento para `READ UNCOMMITTED` (`SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;`) e repita o teste acima. $\rightarrow$ Observe se a aba B consegue ler o valor alterado pela aba A mesmo sem o commit.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
