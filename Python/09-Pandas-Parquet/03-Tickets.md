---
tipo: ticket
trilha: python
capitulo: 09
titulo: "Tickets de Pandas & Parquet"
nivel: 4
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-01
tags: [ticket, pandas, parquet, optimization]
---
# Tickets: Pandas & Parquet

> [!abstract] Capítulo 09 · Tickets de Pandas & Parquet
> ⏱ 2h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[Python/09-Pandas-Parquet/02-Lab]] · 📦 Entrega: [[Python/09-Pandas-Parquet/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P09-01: A Armadilha do `.apply()` (REFATORAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O pipeline de precificação está lento. O desenvolvedor anterior usou um `.apply(lambda x: x * 1.1)` para aplicar um aumento de 10% em todos os preços de 5 milhões de linhas.
> **Entrada:** DataFrame com coluna `price`.
> **Saída Esperada:** Refatoração para operação vetorizada.

**✅ Critério de Aceite:**
- [ ] Substituir o `.apply()` por operação aritmética direta (`df['price'] * 1.1`).
- [ ] Comparar o tempo de execução (usando a biblioteca `time`) e documentar a diferença.
- [ ] O resultado final deve ser idêntico ao anterior.

**💡 Dicas:**
> [!tip] Nível 1
> Operações vetorizadas do Pandas são implementadas em C e processam a coluna inteira de uma vez.
> 
> [!tip] Nível 2
> Meça o tempo usando `%%timeit` no Jupyter ou `time.time()` em scripts.

**🧪 Como Verificar:**
O código refatorado deve ser ordens de magnitude mais rápido que o original.

---

## 🎫 TICKET P09-02: O Mistério do Memory Leak (REVISAR)
**Prioridade:** Média | **Tipo:** Debug | **Tempo:** 60min
> **Contexto:** O script de processamento está estourando a RAM (OOM - Out of Memory). Ele lê um CSV de 10GB em um servidor com 8GB de RAM.
> **Entrada:** `pd.read_csv('large_data.csv')`.
> **Saída Esperada:** Implementação de processamento em pedaços (`chunks`).

**✅ Critério de Aceite:**
- [ ] Implementar o parâmetro `chunksize` no `read_csv`.
- [ ] Processar cada pedaço (chunk) individualmente e salvar os resultados parciais.
- [ ] O uso de RAM deve permanecer constante, independentemente do tamanho do arquivo.

**💡 Dicas:**
> [!tip] Nível 1
> O `chunksize` retorna um iterador. Você deve fazer um loop `for chunk in reader:` para processar os dados.
> 
> [!tip] Nível 2
> Para salvar os chunks em Parquet, use o modo `append` ou salve arquivos numerados.

**🧪 Como Verificar:**
Monitorar o Gerenciador de Tarefas/htop durante a execução; a RAM não deve subir linearmente com o tamanho do arquivo.

---

## 🎫 TICKET P09-03: A Migração para Colunar (ESCREVER)
**Prioridade:** Baixa | **Tipo:** Infra/Storage | **Tempo:** 30min
> **Contexto:** A equipe de Analytics reclama que as queries no CSV são lentas. Você deve migrar os dados brutos para Parquet.
> **Entrada:** Pasta com 12 arquivos CSV (um por mês).
> **Saída Esperada:** Um único arquivo Parquet consolidado.

**✅ Critério de Aceite:**
- [ ] Ler todos os CSVs da pasta usando `glob`.
- [ ] Concatenar os DataFrames em um único.
- [ ] Exportar para Parquet usando compressão `snappy`.
- [ ] Comparar o tamanho do arquivo final (CSV total vs Parquet).

**💡 Dicas:**
> [!tip] Nível 1
> Use `pd.concat([list_of_dfs])` para unir os arquivos.
> 
> [!tip] Nível 2
> A compressão Snappy é o padrão da indústria por equilibrar velocidade e tamanho.

**🧪 Como Verificar:**
O arquivo Parquet deve ser significativamente menor que a soma dos CSVs.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/09-Pandas-Parquet/01-Aula]] ou [[Python/09-Pandas-Parquet/02-Lab]].
