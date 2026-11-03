---
tipo: flashcards
trilha: SQL
capitulo: 11
titulo: "Flashcards: Particionamento"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Particionamento

> [!question] Qual a diferença entre Sharding e Particionamento?
> [!success] Resposta
> O Particionamento divide a tabela em pedaços dentro de um **único servidor**. O Sharding divide os dados entre **múltiplos servidores** físicos diferentes.

> [!question] O que é Partition Pruning?
> [!success] Resposta
> É a otimização onde o MySQL ignora partições que comprovadamente não contêm os dados da query (baseado na Partition Key), reduzindo drasticamente a leitura de disco.

> [!question] Qual a restrição fundamental da Primary Key em tabelas particionadas no MySQL?
> [!success] Resposta
> Todas as colunas utilizadas na função de particionamento DEVEM obrigatoriamente fazer parte de todas as Unique Keys e da Primary Key da tabela.

> [!question] Por que usar DROP PARTITION em vez de DELETE para limpar dados antigos?
> [!//success] Resposta
> O `DELETE` gera logs de transação para cada linha removida (lento e consome Undo Log). O `DROP PARTITION` remove o arquivo físico da partição instantaneamente (DDL), sendo ordens de magnitude mais rápido.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
