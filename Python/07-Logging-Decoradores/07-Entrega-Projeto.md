---
tipo: projeto
trilha: python
capitulo: 07
titulo: "Entrega: Sistema de Monitoramento de Pipeline"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, observabilidade, logging]
---
# Entrega: Sistema de Monitoramento de Pipeline

> [!abstract] Parte do Projeto Python
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/07-Logging-Decoradores/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Implementar a camada de observabilidade do pipeline de dados da Loja Aurora. O objetivo é transformar a execução do código em um processo auditável, onde cada transformação de dado seja monitorada em tempo e status, sem poluir a lógica de negócio com códigos de log.

## 🛠 Implementação
Você deve criar o arquivo `monitor.py` que implemente as seguintes funcionalidades:

1. **Configuração Centralizada:** Uma função `setup_logging(level="INFO")` que configure o logging para salvar em arquivo (`pipeline.log`) e imprimir no console, com formato: `[TIMESTAMP] [LEVEL] [MODULE] MESSAGE`.
2. **Decorador de Auditoria:** O decorador `@monitor_step` que deve:
   - Logar a entrada na função e a saída.
   - Medir o tempo de execução.
   - Capturar qualquer exceção, logá-la como `ERROR` com o traceback completo e relançar a exceção.
3. **Integração:** Aplicar o decorador `@monitor_step` nas funções da `transformations.py` (criada no Cap 05) e no `ingestor.py` (criado no Cap 06).

**Requisito Técnico:**
- Uso obrigatório de `functools.wraps`.
- Separação de logs: logs de performance em `performance.log` e logs de erro em `error.log`.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Para garantir a observabilidade do pipeline, implementei um sistema de monitoramento baseado em decoradores. Esta abordagem segue o princípio de separação de preocupações (Separation of Concerns), permitindo que a lógica de negócio permaneça limpa enquanto a infraestrutura de logs cuida da auditoria. A escolha por logs estruturados e a captura automática de stack traces via `logger.exception` reduz drasticamente o tempo médio de recuperação de falhas (MTTR), transformando o pipeline em um sistema resiliente e auditável."

## ✅ Checklist de Aceite
- [ ] O arquivo `pipeline.log` registra corretamente o início e fim de cada etapa.
- [ ] Erros em transformações são capturados com traceback completo no log.
- [ ] O tempo de execução de cada função é registrado com precisão de milissegundos.
- [ ] A função decorada mantém seu nome e docstring originais.
- [ ] O sistema de logging não trava a execução do pipeline em caso de falha na escrita do log.
