---
tipo: projeto
trilha: python
capitulo: 03
titulo: "Entrega: Motor de Filtragem de Eventos"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, filtragem, performance]
---
# Entrega: Motor de Filtragem de Eventos

> [!abstract] Parte do Projeto Python
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/03-Controle-Fluxo/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Desenvolver um componente de processamento de logs que filtre, transforme e agregue eventos de sistema, garantindo que a solução seja escalável (evitando loops aninhados) e utilize a sintaxe Pythônica para performance.

## 🛠 Implementação
Você deve criar o arquivo `event_filter.py` com as seguintes funcionalidades:
1. **Filtro de Nível:** Uma função que utilize *list comprehension* para extrair eventos de um nível específico (ex: `"ERROR"`, `"CRITICAL"`).
2. **Agregador de Mensagens:** Uma função que percorra os eventos filtrados e concatene as mensagens de erro em um único relatório resumido.
3. **Detecção de Anomalias:** Um loop que identifique se existem mais de 5 erros em um intervalo de 10 eventos (Janela Deslizante simples).

**Requisito Técnico:** 
- O código deve ser capaz de processar a lista de eventos da "Loja Aurora" (gerada no dataset).
- Complexidade temporal máxima permitida: $O(n)$.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Para a construção do Motor de Filtragem, optei pelo uso de List Comprehensions em vez de loops for tradicionais para a extração de eventos. Esta decisão foi baseada na maior performance de execução do interpretador Python para este padrão. Além disso, implementei a detecção de anomalias com complexidade linear $O(n)$, garantindo que o motor de filtragem mantenha a mesma performance independentemente do volume de logs processados, evitando a degradação exponencial comum em implementações iniciantes."

## ✅ Checklist de Aceite
- [ ] Não há loops aninhados para comparação de dados.
- [ ] O filtro retorna a lista correta de eventos.
- [ ] O agregador lida corretamente com listas vazias (não quebra).
- [ ] A detecção de anomalias identifica corretamente o pico de erros.
- [ ] Código segue a PEP 8 (estilo de código Python).
