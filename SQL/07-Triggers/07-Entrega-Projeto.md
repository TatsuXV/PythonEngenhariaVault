---
tipo: projeto
trilha: SQL
capitulo: 07
titulo: "Projeto: Sistema de Controle de Estoque e Auditoria"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, triggers, audit]
---
# Projeto: Sistema de Controle de Estoque e Auditoria

## 🚩 Cenário
A Aurora Tech possui um armazém de hardware. Eles precisam de um sistema que garanta que o estoque nunca fique negativo e que qualquer alteração no preço ou na quantidade de produtos seja registrada para auditoria interna.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL único que implemente a seguinte lógica:

1. **Tabelas:**
    - `produtos` (`prod_id` PK, `nome`, `preco`, `estoque`).
    - `estorno_estoque` (`estorno_id` PK, `prod_id`, `qtd_alterada`, `data_estorno`).
    - `log_auditoria` (`log_id` PK, `prod_id`, `coluna_alterada`, `valor_antigo`, `valor_novo`, `usuario`, `data_log`).

2. **Lógica de Trigger 1 (Integridade):**
    - Um trigger `BEFORE UPDATE` na tabela `produtos` que impeça a alteração do estoque para um valor negativo. Se o valor for negativo, o trigger deve forçar o estoque para 0.

3. **Lógica de Trigger 2 (Auditoria de Preços):**
    - Um trigger `AFTER UPDATE` que, sempre que o preço do produto mudar, insira um registro na `log_auditoria` detalhando o preço antigo e o novo.

4. **Lógica de Trigger 3 (Controle de Exclusão):**
    - Um trigger `BEFORE DELETE` que, antes de excluir um produto, insira automaticamente os dados do produto na tabela `estorno_estoque` para fins de backup.

## ✅ Critérios de Aceite
- [ ] Uso correto de `DELIMITER`.
- [ ] Implementação de `BEFORE` e `AFTER` triggers.
- [ ] Uso correto de `OLD` e `NEW`.
- [ ] Validação de que o estoque não fica negativo.

## 🧪 Como Validar
1. Tente atualizar o estoque de um produto para -10 e verifique se ele foi salvo como 0.
2. Altere o preço de um produto e verifique a tabela `log_auditoria`.
3. Delete um produto e verifique se ele foi espelhado na tabela `estorno_estoque`.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[08-Transacoes-Isolamento]] →
