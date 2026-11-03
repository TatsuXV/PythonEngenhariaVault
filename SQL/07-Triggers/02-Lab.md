---
tipo: lab
trilha: SQL
capitulo: 07
titulo: "Sistemas de Auditoria e Integridade"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, triggers, lab]
---
# Lab: Sistemas de Auditoria e Integridade

> [!abstract] Capítulo 07 · Sistemas de Auditoria e Integridade
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
-- Tabela de Produtos
CREATE TABLE IF NOT EXISTS lab_products_t (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10, 2),
    stock INT
);

-- Tabela de Log de Auditoria
CREATE TABLE IF NOT EXISTS lab_product_logs (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    old_price DECIMAL(10, 2),
    new_price DECIMAL(10, 2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO lab_products_t VALUES 
(1, 'Mouse', 50.00, 100), 
(2, 'Teclado', 150.00, 50), 
(3, 'Monitor', 800.00, 20);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Toda vez que o preço de um produto for alterado, uma nova linha será inserida automaticamente na `lab_product_logs` com o valor antigo e o novo.
> > Se você fizer `UPDATE lab_products_t SET price = 60 WHERE product_id = 1;`, a tabela de logs terá: (1, 50.00, 60.00, timestamp).
> > **Explicação:** O trigger `AFTER UPDATE` captura o estado `OLD` e `NEW` da linha.

```sql
DELIMITER //
CREATE TRIGGER tr_audit_price
AFTER UPDATE ON lab_products_t
FOR EACH ROW
BEGIN
    IF OLD.price <> NEW.price THEN
        INSERT INTO lab_product_logs (product_id, old_price, new_price)
        VALUES (OLD.product_id, OLD.price, NEW.price);
    END IF;
END //
DELIMITER ;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar um trigger `BEFORE INSERT` que impeça a inserção de produtos com preço negativo, forçando o preço a ser 0 caso seja negativo.

```sql
DELIMITER //
CREATE TRIGGER tr_validate_price
BEFORE INSERT ON lab_products_t
FOR EACH ROW
BEGIN
    -- TODO: Verifique se o novo preço é menor que 0
    IF NEW.price < 0 THEN
        -- TODO: Force o preço a ser 0
        SET NEW.price = 0;
    END IF;
END //
DELIMITER ;
```

**Como verificar:** `INSERT INTO lab_products_t VALUES (4, 'Erro', -10.00, 10);` $\rightarrow$ Verifique se o preço foi salvo como 0.

## 🚀 3. Do Zero
**Enunciado:** Crie um trigger chamado `tr_update_stock_log` que, sempre que um produto for deletado da tabela `lab_products_t`, insira uma mensagem na tabela `lab_product_logs` (você precisará adicionar uma coluna `action` na tabela de logs primeiro) informando que o produto X foi removido.
**Critério de Aceite:** 
1. Uso de `AFTER DELETE`.
2. Referência correta ao `OLD.product_name`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. No trigger de auditoria, tente fazer: `UPDATE lab_products_t SET stock = stock - 1 WHERE product_id = NEW.product_id;` $\rightarrow$ Erro esperado: **Can't update table in stored function/trigger**. Explique a proibição de recursividade.
2. Tente criar um trigger `AFTER TRUNCATE` $\rightarrow$ Erro esperado: Sintaxe inválida. Explique por que o `TRUNCATE` não dispara triggers.
3. Remova o `DELIMITER` e tente criar o trigger $\rightarrow$ Erro esperado: **Error 1064**. Explique a confusão do MySQL com o `;`.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
