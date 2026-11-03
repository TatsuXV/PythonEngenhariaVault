---
tipo: revisao
trilha: python
capitulo: 09
titulo: "Revisão: Pandas & Parquet"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [revisao, pandas, parquet]
---
# Revisão: Pandas & Parquet

> [!abstract] Capítulo 09 · Revisão de Processamento de Dados
> ⏱ 1h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/09-Pandas-Parquet/01-Aula]] · 📦 Entrega: [[Python/09-Pandas-Parquet/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **DataFrames:** Sei filtrar, selecionar e agregar dados usando `.loc`, `.iloc` e `.groupby`?
- [ ] **Performance:** Entendo por que a vetorização é superior ao loop `for` e sei evitar o `.apply()` para operações simples?
- [ ] **Storage:** Sei a diferença entre CSV e Parquet e por que o Parquet é preferível em Data Lakes?
- [ ] **Memória:** Sei processar arquivos maiores que a minha RAM utilizando `chunksize`?
- [ ] **Limpeza:** Consigo tratar valores ausentes (`NaN`) usando `fillna` ou `dropna`?

## 🧠 Mapa Mental de Conceitos

**Pandas $\rightarrow$**
- **Estrutura $\rightarrow$** `DataFrame` (Tabela) $\rightarrow$ `Series` (Coluna).
- **Manipulação $\rightarrow$** Filtros $\rightarrow$ Agregações $\rightarrow$ Merges (SQL Join).
- **Performance $\rightarrow$** Vetorização (NumPy) $\rightarrow$ Evitar Loops $\rightarrow$ Evitar `.apply()`.
- **Escala $\rightarrow$** `chunksize` $\rightarrow$ Processamento em Batch.

**Parquet $\rightarrow$**
- **Formato $\rightarrow$** Binário Colunar.
- **Vantagens $\rightarrow$** Compressão $\rightarrow$ Tipagem preservada $\rightarrow$ Pushdown de colunas (leitura parcial).

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você tem um dataset de 50GB de logs de vendas em CSV. Você precisa calcular a receita total por categoria de produto e salvar em um arquivo final. Seu servidor tem apenas 16GB de RAM.

**Qual o workflow ideal?**
1. Usar `pd.read_csv` com `chunksize`.
2. Para cada chunk, filtrar as colunas necessárias (categoria, valor).
3. Fazer uma soma parcial por categoria em cada chunk.
4. Acumular esses resultados em um DataFrame pequeno de resumo.
5. Salvar o resumo final em Parquet.

## 🔗 Links Rápidos
- Aula Teórica: [[Python/09-Pandas-Parquet/01-Aula]]
- Lab Prático: [[Python/09-Pandas-Parquet/02-Lab]]
- Tickets de Performance: [[Python/09-Pandas-Parquet/03-Tickets]]

---
← [[Python/09-Pandas-Parquet/05-Flashcards]] · [[MOC-Python]] · [[Python/09-Pandas-Parquet/07-Entrega-Projeto]] →
