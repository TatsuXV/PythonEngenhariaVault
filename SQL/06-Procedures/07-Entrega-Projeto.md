---
tipo: projeto
trilha: SQL
capitulo: 06
titulo: "Projeto: Orquestrador de ETL Interno"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, automation, etl]
---
# Projeto: Orquestrador de ETL Interno

## 🚩 Cenário
Você precisa criar um sistema de "limpeza e carga" automatizado. Os dados de vendas chegam em uma tabela chamada `stg_sales` (staging). Você deve criar uma procedure que orquestre todo o processo de movimentação desses dados para a tabela final `fact_sales`.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL contendo a criação de uma Procedure chamada `sp_etl_sales_load` que realize os seguintes passos:

1. **Validação:** Verificar se a tabela `stg_sales` possui dados. Se estiver vazia, a procedure deve encerrar a execução imediatamente e retornar uma mensagem de "Sem dados para carregar" via parâmetro `OUT`.
2. **Limpeza:** Identificar e deletar registros duplicados na `stg_sales` baseando-se no `order_id` (manter apenas o registro mais recente).
3. **Carga:** Inserir os dados limpos da `stg_sales` na tabela `fact_sales`.
4. **Finalização:** Limpar a tabela `stg_sales` (`TRUNCATE`) para a próxima carga.
5. **Log:** Inserir um registro na tabela `etl_logs` com a data, a quantidade de linhas carregadas e o status 'SUCCESS'.

## ✅ Critérios de Aceite
- [ ] Uso correto de `DELIMITER`.
- [ ] Implementação de lógica condicional (`IF`) para a validação inicial.
- [ ] Uso de parâmetros `OUT` para feedback de execução.
- [ ] Orquestração correta da sequência: Validar $\rightarrow$ Limpar $\rightarrow$ Carregar $\rightarrow$ Truncar $\rightarrow$ Logar.

## 🧪 Como Validar
Crie as tabelas `stg_sales`, `fact_sales` e `etl_logs`. Insira dados duplicados na staging e execute a procedure. Verifique se a `fact_sales` contém apenas dados únicos e se o log foi gerado.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[07-Triggers]] →
