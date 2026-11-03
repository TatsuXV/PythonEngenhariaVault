---
tipo: flashcard
trilha: python
capitulo: 12
titulo: "Flashcards: Projeto de Escala"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [flashcards, big-data, multiprocessing]
---
# Flashcards: Projeto de Escala

## 🧠 Conceitos
O que é processamento Out-of-Core?::É a técnica de processar dados que não cabem na memória RAM, lendo-os do disco em fragmentos (chunks) e processando-os sequencialmente ou em paralelo.
Por que o `multiprocessing` é preferível ao `threading` para cálculos pesados em Python?::Devido ao GIL (Global Interpreter Lock), que impede threads de executarem código Python em núcleos diferentes. Processos independentes possuem seu próprio GIL e memória.
Qual a vantagem de converter colunas de texto repetitivas para o tipo `category` no Pandas?::Reduz drasticamente o uso de memória, pois armazena a string única apenas uma vez e usa inteiros para referenciá-la nas linhas.

## ⌨️ Código & Sintaxe
Como implementar a leitura de um arquivo CSV em pedaços no Pandas?::`for chunk in pd.read_csv('file.csv', chunksize=100000):`
Qual a função do `asyncio.gather()` em pipelines de I/O?::Dispara múltiplas tarefas assíncronas simultaneamente e aguarda a conclusão de todas, retornando os resultados em uma lista.
Como forçar a liberação de memória de um objeto grande no Python?::Utilizando `del objeto` seguido de `gc.collect()` da biblioteca `gc`.

## ⚠️ Erros e Correções
Erro: `MemoryError` ao processar Big Data. Causa?::Tentativa de carregar o dataset inteiro na RAM. Correção: Implementar Chunking ou usar bibliotecas como Polars/PySpark.
Erro: Lentidão extrema ao usar `Pool.map` com DataFrames. Causa?::Overhead de serialização (Pickle) ao mover objetos pesados entre processos. Correção: Passar apenas o caminho do arquivo para o worker.
Erro: Pipeline que reinicia do zero após cada falha. Causa?::Falta de controle de estado. Correção: Implementar Checkpointing salvando o progresso em arquivo ou banco.

## 🧩 Cloze (Preencher)
A técnica de ==Vetorização== permite que o Pandas realize operações em colunas inteiras utilizando implementações em C, eliminando a necessidade de loops `for` lentos em Python?
resposta: Vetorização
