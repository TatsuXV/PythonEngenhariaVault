---
tipo: revisao
trilha: python
capitulo: 06
titulo: "Revisão: Arquivos e Pathlib"
nivel: 3
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [revisao, pathlib, csv, json]
---
# Revisão: Arquivos e Pathlib

## ⚪ Folha em Branco
**Desafio:** Escreva um script que:
1. Localize todos os arquivos `.json` em uma pasta `input/`.
2. Leia cada JSON (que contém uma lista de vendas).
3. Extraia apenas os valores de venda e salve a soma total em um arquivo `total.txt`.
4. Use `pathlib` para tudo.

> [!success] Comparação
> ```python
> from pathlib import Path
> import json
> 
> base = Path("input")
> total = 0.0
> 
> for file in base.glob("*.json"):
>     with open(file, "r", encoding="utf-8") as f:
>         data = json.load(f)
>         total += sum(item["valor"] for item in data)
> 
> Path("total.txt").write_text(str(total), encoding="utf-8")
> ```

## 🗣 Explique ao Júnior
Explique por que carregar um arquivo de 10GB com `.read()` é um erro fatal e qual a alternativa correta.
> [!tip] Resposta Sugerida
> "O `.read()` tenta colocar todo o conteúdo do arquivo na memória RAM de uma vez. Se o arquivo tem 10GB e seu servidor tem 8GB, o sistema operacional matará seu processo por falta de memória (OOM). A alternativa correta é iterar sobre o arquivo: `for line in file:`. Assim, o Python carrega apenas uma linha por vez, mantendo o uso de memória baixo e constante, não importa se o arquivo tem 1MB ou 1TB."

## 📅 Agenda de Fixação
- [ ] D1: [[Python/06-Arquivos-Pathlib/05-Flashcards]] - 2026-11-03
- [ ] D3: [[Python/06-Arquivos-Pathlib/05-Flashcards]] - 2026-11-05
- [ ] D7: [[Python/06-Arquivos-Pathlib/05-Flashcards]] - 2026-11-09

## 🔄 Intercalação
1. **Funções:** O que é uma função pura e por que ela é importante para arquivos?
2. **Coleções:** Como converter uma lista de IDs extraídos de um CSV para remover duplicatas?
3. **Tipos:** Como tratar um erro de `json.JSONDecodeError` ao ler um config?

## 📈 Checklist de Domínio
- [ ] 0: Vi o conteúdo.
- [ ] 1: Pratiquei e resolvi os tickets.
- [ ] 2: Dominei (manipulo caminhos e arquivos sem erro de encoding).
- [ ] 3: Consegui explicar a diferença entre streaming e loading para alguém.

## 📓 Registro de Erros
Sintoma: `PermissionError: [Errno 13] Permission denied: 'data/raw'`.
Causa: Tentar abrir um diretório como se fosse um arquivo (`open()`).
Regra: Verificar `if path.is_file()` antes de abrir.
Tag: #erro/arquivos
