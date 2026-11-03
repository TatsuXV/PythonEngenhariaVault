# Dashboard de Progresso - Engenharia de Dados

Este dashboard utiliza Dataview para monitorar a evolução do aprendizado.

## 🚩 Revisões Vencidas (Spaced Repetition)
```dataview
LIST FROM #flashcards
WHERE proxima_revisao <= date(today)
SORT proxima_revisao ASC
```

## 📊 Progresso por Trilha
```dataview
TABLE 
    status as Status, 
    dominio as Domínio, 
    tempo_estimado_h as "Hrs Est.",
    verificado as Verificado
FROM "Vault-Engenharia-de-Dados"
WHERE tipo = "aula"
SORT trilha ASC, capitulo ASC
```

## ⚠️ Conteúdo Não Verificado
```dataview
LIST FROM "Vault-Engenharia-de-Dados"
WHERE verificado = false
```

## 🐛 Erros Recorrentes (Caderno de Erros)
```dataview
TABLE 
    tags as Categorias, 
    causa as "Causa Raiz"
FROM "Vault-Engenharia-de-Dados/00-Painel/Caderno-de-Erros"
SORT proxima_revisao ASC
```
