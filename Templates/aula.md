# Template: Aula
---
tipo: aula
trilha: 
capitulo: 
titulo: ""
nivel: 
tempo_estimado_h: 
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: ""
proxima_revisao: 
tags: []
comparativo_dialecto: false
---
# {{titulo}}

> [!abstract] Capítulo {{capitulo}} · {{titulo}}
> ⏱ {{tempo}}h · 🎯 Nível {{nivel}}/5 · 🔗 Pré-requisitos: [[...]] · 📦 Entrega: [[...]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1
> ?
> [!question] Pergunta 2
> ?
> [!question] Pergunta 3
> ?

## 🎯 Objetivo
> [!goal]
> {{objetivo}}

## ⚙️ No Pipeline
> [!pipeline]
> {{onde_aparece_em_prod}}

## 📚 Teoria
{{conteudo_teorico}}

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | {{exemplo1}} | `{{pg_code}}` | `{{mysql_code}}` | {{nota}} |

## ⚠️ Armadilhas e Erros Comuns
{{armadilhas}}

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** {{erro_original}}
> **Por que está errado:** {{explicacao}}
> **Correto:** {{correcao}}

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> {{info_da_doc_oficial}}

## 📖 Fonte
Fonte: [Link da Documentação Oficial] (Versão X.X)

---
← [[anterior]] · [[MOC]] · [[próximo]] →
