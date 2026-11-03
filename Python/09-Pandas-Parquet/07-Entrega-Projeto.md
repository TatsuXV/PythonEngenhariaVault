---
tipo: entrega
trilha: python
capitulo: 09
titulo: "Entrega: Pipeline de Processamento Aurora"
nivel: 4
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [entrega, projeto, pandas, parquet, pipeline]
---
# Entrega: Pipeline de Processamento Aurora

> [!abstract] Capítulo 09 · Projeto de Manipulação de Dados em Escala
> ⏱ 8h · 🎯 Nível 4/5 · 📦 Objetivo: Construir um pipeline de ETL robusto usando Pandas e Parquet. · ✅ Verificado

## 🎯 Objetivo do Projeto
Você deve desenvolver um script de processamento de dados que simule a ingestão de dados da Loja Aurora. O objetivo é transformar dados brutos (CSV) em dados agregados e otimizados (Parquet), aplicando técnicas de limpeza e performance.

## 🛠 Requisitos do Pipeline

### 1. Ingestão Otimizada (Extract)
- O script deve ler arquivos CSV de vendas (`sales_raw.csv`) utilizando a técnica de **chunks** (processamento em pedaços) para evitar estouro de memória.
- Deve-se definir explicitamente os tipos de dados (`dtype`) no `read_csv` para evitar que o Pandas tente inferir tipos em arquivos gigantes.

### 2. Transformação e Limpeza (Transform)
- **Tratamento de Nulos:** Preencher valores ausentes em colunas numéricas com a média e em colunas de texto com "Desconhecido".
- **Filtro de Qualidade:** Remover registros onde o valor da venda seja negativo ou zero.
- **Feature Engineering:** Criar uma nova coluna `month_year` extraída da data da venda.
- **Enriquecimento:** Realizar um `merge` com o arquivo de produtos para adicionar a categoria de cada venda.

### 3. Agregação e Carga (Load)
- Calcular a **Receita Total por Categoria** e por **Mês/Ano**.
- Salvar o resultado final em um arquivo **Parquet** utilizando compressão `snappy`.
- Gerar um relatório simples no console com o top 3 categorias que mais venderam.

## ✅ Critérios de Aceite
- [ ] O código deve processar arquivos simuladamente grandes sem ultrapassar 2GB de RAM.
- [ ] O arquivo de saída deve estar rigorosamente no formato Parquet.
- [ ] O pipeline deve ser idempotente (se rodar duas vezes, o resultado final é o mesmo).
- [ ] O uso de `.apply()` deve ser evitado em favor de operações vetorizadas.

## 🧪 Cenário de Teste
- Entrada: `sales_raw.csv` (1M de linhas) e `products.csv` (1k linhas).
- Saída: `sales_summary.parquet`.
- Validação: O valor total de vendas no Parquet deve coincidir com a soma do CSV original (descontando os nulos/negativos).

## 🏁 Entrega
Submeta o código fonte do pipeline (`etl_aurora.py`) e um breve README explicando as decisões de performance tomadas (ex: por que escolheu tal `chunksize`).

---
← [[Python/09-Pandas-Parquet/06-Revisao]] · [[MOC-Python]] · [[Python/10-SQLAlchemy-Sessoes/01-Aula]] →
