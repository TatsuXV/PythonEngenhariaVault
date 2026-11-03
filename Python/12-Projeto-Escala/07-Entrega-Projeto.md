---
tipo: entrega
trilha: python
capitulo: 12
titulo: "Entrega: Pipeline de Escala Aurora"
nivel: 5
tempo_estimado_h: 12
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [entrega, projeto, big-data, multiprocessing, optimization]
---
# Entrega: Pipeline de Escala Aurora

> [!abstract] Capítulo 12 · Projeto Final de Python para Engenharia de Dados
> ⏱ 12h · 🎯 Nível 5/5 · 📦 Objetivo: Construir um pipeline resiliente e performático para processamento massivo de dados. · ✅ Verificado

## 🎯 Objetivo do Projeto
O desafio final é construir um pipeline de processamento "estável" para a Loja Aurora. Você deve processar um dataset massivo (simulado por arquivos gigantes de logs) que excede a memória RAM da máquina, transformando-o em um dataset consolidado e otimizado.

## 🛠 Requisitos do Pipeline

### 1. Ingestão Paralela e Distribuída (Extract)
- O script deve processar múltiplos arquivos CSV de logs simultaneamente utilizando `multiprocessing.Pool`.
- **Isolamento de I/O:** Cada worker deve ler seu próprio arquivo do disco para evitar o gargalo de serialização do Pickle.
- **Chunking:** Dentro de cada processo, os dados devem ser lidos em pedaços (`chunksize`) para garantir que a RAM nunca sature.

### 2. Processamento de Performance (Transform)
- **Otimização de Memória:** Implementar a redução de tipos (`float64` $\rightarrow$ `float32`, etc.) e a conversão de colunas repetitivas para `category`.
- **Agregação Local:** Cada worker deve calcular somas e contagens parciais para evitar mover milhões de linhas entre processos.
- **Filtros Vetorizados:** Toda a limpeza de dados deve ser feita via operações vetorizadas do Pandas (proibido o uso de `for` ou `.apply` em massa).

### 3. Resiliência e Carga (Load)
- **Checkpointing:** Implementar um sistema de controle de estado que salve o progresso do processamento. Se o script for interrompido, ele deve retomar do último arquivo/chunk processado.
- **Escrita Incremental:** Os resultados finais devem ser gravados em disco via `pyarrow` (Parquet) em modo append, garantindo que o resultado final não seja acumulado na RAM.
- **Consolidação Final:** Ao término, o pipeline deve gerar um relatório final com as métricas globais (Média Ponderada).

## ✅ Critérios de Aceite
- [ ] O uso de RAM deve permanecer **constante** (flat line), independentemente do número de arquivos processados.
- [ ] O script deve utilizar todos os núcleos da CPU disponíveis.
- [ ] O pipeline deve ser **idempotente** e **recuperável** (via checkpoint).
- [ ] O arquivo de saída deve estar no formato Parquet com compressão Snappy.

## 🧪 Cenário de Teste
- **Entrada:** Pasta com 50 arquivos CSV de 1GB cada.
- **Hardware:** Máquina com 8GB de RAM.
- **Validação:** O processo deve completar a execução sem disparar `MemoryError` e o valor final deve ser matematicamente idêntico ao processamento sequencial.

## 🏁 Entrega
Submeta o código fonte do pipeline (`scale_pipeline.py`), o arquivo de configuração de tipos (`types_config.json`) e um log de performance comparando o tempo de execução sequencial vs paralelo.

---
← [[Python/12-Projeto-Escala/06-Revisao]] · [[MOC-Python]] · [[Python/Simulado-Python]] →
