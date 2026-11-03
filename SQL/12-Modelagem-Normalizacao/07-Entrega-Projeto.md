---
tipo: projeto
trilha: SQL
capitulo: 12
titulo: "Projeto Final: Arquitetura de Data Warehouse de Vendas"
nivel: 5
tempo_estimado_h: 8
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, architecture, star-schema, etl]
---
# Projeto Final: Arquitetura de Data Warehouse de Vendas

## 🚩 Cenário
Você foi promovido a Arquiteto de Dados. A empresa agora quer consolidar todos os seus dados de vendas, produtos e clientes em um **Data Warehouse (DW)** para alimentar dashboards de BI. Atualmente, os dados estão espalhados em três sistemas legados desorganizados.

## 🎯 Requisitos da Entrega
Você deve entregar a documentação e o script SQL de criação de um ecossistema completo seguindo estas etapas:

1. **Modelagem Transacional (Staging):**
    - Criar tabelas normalizadas (3NF) para receber os dados brutos dos sistemas legados (`stg_customers`, `stg_products`, `stg_orders`).

2. **Modelagem Analítica (DW - Star Schema):**
    - Projetar e implementar o **Star Schema**:
        - `dim_customer` (com Surrogate Key).
        - `dim_product` (com atributos de categoria e marca).
        - `dim_time` (Tabela de tempo pré-calculada com dia, mês, trimestre, ano).
        - `fact_sales` (Contendo as métricas e as FKs para as dimensões).

3. **Pipeline de Transformação (ETL):**
    - Escrever as queries que movem os dados da camada `stg` para a camada `dim` e `fact`, garantindo a desduplicação.

4. **Consultas de BI (Validação):**
    - Criar 3 views de negócio:
        - `vw_faturamento_mensal`: Soma de vendas por mês/ano.
        - `vw_top_clientes`: Top 10 clientes por valor gasto.
        - `vw_produtos_estagnados`: Produtos que não tiveram vendas nos últimos 3 meses.

## ✅ Critérios de Aceite
- [ ] Separação clara entre Camada Transacional (Normalizada) e Camada Analítica (Dimensional).
- [ ] Uso correto de Surrogate Keys nas dimensões.
- [ ] Implementação de integridade referencial em todo o modelo.
- [ ] Queries de BI otimizadas (evitando Full Table Scans via índices).

## 🧪 Como Validar
1. Carregue dados fictícios nas tabelas `stg`.
2. Execute o script de transformação para alimentar o DW.
3. Valide se os resultados das Views de BI batem com a soma dos dados originais.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[Simulado-SQL]] →
