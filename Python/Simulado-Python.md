---
tipo: simulado
trilha: python
capitulo: final
titulo: "Simulado Técnico: Python para Engenharia de Dados"
nivel: 5
tempo_estimado_h: 4
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-20
tags: [simulado, tecnico, python, data-engineering]
---
# Simulado Técnico: Python para Engenharia de Dados

> [!abstract] Avaliação Final de Proficiência
> ⏱ 4h · 🎯 Nível 5/5 · 🔗 Abrangência: Capítulos 01 ao 12 · ✅ Verificado

## 🎯 Objetivo do Simulado
Validar a capacidade do aluno em resolver problemas reais de engenharia de dados, integrando conceitos de OOP, performance, persistência e integração. Este simulado simula a entrevista técnica de um Desenvolvedor de Dados Júnior.

---

## 🧩 Parte 1: Teoria e Conceitos (Múltipla Escolha)
*Tente responder sem consultar o material.*

**1. Qual a principal razão para utilizar `@dataclass(frozen=True)` em vez de uma classe comum para representar registros de um banco de dados em um pipeline?**
a) Melhora a velocidade de inserção no banco de dados.
b) Garante a imutabilidade dos dados, evitando efeitos colaterais durante transformações.
c) Permite que a classe seja serializada automaticamente para JSON.
d) Reduz o consumo de memória RAM em comparação a dicionários.

**2. No contexto de processamento de Big Data com Pandas, o que acontece quando utilizamos o parâmetro `chunksize` no `read_csv`?**
a) O Pandas lê o arquivo mais rápido usando threads internas.
b) O arquivo é lido inteiramente, mas dividido em partes na memória.
c) O Pandas retorna um iterador (TextFileReader), carregando apenas a quantidade de linhas especificada por vez.
d) O arquivo é compactado automaticamente para economizar espaço.

**3. Por que o uso de `joinedload` no SQLAlchemy é essencial para evitar o problema do "N+1 Queries"?**
a) Porque ele executa a query de forma assíncrona.
b) Porque ele força a realização de um JOIN no banco de dados, trazendo os dados relacionados em uma única requisição.
c) Porque ele armazena os resultados em cache local.
d) Porque ele converte os objetos do ORM em dicionários simples.

---

## 🛠 Parte 2: Desafios de Código (Hands-on)

### Desafio A: O Limpador de Dados (Performance)
**Cenário:** Você tem um DataFrame com 10 milhões de linhas. A coluna `status` contém valores como "SUCESSO", "ERRO" e "PENDENTE". Você precisa criar uma nova coluna `is_valid` que seja `True` para "SUCESSO" e `False` para os demais.

**Tarefa:** Escreva a implementação utilizando **vetorização**.
- [ ] Proibido usar `.apply()` ou loops `for`.
- [ ] Use `np.where` ou indexação booleana.

### Desafio B: O Integrador Assíncrono (API)
**Cenário:** Você precisa buscar o preço atual de 50 moedas diferentes de uma API REST. Se fizer isso sequencialmente, levará 50 segundos.

**Tarefa:** Implemente a função utilizando `httpx` e `asyncio.gather()`.
- [ ] a função deve receber uma lista de IDs de moedas.
- [ ] as requisições devem ser disparadas simultaneamente.

### Desafio C: A Camada de Persistência (ORM)
**Cenário:** Implemente uma função `upsert_product(session, product_data)` que:
1. Verifique se o produto já existe no banco pelo ID.
2. Se existir, atualize o preço e a quantidade.
3. Se não existir, crie um novo registro.
4. Garanta que a operação ocorra dentro de uma transação atômica.

---

## 🚀 Parte 3: Arquitetura (Case Study)
**Case:** "O Pipeline de Vendas da Aurora"
Você deve desenhar a lógica de um pipeline que:
1. Lê arquivos CSV de 5GB vindos de um S3 (via chunks).
2. Limpa os dados (remove nulos, corrige tipos para `float32`).
3. Enriquece os dados fazendo merge com uma tabela de Categorias no PostgreSQL via SQLAlchemy.
4. Salva o resultado final em arquivos Parquet particionados por data.

**Pergunta:** Como você garantiria que esse pipeline não trave por falta de memória e seja capaz de retomar de onde parou caso a conexão com o S3 caia?

---

## 🏁 Gabarito e Critérios de Avaliação
- **Teoria:** 1(b), 2(c), 3(b).
- **Código:** Avaliado por: (1) Ausência de loops em DataFrames, (2) Uso correto de `await/async`, (3) Gestão de `session.commit/rollback`.
- **Arquitetura:** Espera-se a menção a: `chunksize` $\rightarrow$ `astype` $\rightarrow$ `joinedload` $\rightarrow$ `checkpointing` $\rightarrow$ `Parquet`.

---
← [[Python/12-Projeto-Escala/07-Entrega-Projeto]] · [[MOC-Python]] · [[Python/Projeto-Final-Python]] →
