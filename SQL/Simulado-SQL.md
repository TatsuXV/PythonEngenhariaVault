# 📝 Simulado Final de SQL (MySQL 8.x)

Este simulado foi desenhado para testar seu conhecimento em todos os níveis: do básico ao arquitetural. Tente resolver cada questão sem consultar as aulas.

---

## 🟢 Nível 1: Fundamentos (Júnior)
**Questão 1:** Você tem uma tabela `vendas` com as colunas `id`, `valor`, `data` e `cliente_id`. Escreva uma query que retorne o total de vendas por cliente, mas apenas para clientes que gastaram mais de 1000.00 no total.

**Questão 2:** Qual a diferença entre `INNER JOIN` e `LEFT JOIN`? Dê um exemplo de cenário onde o `LEFT JOIN` é a única opção correta.

**Questão 3:** O que acontece se você executar um `DELETE` sem a cláusula `WHERE`?

---

## 🟡 Nível 2: Analítico (Pleno)
**Questão 4:** Utilizando a tabela `vendas`, escreva uma query que retorne:
- O ID do pedido.
- O valor da venda.
- A soma acumulada de vendas para aquele cliente ao longo do tempo (Running Total).

**Questão 5:** Você precisa criar um relatório que mostre a venda do dia atual e a venda do dia anterior na mesma linha. Qual função de Window você utilizaria e como seria a sintaxe?

**Questão 6:** Refatore a seguinte query para usar uma CTE:
`SELECT * FROM (SELECT cliente_id, SUM(valor) as total FROM vendas GROUP BY cliente_id) as t WHERE t.total > 500;`

---

## 🔴 Nível 3: Performance e Arquitetura (Sênior/DE)
**Questão 7:** Você roda um `EXPLAIN` em uma query e vê `type: ALL` e `Using filesort`. O que isso significa tecnicamente e quais as duas ações principais para resolver isso?

**Questão 8:** Explique a regra do "Prefixo à Esquerda" em índices compostos. Se você tem um índice em `(Cidade, Estado, CEP)`, a query `WHERE Estado = 'SP'` usará o índice? Por quê?

**Questão 9:** Você tem uma tabela de logs com 1 bilhão de linhas. A empresa quer deletar dados de 2021. Por que usar `DELETE FROM logs WHERE ano = 2021` é uma má ideia e qual a alternativa usando Particionamento?

**Questão 10:** Desenhe a lógica (ou escreva a query) para transformar uma tabela "Flat" (com nome, email, produto e preço na mesma linha) em um modelo Star Schema (Tabelas de Dimensão e Fato).

---

## 🏁 Gabarito Rápido (Para Conferência)
1. `SELECT cliente_id, SUM(valor) FROM vendas GROUP BY cliente_id HAVING SUM(valor) > 1000;`
2. `INNER` pega intersecção; `LEFT` pega tudo da esquerda + correspondentes da direita. Ex: Listar todos os clientes, mesmo os que nunca compraram.
3. Apaga todos os registros da tabela.
4. `SUM(valor) OVER (PARTITION BY cliente_id ORDER BY data)`.
5. `LAG(valor) OVER (PARTITION BY cliente_id ORDER BY data)`.
6. `WITH total_vendas AS (SELECT cliente_id, SUM(valor) as total FROM vendas GROUP BY cliente_id) SELECT * FROM total_vendas WHERE total > 500;`
7. `ALL` = Full Table Scan; `filesort` = ordenação em disco. Solução: Criar índices adequados.
8. Não usa. O índice começa por Cidade. Para usar, precisa filtrar pela primeira coluna do índice.
9. `DELETE` gera logs massivos de undo. `DROP PARTITION` é instantâneo.
10. Processo: `SELECT DISTINCT` para Dimensões $\rightarrow$ `JOIN` para pegar IDs $\rightarrow$ `INSERT` na Fato.
