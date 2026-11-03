---
tipo: projeto
trilha: SQL
capitulo: 08
titulo: "Projeto: Sistema de Transferência Bancária Segura"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, transactions, acid]
---
# Projeto: Sistema de Transferência Bancária Segura

## 🚩 Cenário
Você deve criar a lógica de backend para um módulo de transferências bancárias. O sistema deve garantir que, em hipótese alguma, o dinheiro "desapareça" ou seja "criado do nada" devido a falhas no sistema ou concorrência de usuários.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL que implemente a seguinte lógica de transação:

1. **Criação de Ambiente:**
    - Tabela `contas` (`conta_id` PK, `cliente` VARCHAR, `saldo` DECIMAL).
    - Tabela `transacoes_log` (`transacao_id` PK, `conta_origem`, `conta_destino`, `valor`, `data_transacao`).

2. **Lógica de Transferência (A Transação):**
    - Iniciar uma transação.
    - **Passo 1:** Verificar se a conta de origem tem saldo suficiente. Se não tiver, disparar um erro e fazer `ROLLBACK`.
    - **Passo 2:** Subtrair o valor da conta de origem.
    - **Passo 3:** Adicionar o valor à conta de destino.
    - **Passo 4:** Inserir o registro na `transacoes_log`.
    - **Passo 5:** Confirmar tudo com `COMMIT`.

3. **Desafio de Concorrência:**
    - O script deve incluir comentários explicando como você evitaria que duas transferências simultâneas da mesma conta gerassem um saldo negativo (Dica: Pesquise sobre `FOR UPDATE` ou Locks).

## ✅ Critérios de Aceite
- [ ] Uso correto de `START TRANSACTION`, `COMMIT` e `ROLLBACK`.
- [ ] Validação de saldo antes da operação.
- [ ] Atomicidade: Se o log de transação falhar, o dinheiro deve voltar para a conta de origem.
- [ ] Implementação de `SAVEPOINT` para permitir a recuperação de erros menores sem cancelar a transação inteira.

## 🧪 Como Validar
1. Realize uma transferência com saldo insuficiente $\rightarrow$ Verifique se nenhum saldo foi alterado.
2. Realize uma transferência válida $\rightarrow$ Verifique se ambos os saldos mudaram e o log foi criado.
3. Simule a queda do sistema após o Passo 2 (comente o COMMIT) $\rightarrow$ Verifique se o `ROLLBACK` automático recuperou o dinheiro.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[09-Ordem-Execucao-Explain]] →
