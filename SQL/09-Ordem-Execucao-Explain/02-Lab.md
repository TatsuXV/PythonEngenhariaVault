---
tipo: lab
trilha: SQL
capitulo: 09
titulo: "Analisando Planos de Execução"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, explain, performance, lab]
---
# Lab: Analisando Planos de Execução

> [!abstract] Capítulo 09 · Analisando Planos de Execução
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_big_orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2)
);

-- Inserindo dados para criar volume
INSERT INTO lab_big_orders (order_id, customer_id, order_date, total_amount) VALUES
(1, 10, '2023-01-01', 100.00), (2, 10, '2023-01-02', 150.00),
(3, 20, '2023-01-01', 200.00), (4, 20, '2023-01-02', 250.00),
(5, 30, '2023-01-01', 300.00), (6, 30, '2023-01-02', 350.00);

-- Criando um índice para testar a diferença
CREATE INDEX idx_customer ON lab_big_orders(customer_id);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado do EXPLAIN
> > [!success] Resposta
> > O `type` será `ref`, a `key` será `idx_customer` e o `rows` será pequeno (estimativa de 2 linhas).
> > **Explicação:** O MySQL usa o índice para ir direto nos registros do cliente 10, evitando ler a tabela toda.

```sql
EXPLAIN SELECT * FROM lab_big_orders WHERE customer_id = 10;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Analisar a performance de uma query que filtra por data. Primeiro, tente fazer a query de forma "Não SARGável" (errada) e depois de forma "SARGável" (correta).

```sql
-- Parte A: Forma ERRADA (Não SARGável)
-- O MySQL não usará o índice porque a função altera a coluna
EXPLAIN SELECT * FROM lab_big_orders 
WHERE # TODO: Use a função YEAR(order_date) = 2023
;

-- Parte B: Forma CORRETA (SARGável)
-- O MySQL usará o índice porque a coluna está "limpa"
EXPLAIN SELECT * FROM lab_big_orders 
WHERE # TODO: Use um intervalo entre '2023-01-01' e '2023-12-31'
;
```

**Como verificar:** Compare a coluna `type` no EXPLAIN. A Parte A provavelmente será `ALL` e a Parte B será `range` ou `ref`.

## 🚀 3. Do Zero
**Enunciado:** Crie uma query que busque pedidos de um cliente específico e ordene por data. Use o `EXPLAIN` e identifique se o MySQL está fazendo um `filesort` (está escrito "Using filesort" na coluna Extra).
**Critério de Aceite:** 
1. Identificar a presença de `Using filesort`.
2. Propor a solução (criar um índice composto) e rodar o `EXPLAIN` novamente para provar que o `Using filesort` sumiu.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Remova o índice `idx_customer` e rode o EXPLAIN da query do exemplo 1 $\rightarrow$ O `type` mudará para `ALL`. Explique o impacto disso em uma tabela de 100 milhões de linhas.
2. Tente fazer um JOIN entre duas tabelas sem índices nas chaves de ligação $\rightarrow$ Observe a coluna `rows` explodir. Explique por que o MySQL teve que ler quase tudo.
3. Use `EXPLAIN ANALYZE` (se estiver no MySQL 8.0.18+) $\rightarrow$ Observe a diferença entre a *estimativa* e o *tempo real* de execução.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
