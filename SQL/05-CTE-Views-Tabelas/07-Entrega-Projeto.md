---
tipo: projeto
trilha: SQL
capitulo: 05
titulo: "Projeto: Pipeline de Transformação de Dados"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, pipeline, etl]
---
# Projeto: Pipeline de Transformação de Dados

## 🚩 Cenário
Você está construindo a camada "Silver" de um Data Lake no MySQL. Os dados brutos chegam em tabelas desorganizadas e você precisa criar um processo de limpeza e agregação modular.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL que execute a seguinte sequência lógica:

1. **Etapa de Limpeza (CTE 1):** Criar uma CTE que selecione apenas vendas válidas (status = 'concluido') e trate valores nulos de desconto como 0.
2. **Etapa de Enriquecimento (CTE 2):** Criar uma segunda CTE que faça JOIN entre a primeira CTE e a tabela de produtos para obter a categoria do produto.
3. **Etapa de Agregação (CTE 3):** Criar uma terceira CTE que agrupe o faturamento por categoria e calcule a média de vendas.
4. **Entrega Final:** Um SELECT final que retorne a categoria e o total de faturamento, filtrando apenas categorias que venderam mais de 1000.00.

**Bônus:** Crie uma `VIEW` final chamada `vw_faturamento_categorias` que encapsule toda essa lógica para que o time de BI possa consultá-la sem ver o código.

## ✅ Critérios de Aceite
- [ ] Uso de múltiplas CTEs sequenciais.
- [ ] Tratamento de nulos (ex: `COALESCE` ou `IFNULL`).
- [ ] Join correto entre as etapas.
- [ ] Criação da View final.

## 🧪 Como Validar
Execute o script e valide se a View `vw_faturamento_categorias` retorna a lista correta de categorias e valores.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[06-Procedures]] →
