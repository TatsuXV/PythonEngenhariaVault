---
tipo: flashcard
trilha: python
capitulo: 09
titulo: "Flashcards: Pandas & Parquet"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [flashcards, pandas, parquet]
---
# Flashcards: Pandas & Parquet

## 🧠 Conceitos
Por que o formato Parquet é considerado "colunar"?::Porque ele armazena os dados de cada coluna juntos no disco, permitindo que o sistema leia apenas as colunas necessárias para uma query, ignorando as demais.
O que é a "Vetorização" no Pandas?::É a capacidade de aplicar uma operação a toda uma coluna (Series) de uma vez, utilizando implementações de baixo nível (C/NumPy), eliminando a necessidade de loops `for` explícitos em Python.
Qual a diferença entre `.loc` e `.iloc` no Pandas?::`.loc` é baseado em **rótulos/nomes** (labels), enquanto `.iloc` é baseado em **posições inteiras** (índices numéricos).

## ⌨️ Código & Sintaxe
Como converter um DataFrame para o formato Parquet?::`df.to_parquet('arquivo.parquet')`
Como ler apenas as colunas 'A' e 'B' de um arquivo Parquet para economizar RAM?::`df = pd.read_parquet('arquivo.parquet', columns=['A', 'B'])`
Como preencher valores nulos (`NaN`) com um valor fixo no Pandas?::`df['coluna'].fillna(valor)`

## ⚠️ Erros e Correções
Erro: `SettingWithCopyWarning`. Causa?::Ocorre ao tentar alterar um DataFrame que foi criado como uma fatia (view) de outro. Correção: Usar `.copy()` ao criar a fatia ou usar `.loc` para a atribuição.
Erro: `ImportError` ao tentar usar `to_parquet`. Causa?::Falta a biblioteca de engine necessária. Correção: `pip install pyarrow` ou `pip install fastparquet`.
Erro: `MemoryError` ao ler um CSV gigante. Causa?::Tentativa de carregar todo o arquivo na RAM. Correção: Usar o parâmetro `chunksize` no `read_csv`.

## 🧩 Cloze (Preencher)
O método ==merge== do Pandas é a implementação equivalente ao JOIN do SQL, permitindo combinar dois DataFrames com base em chaves comuns?
resposta: merge
