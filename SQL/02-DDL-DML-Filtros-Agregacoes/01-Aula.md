---
tipo: aula
trilha: SQL
capitulo: 02
titulo: "DDL, DML, Filtros e Agregações"
nivel: 2
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0 Reference Manual"
proxima_revisao: 
tags: [mysql, ddl, dml, agregacoes]
comparativo_dialecto: true
---
# DDL, DML, Filtros e Agregações

> [!abstract] Capítulo 02 · DDL, DML, Filtros e Agregações
> ⏱ 6h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Pergunta 1: Qual a diferença entre `TRUNCATE` e `DELETE`?
> ?
> [!question] Pergunta 2: O que acontece se você usar uma função de agregação (como `SUM`) no SELECT sem usar o `GROUP BY` para as outras colunas?
> ?
> [!question] Pergunta 3: Qual a diferença entre `CHAR` e `VARCHAR` no MySQL?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a manipulação de estruturas (DDL) e de dados (DML), além de aprender a resumir grandes volumes de informação utilizando funções de agregação e agrupamentos.

## ⚙️ No Pipeline
> [!pipeline]
> Como Engenheiro de Dados, você passará muito tempo criando tabelas de "Staging" (temporárias) e transformando dados brutos em agregados para dashboards. Saber a diferença entre `DELETE` e `TRUNCATE` é a diferença entre um Job de 1 minuto e um Job de 1 hora.

## 📚 Teoria

### 1. DDL (Data Definition Language) - Definindo a Estrutura
DDL lida com o esquema do banco de dados.
- `CREATE TABLE`: Cria a tabela e define tipos de dados e constraints.
- `ALTER TABLE`: Modifica a estrutura (adiciona/remove colunas).
- `DROP TABLE`: Remove a tabela e todos os seus dados permanentemente.
- `TRUNCATE TABLE`: Esvazia a tabela rapidamente, resetando contadores de `AUTO_INCREMENT`.

### 2. DML (Data Manipulation Language) - Manipulando Dados
DML lida com as linhas dentro das tabelas.
- `INSERT INTO`: Adiciona novos registros.
- `UPDATE`: Modifica registros existentes (Sempre use `WHERE`!).
- `DELETE`: Remove registros específicos (Sempre use `WHERE`!).

### 3. Funções de Agregação e GROUP BY
Agregações transformam múltiplas linhas em um único valor resumo.
- `COUNT()`: Conta registros.
- `SUM()`: Soma valores numéricos.
- `AVG()`: Calcula a média.
- `MAX()` / `MIN()`: Retorna o maior/menor valor.

**Regra de Ouro do GROUP BY:** Qualquer coluna que apareça no `SELECT` e NÃO esteja dentro de uma função de agregação **DEVE** obrigatoriamente estar na cláusula `GROUP BY`.

## 🔄 Tradução de Dialeto: Postgres $\rightarrow$ MySQL
> [!compare] Diferenças Importantes
> | Conceito | PostgreSQL | MySQL 8.x | Nota de Migração |
> | :--- | :--- | :--- | :--- |
> | **Auto-incremento** | `SERIAL` ou `GENERATED ALWAYS AS IDENTITY` | `AUTO_INCREMENT` | No MySQL, o `AUTO_INCREMENT` deve ser definido junto com a `PRIMARY KEY`. |
> | **Tipos de Texto** | `TEXT` é performático. | `TEXT` vs `VARCHAR(N)`. | No MySQL, prefira `VARCHAR` se souber o limite, pois facilita a criação de índices. |
> | **Truncate** | `TRUNCATE` é rápido mas requer cautela com FKs. | `TRUNCATE` é extremamente rápido. | Ambos resetam a identidade/auto-incremento. |
> | **Booleanos** | Tipo `BOOLEAN` real. | `TINYINT(1)` (0 ou 1). | O MySQL trata `BOOL` como um apelido para `TINYINT(1)`. |

## ⚠️ Armadilhas e Erros Comuns
- **UPDATE/DELETE sem WHERE:** O erro mais clássico e perigoso. Você altera/deleta a tabela inteira.
- **Agregações Incompletas:** Tentar selecionar `cliente_id` e `SUM(valor)` sem agrupar por `cliente_id`.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** `SELECT cidade, SUM(populacao) FROM cidades;`
> **Por que está errado:** Falta a cláusula `GROUP BY cidade`. O MySQL (em versões antigas ou configs específicas) poderia retornar um erro ou um resultado aleatório.
> **Correto:** `SELECT cidade, SUM(populacao) FROM cidades GROUP BY cidade;`

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> Estude sobre **Constraints** (Restrições):
> - `PRIMARY KEY`: Unicidade e não nulidade.
> - `FOREIGN KEY`: Integridade referencial entre tabelas.
> - `UNIQUE`: Impede valores duplicados.
> - `NOT NULL`: Obriga o preenchimento do campo.

## 📖 Fonte
Fonte: [MySQL 8.0 Reference Manual - Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html) (Versão 8.0)

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Join-Having]] →
