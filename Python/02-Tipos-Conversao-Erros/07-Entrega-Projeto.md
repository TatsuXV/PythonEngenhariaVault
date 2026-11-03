---
tipo: projeto
trilha: python
capitulo: 02
titulo: "Entrega: Validador de Tipos de Dados"
nivel: 1
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, validacao, casting]
---
# Entrega: Validador de Tipos de Dados

> [!abstract] Parte do Projeto Python
> ⏱ 1h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/02-Tipos-Conversao-Erros/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Construir um módulo de validação de tipos que servirá como a primeira camada de "limpeza" (Silver layer) do pipeline de dados da Loja Aurora.

## 🛠 Implementação
Crie um arquivo `validators.py` contendo as seguintes funções:
1. `to_float_safe(value, default=0.0)`: Converte para float, tratando vírgulas e retornando o default em caso de erro.
2. `to_int_safe(value, default=0)`: Converte para int, tratando floats intermediários e retornando o default em caso de erro.
3. `to_bool_safe(value, default=False)`: Converte strings como "Yes", "True", "1" para `True` e as demais para `False`.

**Requisito Técnico:** Todas as funções devem usar `logging` para reportar valores que dispararam o valor default.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Implementei um módulo de validação de tipos robusto para garantir a integridade dos dados na fase de ingestão. A decisão de utilizar casting seguro com valores de imputação (defaults) em vez de interromper a execução do pipeline permite que o processamento de milhões de registros continue mesmo diante de anomalias pontuais, enquanto o sistema de logging fornece a rastreabilidade necessária para auditoria de qualidade de dados."

## ✅ Checklist de Aceite
- [ ] As funções não levantam exceções não tratadas.
- [ ] Strings com vírgula são convertidas corretamente.
- [ ] `None` é tratado sem causar `TypeError`.
- [ ] Logs de warning são gerados para cada falha de conversão.
- [ ] O módulo foi testado com a lista de entrada: `["10.5", "20,00", "ABC", None]`.
