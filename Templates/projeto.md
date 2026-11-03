# Template: Projeto
---
tipo: projeto
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
---
# Projeto: {{titulo}}

> [!abstract] Parte do Projeto {{trilha}}
> ⏱ {{tempo}}h · 🎯 Nível {{nivel}}/5 · 🔗 Pré-requisitos: [[...]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> {{objetivo}}

## 🛠 Implementação
{{descricao_do_que_deve_ser_feito}}

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> {{espaco_para_texto}}

## ✅ Checklist de Aceite
- [ ] {{critério1}}
- [ ] {{critério2}}
- [ ] Testes passam (`pytest` ou `verificar.sql`)
- [ ] Logging implementado
- [ ] Sem segredos no código (`.env` usado)
