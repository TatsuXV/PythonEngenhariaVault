---
tipo: lab
trilha: SQL
capitulo: 10
titulo: "Prática de Indexação e Performance"
nivel: 4
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, btree, indexing, lab]
---
# Lab: Prática de Indexação e Performance

> [!abstract] Capítulo 10 · Prática de Indexação e Performance
> ⏱ 4h · 🎯 Nível 4/5 · 🔗 Pré-requisitos: [[01-Aula]] · 📦 Entrega: [[07-Entrega-Projeto]] · ✅ Verificado

## 📦 0. Setup de Dados (Local)
> [!example] Execute este script no seu MySQL 8.x para preparar o Lab
```sql
CREATE TABLE IF NOT EXISTS lab_users_idx (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    city VARCHAR(50),
    created_at DATE
);

INSERT INTO lab_users_idx VALUES 
(1, 'Ana', 'Silva', 'ana@email.com', 'São Paulo', '2023-01-01'),
(2, 'Bruno', 'Costa', 'bruno@email.com', 'Rio de Janeiro', '2023-01-05'),
(3, 'Carla', 'Dias', 'carla@email.com', 'São Paulo', '2023-02-10'),
(4, 'Daniel', 'Oliveira', 'daniel@email.com', 'Curitiba', '2023-03-15'),
(5, 'Eduarda', 'Lima', 'eduarda@email.com', 'Belo Horizonte', '2023-04-20');
```

## 💡 1. Exemplo Resolvido
> [!question] Preveja o resultado do EXPLAIN
> > [!//success] Resposta
> > O `type` será `ALL` porque não há índice na coluna `email`. O MySQL lerá a tabela inteira.
> > **Explicação:** Sem um índice, o banco não tem "estrada expressa" para o dado.

```sql
EXPLAIN SELECT * FROM lab_users_idx WHERE email = 'ana@email.com';
```

## 🛠 2. Complete (Fill-in-the-blanks)
O código abaixo contém lacunas `# TODO`. Complete-o para que o teste passe.

**Objetivo:** Criar um índice para a coluna `email` e validar a mudança de performance via EXPLAIN.

```sql
-- Step 1: Criar o índice
CREATE INDEX # TODO: Nomeie o índice e defina a coluna email
ON lab_users_idx(email);

-- Step 2: Analisar a query novamente
EXPLAIN SELECT * FROM lab_users_idx WHERE email = 'ana@email.com';
```

**Como verificar:** O `type` deve mudar de `ALL` para `ref`.

## 🚀 3. Do Zero
**Enunciado:** Crie um índice composto nas colunas `(city, last_name)`. Em seguida, execute duas queries e use o `EXPLAIN` para provar:
1. A primeira query filtra por `city` $\rightarrow$ O índice é usado.
2. A segunda query filtra apenas por `last_name` $\rightarrow$ O índice é ignorado.

**Critério de Aceite:** 
1. Provar a regra do "Prefix Left-most" (Prefixo à esquerda).

## 🧪 Quebre de Propósito
Aplique as seguintes mudanças e explique o erro:
1. Tente criar um índice em uma coluna de texto gigantesca (`LONGTEXT`) sem especificar um comprimento $\rightarrow$ Erro esperado: **Specified key was too long**. Explique a necessidade de prefixar índices em textos longos.
2. Crie índices em todas as 6 colunas da tabela e execute um `INSERT` massivo $\rightarrow$ Observe a lentidão. Explique por que cada índice torna a escrita mais cara.
3. Tente criar dois índices idênticos na mesma coluna $\rightarrow$ Observe se o MySQL permite ou se ignora o segundo.

---
← [[01-Aula]] · [[MOC-SQL]] · [[03-Tickets]] →
