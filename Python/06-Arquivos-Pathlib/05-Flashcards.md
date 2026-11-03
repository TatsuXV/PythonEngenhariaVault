---
tipo: flashcard
trilha: python
capitulo: 06
titulo: "Flashcards: Arquivos e Pathlib"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [flashcards, pathlib, csv, json]
---
# Flashcards: Arquivos e Pathlib

## 🧠 Conceitos
Qual a principal vantagem de usar `pathlib.Path` em vez de `os.path`?::A `pathlib` trata caminhos como objetos e utiliza o operador `/` para junções, tornando o código portável entre Windows e Linux sem a necessidade de tratar barras manualmente.
Por que devemos usar `with open(...)` em vez de apenas `open().close()`?::O `with` garante o fechamento do arquivo mesmo que ocorra uma exceção durante a leitura/escrita, evitando o vazamento de descritores de arquivo.
O que é o processamento em streaming de arquivos?::É a prática de ler um arquivo linha por linha (ou em chunks) em vez de carregar todo o conteúdo na memória RAM, essencial para arquivos de escala Gigabyte/Terabyte.

## ⌨️ Código & Sintaxe
Como criar uma pasta recursivamente com `pathlib`?::`Path("caminho/da/pasta").mkdir(parents=True, exist_ok=True)`
Como ler um CSV como se fosse um dicionário?::Usando `csv.DictReader(arquivo)`.
Como converter um dicionário Python para uma string JSON formatada?::`json.dumps(dicionario, indent=4)`.

## ⚠️ Erros e Correções
Erro: `UnicodeDecodeError: 'charmap' codec can't decode byte...`. Causa?::Tentar ler um arquivo UTF-8 usando a codificação padrão do Windows (cp1252). Correção: Especificar `encoding="utf-8"` no `open()`.
Erro: `FileNotFoundError` ao tentar escrever em `/output/data.csv` quando a pasta `output` não existe. Correção?::Criar a pasta antes com `Path("output").mkdir(exist_ok=True)`.

## 🧩 Cloze (Preencher)
O método ==.glob()== da pathlib permite buscar arquivos que correspondam a um padrão específico, como "*.csv", retornando um gerador?
resposta: .glob()
