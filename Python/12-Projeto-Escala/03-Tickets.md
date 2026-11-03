---
tipo: ticket
trilha: python
capitulo: 12
titulo: "Tickets de Escala e Performance"
nivel: 5
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-15
tags: [ticket, big-data, multiprocessing, optimization]
---
# Tickets: Escala e Performance

> [!abstract] Capítulo 12 · Tickets de Escala e Performance
> ⏱ 2h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Python/12-Projeto-Escala/02-Lab]] · 📦 Entrega: [[Python/12-Projeto-Escala/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P12-01: O Gargalo do Pickle (OTIMIZAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O pipeline paralelo está lento. O desenvolvedor está enviando o DataFrame completo para as funções worker via `Pool.map`. O log mostra que a CPU gasta 80% do tempo em "Pickling" e apenas 20% calculando.
> **Entrada:** `pool.map(process_df, [df1, df2, df3])`.
> **Saída Esperada:** Refatoração para passar apenas os caminhos dos arquivos.

**✅ Critério de Aceite:**
- [ ] Alterar a função worker para receber `file_path` em vez de `df`.
- [ ] Mover a leitura do CSV (`pd.read_csv`) para dentro da função worker.
- [ ] Reduzir o tempo de inicialização dos processos.

**💡 Dicas:**
> [!tip] Nível 1
> O multiprocessing do Python usa o protocolo Pickle para mover dados entre processos. Serializar um DataFrame gigante é extremamente caro.
> 
> [!tip] Nível 2
> Ler o dado localmente em cada processo é a maneira mais eficiente de distribuir a carga de I/O.

**🧪 Como Verificar:**
Comparar o tempo de execução do script antes e depois da mudança; a versão com caminhos deve ser drasticamente mais rápida.

---

## 🎫 TICKET P12-02: A Morte por OOM (DEBUG)
**Prioridade:** Média | **Tipo:** Stability | **Tempo:** 60min
> **Contexto:** O script de processamento roda bem por 2 horas, mas depois trava com `MemoryError`. Ao analisar, percebeu-se que a lista `all_results = []` cresce a cada chunk processado até estourar a RAM.
> **Entrada:** Acúmulo de resultados em lista na memória.
> **Saída Esperada:** Implementação de escrita incremental em disco.

**✅ Critério de Aceite:**
- [ ] Substituir a lista de resultados por um arquivo de saída (CSV ou Parquet).
- [ ] Implementar a escrita em modo `append` para cada chunk processado.
- [ ] O uso de RAM deve permanecer constante (flat line) durante todo o processamento.

**💡 Dicas:**
> [!tip] Nível 1
> Nunca acumule resultados de Big Data em memória. O resultado final deve ser um fluxo que vai para o disco.
> 
> [!tip] Nível 2
> Para arquivos Parquet, use a biblioteca `pyarrow.parquet.ParquetWriter` para fazer append de row groups.

**🧪 Como Verificar:**
Monitorar a RAM com `htop` ou Gerenciador de Tarefas; a curva de memória não deve ser ascendente.

---

## 🎫 TICKET P12-03: O Desafio da Idempotência (ESCREVER)
**Prioridade:** Baixa | **Tipo:** Reliability | **Tempo:** 30min
> **Contexto:** Se o pipeline de 1 bilhão de linhas cair no meio, o desenvolvedor precisa reiniciar do zero, perdendo 5 horas de processamento.
> **Entrada:** Pipeline sem controle de estado.
> **Saída Esperada:** Implementação de Checkpointing.

**✅ Critério de Aceite:**
- [ ] Criar um arquivo de log `checkpoint.txt` que salve o último índice de chunk processado com sucesso.
- [ ] Ao iniciar, o script deve ler esse arquivo e pular os chunks já processados.
- [ ] O sistema deve ser capaz de retomar a execução exatamente de onde parou.

**💡 Dicas:**
> [!tip] Nível 1
> Checkpointing é essencial para pipelines de produção. Use um arquivo simples ou uma tabela no banco de dados para salvar o estado.
> 
> [!tip] Nível 2
> Garanta que a escrita do checkpoint ocorra apenas APÓS o commit do dado no destino.

**🧪 Como Verificar:**
Interromper o script forçadamente (Ctrl+C) no meio do processamento e reiniciá-lo; ele deve pular os dados já processados.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/12-Projeto-Escala/01-Aula]] ou [[Python/12-Projeto-Escala/02-Lab]].
