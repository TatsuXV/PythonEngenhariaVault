---
tipo: lab
trilha: SQL
capitulo: 04
titulo: "Análise de Rankings e Séries Temporais"
nivel: 4
tempo_estimado_h: 5
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, window-functions, lab]
---
# Lab: Análise de Rankings e Séries Temporais

> [!abstract] Capítulo 04 · Análise de Rankings e Séries Temporais
> ⏱ 5h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_sales_wf (
    sale_id INT PRIMARY KEY,
    seller_id INT,
    sale_date DATE,
    amount DECIMAL(10, 2)
);

INSERT INTO lab_sales_wf (sale_id, seller_id, sale_date, amount) VALUES
(1, 1, '2023-01-01', 100.00),
(2, 1, '2023-01-02', 150.00),
(3, 1, '2023-01-03', 120.00),
(4, 2, '2023-01-01', 200.00),
(5, 2, '2023-01-02', 200.00),
(6, 2, '2023-01-03', 300.00),
(7, 3, '2023-01-01', 50.00),
(8, 3, '2023-01-02', 80.00),
(9, 3, '2023-01-03', 100.00);
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > Retornará a venda, o vendedor e a soma acumulada das vendas daquele vendedor ao longo do tempo.
> > Vendedor 1: 100 -> 250 -> 370.
> > **Explicação:** `PARTITION BY` separa os vendedores; `ORDER BY` define a sequência da soma.

```sql
SELECT 
    sale_id, 
    seller_id, 
    amount,
    SUM(amount) OVER (PARTITION BY seller_id ORDER BY sale_date) as running_total
FROM lab_sales_wf;
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar um ranking de vendas por vendedor. Se houver empate no valor, o ranking deve pular números (`RANK`).

```sql
SELECT 
    seller_id, 
    amount,
    # TODO: Use a função RANK() com OVER
    OVER (ORDER BY amount DESC) as sales_rank
FROM 
    lab_sales_wf;
```

## 🚀 3. Do Zero
**Enunciado:** Escreva uma query que retorne a data da venda, o valor da venda atual e o valor da venda do dia anterior para cada vendedor, utilizando a função `LAG()`.
**Critério de Aceite:** 
1. Usar `PARTITION BY seller_id`.
2. Usar `ORDER BY sale_date`.
3. a coluna resultante deve se chamar `previous_sale_amount`.

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. `SELECT amount, SUM(amount) OVER (PARTITION BY seller_id) FROM lab_sales_wf;` $\rightarrow$ Resultado: A soma é a mesma para todas as linhas do vendedor. Por que a falta do `ORDER BY` removeu a característica de "acumulado"?
2. `SELECT amount, RANK() OVER () FROM lab_sales_wf;` $\rightarrow$ Erro esperado: **Sintaxe incorreta**. Por que o `ORDER BY` é obrigatório no `RANK()`?
3. Tente rodar essa query no MySQL 5.7 (se tiver acesso) $\rightarrow$ Erro esperado: **Sintaxe incorreta perto de 'OVER'**. Explicação: Versões antigas não suportam Window Functions.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
