---
tipo: aula
trilha: python
capitulo: 12
titulo: "Projeto de Escala: Processando 1 Bilhão de Linhas"
nivel: 5
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [big-data, performance, optimization, memory-management, python-scale]
---
# Projeto de Escala: Processando 1 Bilhão de Linhas

> [!abstract] Capítulo 12 · Projeto de Escala: Processando 1 Bilhão de Linhas
> ⏱ 8h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: Toda a trilha de Python (Cap 01-11) · 📦 Entrega: [[Python/12-Projeto-Escala/07-Entrega-Projeto|Pipeline de Escala Aurora]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença entre processamento "In-Memory" e processamento "Out-of-Core"?
> ?
> [!question] Por que o uso de `multiprocessing` é preferível ao `threading` para tarefas de CPU-bound em Python?
> ?
> [!question] O que é o GIL (Global Interpreter Lock) e como ele afeta o processamento de grandes volumes de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Projetar e implementar um pipeline de dados capaz de processar volumes de dados que excedem a memória RAM disponível, utilizando técnicas de paralelismo, fragmentação (chunking) e otimização de tipos de dados.

## ⚙️ No Pipeline
> [!pipeline]
> No mundo real, você não encontrará datasets que cabem perfeitamente no seu notebook. O desafio do Engenheiro de Dados é criar sistemas **estáveis** e **previsíveis**. Processar 1 bilhão de linhas exige que você pare de pensar em "objetos" e comece a pensar em "fluxos" (streams). O objetivo não é a velocidade máxima, mas a **estabilidade**: o pipeline não pode travar por `OutOfMemory` (OOM), independentemente do tamanho do arquivo.

## 📚 Teoria

### 1. Estratégias de Processamento Out-of-Core
Quando os dados não cabem na RAM, usamos a estratégia de **Dividir e Conquistar**:
- **Chunking:** Ler o arquivo em pedaços fixos (ex: 100k linhas).
- **MapReduce Local:** Processar cada pedaço independentemente (Map) e depois consolidar os resultados (Reduce).
- **Generator Pipelines:** Usar `yield` para criar fluxos de dados, evitando carregar a lista completa na memória.

### 2. Paralelismo: Multiprocessing vs Threading
Python tem o GIL, que impede que múltiplas threads executem código Python simultaneamente em núcleos diferentes.
- **Threading:** Ideal para I/O-bound (esperar API, ler disco).
- **Multiprocessing:** Cria processos independentes, cada um com seu próprio GIL e memória. Essencial para cálculos pesados (CPU-bound) em DataFrames.

### 3. Otimização de Tipos (Memory Footprint)
Reduzir o tamanho dos tipos de dados pode diminuir o consumo de RAM em até 70%.
- `float64` $\rightarrow$ `float32`
- `int64` $\rightarrow$ `int32` ou `int16`
- `object` (strings) $\rightarrow$ `category` (para colunas com baixa cardinalidade).

### 4. Checkpointing e Idempotência
Em processamentos longos, falhas são inevitáveis. 
- **Checkpointing:** Salvar o progresso a cada X chunks. Se o script cair, ele recomeça do último checkpoint.
- **Idempotência:** Garantir que processar o mesmo dado duas vezes não duplique os resultados no banco de dados.

## ⚠️ Armadilhas e Erros Comuns
- **Acumular Resultados na RAM:** Fazer um `results.append(chunk_result)` dentro de um loop de 1 bilhão de linhas. O resultado final também deve ser escrito em disco/banco.
- **Overhead de Processos:** Criar 100 processos em uma máquina de 8 núcleos. O custo de alternância de contexto (context switch) torna o código mais lento que o sequencial.
- **Ignorar o Garbage Collector:** Manter referências a objetos grandes que não são mais necessários. Use `del df` e `gc.collect()`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `multiprocessing.Pool` para processar qualquer tarefa em paralelo."
> **Por que está errado:** Passar DataFrames gigantes entre processos via `Pool` gera um overhead imenso de serialização (Pickle).
> **Correto:** Passe apenas os **caminhos dos arquivos** ou **índices de linhas** para os processos; deixe que cada processo leia sua própria fatia de dados do disco.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Além do Pandas:** Quando o processamento em Python puro atinge o limite, migramos para:
> - **Polars:** Escrito em Rust, multithreaded nativamente e muito mais rápido que Pandas.
> - **PySpark:** Processamento distribuído em clusters (o padrão para Big Data).
> - **Dask:** Paraleliza DataFrames do Pandas em escala.

## 📖 Fonte
Fonte: [Python Multiprocessing Docs](https://docs.python.org/3/library/multiprocessing.html) e [Pandas Scaling Guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/scaling.html)

---
← [[Python/11-APIs-REST-CRUD/01-Aula]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/02-Lab]] →
