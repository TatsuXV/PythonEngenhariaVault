---
tipo: projeto
trilha: SQL
capitulo: 11
titulo: "Projeto: Estrutura de Logs de Alta Performance"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, partitioning, big-data]
---
# Projeto: Estrutura de Logs de Alta Performance

## 🚩 Cenário
A Aurora Tech processa 10 milhões de eventos de log por dia. A tabela de logs está se tornando impossível de gerenciar. Consultas simples de "últimas 24 horas" estão levando minutos. Além disso, a política de retenção exige que logs com mais de 6 meses sejam excluídos.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL completo que implemente:

1. **Arquitetura de Particionamento:**
    - Criar a tabela `system_events` particionada por **RANGE** usando a data do evento.
    - Criar partições mensais para o ano corrente e uma partição `p_old` para dados anteriores.
    - Garantir que a Primary Key inclua a coluna de data para permitir o particionamento.

2. **Estratégia de Ingestão:**
    - Implementar um script de carga que utilize a partição correta.
    - Criar um índice local em `event_type` para acelerar a busca dentro de cada partição.

3. **Rotina de Manutenção (Data Lifecycle):**
    - Criar uma procedure chamada `sp_cleanup_old_logs` que identifique e remova a partição mais antiga (anterior a 6 meses) usando `DROP PARTITION`.

4. **Validação de Performance:**
    - Escrever uma query de busca por data e fornecer o `EXPLAIN` provando que o **Partition Pruning** está funcionando (mostrando que apenas 1 partição foi acessada).

## ✅ Critérios de Aceite
- [ ] Uso correto de `PARTITION BY RANGE`.
- [ ] Implementação de índices locais eficientes.
- [ ] Automação da remoção de dados via `DROP PARTITION`.
- [ ] Prova documental via `EXPLAIN` de que a poda de partições está ativa.

## 🧪 Como Validar
1. Insira dados de 3 meses diferentes.
2. Execute a query de busca para um único mês e verifique no `EXPLAIN` a coluna `partitions`.
3. Execute a procedure de limpeza e verifique se a partição mais antiga sumiu instantaneamente.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[12-Modelagem-Normalizacao]] →
