---
tipo: projeto
trilha: SQL
capitulo: 03
titulo: "Projeto: Mapa de Vendas Regional"
nivel: 3
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, joins]
---
# Projeto: Mapa de Vendas Regional

## 🚩 Cenário
A diretoria quer um relatório de "Penetração de Mercado". Eles precisam saber quais cidades têm clientes, mas não possuem nenhuma venda registrada, para que possam enviar equipes de vendas para essas regiões.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL único contendo:

1. **Relatório de Inativos:** 
    - Listar o nome do cliente e a cidade de todos os clientes que **NUNCA** fizeram um pedido.
2. **Relatório de Volume por Cidade:**
    - Listar todas as cidades e a soma total de vendas de cada cidade.
    - Cidades sem vendas devem aparecer com valor 0 ou `NULL`.
3. **Análise de Clientes VIP:**
    - Listar apenas os clientes que fizeram mais de 2 pedidos, mostrando o nome do cliente e a quantidade de pedidos.

## ✅ Critérios de Aceite
- [ ] Uso correto de `LEFT JOIN` para identificar os inativos.
- [ ] Uso de `GROUP BY` e `SUM` para o volume por cidade.
- [ ] Uso de `HAVING` para filtrar os clientes VIP.
- [ ] Código organizado com aliases claros (ex: `c` para customers, `o` para orders).

## 🧪 Como Validar
Execute o script no MySQL 8.x e valide se a lista de inativos condiz com a base de dados do Lab 03.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[04-Window-Functions]] →
