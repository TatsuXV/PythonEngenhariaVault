---
tipo: projeto
trilha: SQL
capitulo: 10
titulo: "Projeto: Estratégia de Indexação para Big Data"
nivel: 4
tempo_estimado_h: 6
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, indexing, performance]
---
# Projeto: Estratégia de Indexação para Big Data

## 🚩 Cenário
A Aurora Tech possui uma tabela de `logs_eventos` com 500 milhões de linhas. Atualmente, as consultas de auditoria estão levando minutos para retornar, e o time de SRE reportou que a tabela está sofrendo com "Index Bloat" (índices excessivos que consomem todo o disco).

## 🎯 Requisitos da Entrega
Você deve entregar um documento de arquitetura de índices contendo:

1. **Análise de Queries:**
    - A query principal filtra por `event_type` e `event_date`, e ordena por `user_id`.
    - Analisar se um índice simples em `event_date` é suficiente.

2. **Proposta de Índice Composto:**
    - Projetar o índice composto ideal para a query acima, aplicando a regra do prefixo à esquerda.
    - Justificar a ordem das colunas no índice (Qual deve vir primeiro e por quê?).

3. **Otimização de Escrita:**
    - Propor uma estratégia para a carga de dados diária (Bulk Load) para que os índices não matem a performance da ingestão.

4. **Validação de Covering Index:**
    - Criar uma query que seja resolvida inteiramente pelo índice, sem acessar a tabela (Index-Only Scan), e provar isso via `EXPLAIN`.

## ✅ Critérios de Aceite
- [ ] Justificativa técnica baseada na estrutura de B-Tree.
- [ ] Prova de que o índice composto reduz o `rows` lidos no `EXPLAIN`.
- [ ] Estratégia de ingestão validada (ex: Drop $\rightarrow$ Load $\rightarrow$ Recreate).
- [ ] Identificação clara de índices redundantes a serem removidos.

## 🧪 Como Validar
1. Use a tabela `lab_big_orders` do Lab 10 para simular o volume.
2. Rode o `EXPLAIN` da query sem o índice composto.
3. Crie o índice proposto e rode o `EXPLAIN` novamente.
4. Compare o custo de CPU/IO estimado.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[11-Particionamento]] →
