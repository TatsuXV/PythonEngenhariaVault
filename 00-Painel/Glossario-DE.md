# Glossário de Engenharia de Dados (DE)

| Termo em Inglês | Tradução/Equivalente | Definição Curta |
| :--- | :--- | :--- |
| **Data Pipeline** | Pipeline de Dados | Sequência de processos que movem dados de uma fonte para um destino. |
| **ETL (Extract, Transform, Load)** | Extrair, Transformar, Carregar | Processo tradicional onde a transformação ocorre antes da carga no DW. |
| **ELT (Extract, Load, Transform)** | Extrair, Carregar, Transformar | Processo moderno onde a transformação ocorre dentro do destino (Cloud DW). |
| **Data Lake** | Lago de Dados | Repositório de dados em formato bruto (raw), geralmente em arquivos (Parquet, JSON). |
| **Data Warehouse** | Armazém de Dados | Banco de dados otimizado para análise (OLAP), com dados estruturados. |
| **Sargable** | Pesquisável por Índice | Consulta SQL que permite ao motor usar índices para filtrar dados. |
| **Idempotency** | Idempotência | Propriedade de uma operação que produz o mesmo resultado, não importa quantas vezes seja executada. |
| **Upsert** | Atualizar ou Inserir | Operação que insere um registro se não existir, ou o atualiza se já existir. |
| **Schema** | Esquema | A estrutura/definição das tabelas e relacionamentos de um banco. |
| **Window Function** | Função de Janela | Funções que realizam cálculos através de um conjunto de linhas relacionadas à linha atual. |
| **CTE (Common Table Expression)** | Expressão de Tabela Comum | Conjunto de resultados temporário definido usando a cláusula `WITH`. |
| **Backfill** | Retroalimentação | Processo de carregar dados históricos em um pipeline após a criação ou alteração. |
| **Orchestration** | Orquestração | Gestão de dependências e agendamento de tarefas (ex: Airflow). |
