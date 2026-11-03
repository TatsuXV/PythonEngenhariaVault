---
tipo: ticket
trilha: python
capitulo: 06
titulo: "Tickets de Arquivos e Pathlib"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, pathlib, csv, json]
---
# Tickets: Arquivos e Pathlib

> [!abstract] Capítulo 06 · Tickets de Arquivos e Pathlib
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/06-Arquivos-Pathlib/02-Lab]] · 📦 Entrega: [[Python/06-Arquivos-Pathlib/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P06-01: A Ingestão Lenta (OTIMIZAR)
**Prioridade:** Alta | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** O script de ingestão usa `f.readlines()` para ler um arquivo de logs de 2GB. O servidor está sofrendo com falta de memória (OOM Kill).
> **Entrada:** Arquivo `.txt` gigante.
> **Saída Esperada:** O script deve processar o arquivo sem carregar tudo na memória.

**✅ Critério de Aceite:** 
- [ ] Substituir `readlines()` por iteração direta `for line in f:`.
- [ ] Consumo de memória estabilizado (verificável via Task Manager/htop).

**💡 Dicas:**
> [!tip] Nível 1
> Arquivos em Python são iteráveis por natureza.
> 
> [!tip] Nível 2
> O método `.read()` e `.readlines()` carregam o conteúdo inteiro para a RAM.

**🧪 Como Verificar:** 
Rodar o script com um arquivo de teste de 1GB e monitorar o uso de RAM.

---

## 🎫 TICKET P06-02: O Caminho Quebrado (CONSERTAR)
**Prioridade:** Média | **Tipo:** Bug | **Tempo:** 45min
> **Contexto:** O pipeline funciona no Linux do desenvolvedor, mas falha no Windows do analista com `FileNotFoundError` devido às barras invertidas.
> **Entrada:** Caminhos escritos como strings: `"data/raw/file.csv"`.
> **Saída Esperada:** Código portável usando `pathlib`.

**✅ la Critério de Aceite:** 
- [ ] Substituir todas as concatenações de strings de caminhos por `Path / "subpasta"`.
- [ ] O script deve rodar em ambos os OS sem alterações.

**💡 Dicas:**
> [!tip] Nível 1
> Use `Path(__file__).parent` para criar caminhos relativos ao script.
> 
> [!tip] Nível 2
> O operador `/` da `pathlib` resolve as barras automaticamente conforme o OS.

**🧪 Como Verificar:** 
Testar a execução em ambiente Windows e Linux/macOS.

---

## 🎫 TICKET P06-03: O JSON Corrompido (INCIDENTE)
**Prioridade:** Média | **Tipo:** Incidente | **Tempo:** 60min
> **Contexto:** Um arquivo de configuração `.json` foi salvo com erro de sintaxe (vírgula sobrando no final). O pipeline trava ao tentar carregar.
> **Entrada:** Arquivo JSON inválido.
> **Saída Esperada:** Implementar um bloco `try...except` que capture `json.JSONDecodeError` e dispare um alerta claro.

**✅ Critério de Aceite:** 
- [ ] Captura específica de `JSONDecodeError`.
- [ ] Mensagem de erro informando a linha e a coluna do erro no JSON.

**💡 Dicas:**
> [!tip] Nível 1
> a exceção `JSONDecodeError` possui atributos `.lineno` e `.colno`.
> 
> [!tip] Nível 2
> Não use `except Exception`, seja específico.

**🧪 Como Verificar:** 
Criar um JSON com erro de sintaxe e rodar a função de carga.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/06-Arquivos-Pathlib/01-Aula]] ou [[Python/06-Arquivos-Pathlib/02-Lab]].
