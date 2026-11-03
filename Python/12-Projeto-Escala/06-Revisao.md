---
tipo: revisao
trilha: python
capitulo: 12
titulo: "Revisão: Projeto de Escala"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [revisao, big-data, performance]
---
# Revisão: Projeto de Escala

> [!abstract] Capítulo 12 · Revisão de Engenharia de Performance
> ⏱ 1h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: Toda a trilha de Python (Cap 01-11) · 📦 Entrega: [[Python/12-Projeto-Escala/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **Memória:** Sei a diferença entre processamento In-Memory e Out-of-Core?
- [ ] **Paralelismo:** Sei quando usar `threading` (I/O) vs `multiprocessing` (CPU) e como evitar o gargalo do Pickle?
- [ ] **Otimização:** Consigo reduzir o footprint de memória de um DataFrame usando `astype` e `category`?
- [ ] **Resiliência:** Sei implementar Checkpointing para que um pipeline longo seja recuperável?
- [ ] **Estabilidade:** Consigo projetar um fluxo de dados que mantenha a RAM constante independente do volume de entrada?

## 🧠 Mapa Mental de Conceitos

**Big Data em Python $\rightarrow$**
- **Estratégia $\rightarrow$** Chunking $\rightarrow$ MapReduce Local $\rightarrow$ Generators.
- **Paralelismo $\rightarrow$** `multiprocessing.Pool` $\rightarrow$ Workers Isolados $\rightarrow$ Consolidação Final.
- **Tipagem $\rightarrow$** `float32` / `int32` $\rightarrow$ `category` $\rightarrow$ Redução de Footprint.
- **Confiabilidade $\rightarrow$** Checkpoints $\rightarrow$ Idempotência $\rightarrow$ Escrita Incremental.

**Limites do Python $\rightarrow$**
- **GIL $\rightarrow$** Bloqueio de Threads $\rightarrow$ Solução: Processos Independentes.
- **RAM $\rightarrow$** MemoryError $\rightarrow$ Solução: Processamento em Stream/Chunks.
- **Escalabilidade $\rightarrow$** Quando Pandas não basta $\rightarrow$ Polars $\rightarrow$ Dask $\rightarrow$ PySpark.

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você tem um pipeline que processa 10TB de dados em 24 horas. O sistema trava aleatoriamente na 18ª hora devido a instabilidades na rede do storage.

**Qual a arquitetura de resiliência ideal?**
1. Implementar Checkpoints a cada 1GB processado.
2. Salvar os resultados parciais em arquivos Parquet temporários.
3. Ao reiniciar, ler o arquivo de checkpoint e pular os offsets já processados.
4. Ao final, concatenar todos os arquivos Parquet temporários em um único dataset final.

## 🔗 Links Rápidos
- Aula Teórica: [[Python/12-Projeto-Escala/01-Aula]]
- Lab Prático: [[Python/12-Projeto-Escala/02-Lab]]
- Tickets de Performance: [[Python/12-Projeto-Escala/03-Tickets]]

---
← [[Python/12-Projeto-Escala/05-Flashcards]] · [[MOC-Python]] · [[Python/12-Projeto-Escala/07-Entrega-Projeto]] →
