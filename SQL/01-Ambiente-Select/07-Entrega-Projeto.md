---
tipo: projeto
trilha: SQL
capitulo: 01
titulo: "Projeto: Auditoria de Base de Clientes"
nivel: 1
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, projeto, auditoria]
---
# Projeto: Auditoria de Base de Clientes

## 🚩 Cenário
Você foi contratado como Data Engineer júnior. Sua primeira tarefa é realizar uma auditoria na tabela de clientes (`lab_customers`) para identificar possíveis anomalias nos dados de registro.

## 🎯 Requisitos da Entrega
Você deve entregar um script SQL único contendo três consultas:

1. **Consulta de Abrangência:** Retornar todos os países únicos presentes na base, ordenados alfabeticamente.
2. **Consulta de Filtro Crítico:** Listar todos os clientes que se registraram em 2023, mas que NÃO moram no Brasil ou USA.
3. **Consulta de Formatação:** Retornar o email e o nome completo (concatenado) apenas dos clientes de 'São Paulo', renomeando a coluna de nome para `cliente_identificado`.

## ✅ Critérios de Aceite
- [ ] Uso correto de `DISTINCT`.
- [ ] Uso de `NOT IN` ou operadores de negação.
- [ ] Uso de `CONCAT` e `AS` para alias.
- [ ] Código indentado e legível.

## 🧪 Como Validar
Execute as queries no MySQL e valide se o número de linhas retornadas condiz com os dados inseridos no Lab 01.

---
← [[06-Revisao]] · [[MOC-SQL]] · [[02-DDL-DML-Filtros-Agregacoes]] →
