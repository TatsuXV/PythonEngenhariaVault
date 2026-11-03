---
tipo: projeto
trilha: SQL
capitulo: 02
titulo: "Projeto: Estruturação de Base de Vendas"
nivel: 2
tempo_estimado_h: 3
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, modelagem]
---
# Projeto: Estruturação de Base de Vendas

## 🚩 Cenário
A empresa "Aurora Tech" está migrando seus dados de planilhas para o MySQL. Você precisa criar a estrutura inicial do banco de dados e gerar o primeiro relatório de performance de vendas por categoria.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL único contendo:

1. **DDL:**
    - Criar a tabela `categorias` (`cat_id` PK, `nome_categoria`).
    - Criar a tabela `produtos` (`prod_id` PK, `nome`, `preco`, `cat_id` FK).
    - Criar a tabela `vendas` (`venda_id` PK, `prod_id` FK, `quantidade`, `data_venda`).

2. **DML:**
    - Inserir 3 categorias, 5 produtos e 10 vendas distribuídas entre eles.

3. **Análise (Query Final):**
    - Gerar um relatório que mostre o `nome_categoria` e o **valor total vendido** (quantidade * preco) por categoria.
    - Filtrar para exibir apenas categorias que venderam mais de 500.00 no total.
    - Ordenar do maior faturamento para o menor.

## ✅ Critérios de Aceite
- [ ] Uso correto de chaves estrangeiras (`FOREIGN KEY`).
- [ ] Implementação correta de `AUTO_INCREMENT`.
- [ ] Uso de `JOIN` (opcional, mas recomendado) ou subqueries para ligar as tabelas.
- [ ] Uso de `GROUP BY` e `HAVING`.

## 🧪 Como Validar
Execute o script completo no MySQL 8.x e valide se o relatório final retorna a categoria com maior faturamento no topo.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[03-Join-Having]] →
