# Caderno de Erros

Este arquivo centraliza a análise de falhas para transformar erros em regras de design.

## 🛠 Registro de Incidentes
(As notas de erro individuais são criadas via template e linkadas aqui)

```dataview
TABLE 
    causa as "Causa", 
    regra as "Regra de Ouro", 
    tags as "Tags"
FROM "Vault-Engenharia-de-Dados"
WHERE tipo = "erro"
SORT proxima_revisao ASC
```

## 📉 Análise de Padrões
A cada 7 dias, analise qual a tag de erro mais frequente:
- [ ] #erro/sintaxe
- [ ] #erro/logica
- [ ] #erro/performance
- [ ] #erro/tipo-dados
- [ ] #erro/null-handling
