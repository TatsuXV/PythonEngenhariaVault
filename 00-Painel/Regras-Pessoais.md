# Regras Pessoais (Checklist Pré-Commit)

Regras derivadas do Caderno de Erros. Estas regras devem ser verificadas antes de considerar qualquer ticket como "concluído".

## 🐍 Python
- [ ] **Type Hints:** Todas as funções possuem tipos de entrada e saída definidos.
- [ ] **Pathlib:** Não use strings para caminhos de arquivo; use `pathlib.Path`.
- [ ] **Logging:** Nenhum `print()` no código final; use `logging.info()` ou `logger.error()`.
- [ ] **SQLAlchemy 2.0:** Use `select()` em vez de `.query()`.
- [ ] **Env Vars:** Credenciais estão no `.env`, nunca hardcoded.

## 🐘 SQL
- [ ] **Sargability:** Filtros `WHERE` não aplicam funções a colunas indexadas (Ex: use `col >= '2023-01-01'` em vez de `YEAR(col) = 2023`).
- [ ] **Order By:** Toda consulta com `LIMIT` possui um `ORDER BY` explícito.
- [ ] **Numeric:** Dinheiro sempre usa `NUMERIC(10,2)`, nunca `FLOAT` ou `REAL`.
- [ ] **Explain:** Consultas complexas foram validadas com `EXPLAIN ANALYZE`.

## 🏗 Engenharia de Dados
- [ ] **Idempotência:** O pipeline pode rodar 10 vezes e o resultado final será o mesmo.
- [ ] **Bronze $\rightarrow$ Silver $\rightarrow$ Gold:** Dados brutos nunca são deletados; transformações são rastreáveis.
