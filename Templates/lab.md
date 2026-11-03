# Template: Lab
---
tipo: lab
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
# Lab: {{titulo}}

> [!abstract] Capítulo {{capitulo}} · {{titulo}}
> ⏱ {{tempo}}h · 🎯 Nível {{nivel}}/5 · 🔗 Pré-requisitos: [[...]] · 📦 Entrega: [[...]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
{{sql_setup_create_and_insert}}
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado
> > [!success] Resposta
> > {{resposta_predicao}}
> > **Explicação:** {{explicacao}}

```{{linguagem}}
{{codigo_completo}}
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

```{{linguagem}}
{{codigo_com_lacunas}}
```

**Como verificar:** `{{comando_teste}}`

## 🚀 3. Do Zero
**Enunciado:** {{enunciado}}
**Critério de Aceite:** {{criterio}}

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. {{mutacao1}} $\rightarrow$ Erro esperado: {{erro1}}
2. {{mutacao2}} $\rightarrow$ Erro esperado: {{erro2}}
3. {{mutacao3}} $\rightarrow$ Erro esperado: {{erro3}}

---
← [[anterior]] · [[MOC]] · [[próximo]] →
