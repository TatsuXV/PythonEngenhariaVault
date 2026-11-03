---
tipo: projeto
trilha: python
capitulo: 06
titulo: "Entrega: Ingestor de Dados Brutos"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, ingestao, pathlib]
---
# Entrega: Ingestor de Dados Brutos

> [!abstract] Parte do Projeto Python
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/06-Arquivos-Pathlib/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Construir a primeira etapa do pipeline de dados: o Ingestor. Ele deve ser capaz de ler múltiplos arquivos de fontes diferentes (CSV e JSON), validar a existência dos caminhos e salvar os dados em um formato unificado para a próxima etapa.

## 🛠 Implementação
Crie o arquivo `ingestor.py` com a seguinte lógica:
1. **Scanner de Pasta:** Uma função que use `pathlib` para encontrar todos os arquivos `.csv` e `.json` em uma pasta de entrada.
2. **Leitor Genérico:** Uma função que identifique a extensão do arquivo e use a biblioteca correta (`csv` ou `json`) para extrair os dados como uma lista de dicionários.
3. **Unificador:** O script deve ler todos os arquivos encontrados e consolidar os dados em uma única lista global.
4. **Salvamento:** Salvar o resultado final em um arquivo `raw_data_consolidated.jsonl` (uma linha por registro) para garantir a escalabilidade.

**Requisitos Técnicos:**
- Uso obrigatório de `with open(..., encoding="utf-8")`.
- Tratamento de erro para arquivos corrompidos (não travar o script, apenas logar o erro e pular o arquivo).
- Caminhos relativos via `Path(__file__).parent`.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Desenvolvi um módulo de ingestão de dados portável e resiliente, utilizando a biblioteca `pathlib` para abstrair as diferenças de sistema operacional. A decisão de implementar a leitura via streaming e a exportação no formato JSONL (JSON Lines) foi tomada para garantir a escalabilidade do pipeline, evitando gargalos de memória ao lidar com arquivos de grande porte. Além disso, a implementação de tratamentos de exceção específicos para cada formato de arquivo assegura que a falha em um único arquivo de origem não interrompa a ingestão de todo o dataset."

## ✅ Checklist de Aceite
- [ ] O script detecta arquivos CSV e JSON automaticamente.
- [ ] O arquivo final `raw_data_consolidated.jsonl` é gerado corretamente.
- [ ] O script roda sem erros no Windows e no Linux.
- [ ] Arquivos com erro de sintaxe são ignorados com log de aviso.
- [ ] O uso de memória permanece baixo durante a execução.
