---
tipo: lab
trilha: SQL
capitulo: 06
titulo: "Automação de Rotinas e Lógica Procedural"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, procedures, lab]
---
# Lab: Automação de Rotinas e Lógica Procedural

> [!abstract] Capítulo 06 · Automação de Rotinas e Lógica Procedural
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_account_balance (
    account_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    balance DECIMAL(10, 2)
);

INSERT INTO lab_account_balance VALUES 
(1, 'Alice', 1000.00), 
(2, 'Bob', 500.00), 
(3, 'Charlie', 100.00);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Se chamarmos `CALL sp_update_balance(1, 200.00)`, o saldo de Alice passará de 1000.00 para 1200.00.
> > **Explicação:** A procedure recebe o ID e o valor, e executa um UPDATE interno.

```sql
DELIMITER //
CREATE PROCEDURE sp_update_balance(IN p_acc_id INT, IN p_amount DECIMAL(10,2))
BEGIN
    UPDATE lab_account_balance 
    SET balance = balance + p_amount 
    WHERE account_id = p_acc_id;
END //
DELIMITER ;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar uma procedure que receba um ID de conta e retorne via parâmetro `OUT` se a conta tem saldo positivo ou negativo.

```sql
DELIMITER //
CREATE PROCEDURE sp_check_status(IN p_acc_id INT, OUT p_status VARCHAR(20))
BEGIN
    DECLARE v_balance DECIMAL(10,2);
    
    -- TODO: Selecione o saldo da conta para a variável v_balance
    SELECT balance INTO v_balance FROM lab_account_balance WHERE account_id = p_acc_id;
    
    -- TODO: Use IF para definir p_status como 'POSITIVO' ou 'NEGATIVO'
    IF v_balance > 0 THEN
        SET p_status = 'POSITIVO';
    ELSE
        SET p_status = 'NEGATIVO';
    END IF;
END //
DELIMITER ;
```

**Como verificar:** 
`CALL sp_check_status(1, @res); SELECT @res;`

## 🚀 3. Do Zero
**Enunciado:** Crie uma procedure chamada `sp_bulk_bonus` que adicione um bônus de 10% ao saldo de TODAS as contas que possuem menos de 200.00 de saldo.
**Critério de Aceite:** 
1. A procedure não deve receber parâmetros.
2. Deve usar a lógica de `UPDATE` com `WHERE`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Tente criar a procedure sem usar o `DELIMITER //` $\rightarrow$ Erro esperado: **Error 1064 (42000)**. Explique por que o MySQL para no primeiro `;`.
2. Tente usar `SET p_status = 'POSITIVO'` fora de um bloco `BEGIN...END` $\rightarrow$ Erro esperado: Sintaxe inválida. Explique a necessidade do bloco procedural.
3. Tente chamar a procedure com um tipo de dado incompatível (ex: string no lugar do ID INT) $\rightarrow$ Observe como o MySQL tenta converter o dado ou retorna erro de tipo.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
