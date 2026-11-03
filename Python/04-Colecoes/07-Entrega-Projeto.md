---
tipo: projeto
trilha: python
capitulo: 04
titulo: "Entrega: Agregador de Vendas por Categoria"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, agregacao, performance]
---
# Entrega: Agregador de Vendas por Categoria

> [!abstract] Parte do Projeto Python
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/04-Colecoes/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Construir um motor de agregação em memória que processe vendas brutas e gere um resumo financeiro por categoria, simulando a lógica de um `GROUP BY` de SQL.

## 🛠 Implementação
Crie o arquivo `sales_aggregator.py` com a seguinte lógica:
1. **Ingestão:** A função deve aceitar uma lista de tuplas `(pedido_id, categoria, valor)`.
2. **Agregação:** Use um `defaultdict` para somar o valor total e contar a quantidade de pedidos por categoria.
3. **Análise:** O resultado final deve ser um dicionário onde cada categoria contém: `{"total_revenue": X, "order_count": Y, "avg_ticket": Z}`.
4. **Performance:** O código deve rodar em $O(n)$ e suportar a escala do dataset "Loja Aurora".

**Requisito Técnico:** 
- Implementar a lógica de "Ticket Médio" (`avg_ticket`) evitando a divisão por zero.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Implementei um agregador de vendas utilizando a estrutura de dados `defaultdict` do Python para simular operações de agregação típicas de Data Warehouses. Optei por esta abordagem para garantir que a complexidade temporal fosse linear $O(n)$, permitindo o processamento de milhões de registros de vendas sem a degradação de performance associada a buscas em listas. A escolha de tuplas para a entrada de dados visou a eficiência de memória e a imutabilidade dos registros durante o processamento."

## ✅ Checklist de Aceite
- [ ] Não existem loops aninhados para soma de valores.
- [ ] O cálculo do Ticket Médio está correto.
- [ ] O código lida com categorias inexistentes ou listas vazias.
- [ ] Complexidade temporal comprovada como $O(n)$.
- [ ] O resultado final é um dicionário de dicionários.
