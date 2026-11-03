---
tipo: flashcards
trilha: SQL
capitulo: 12
titulo: "Flashcards: Modelagem e Normalização"
nivel: 5
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards, modeling]
---
# Flashcards: Modelagem e Normalização

> [!question] Qual o objetivo principal da 3ª Forma Normal (3NF)?
> [!success] Resposta
> Eliminar as dependências transitivas. Garante que toda coluna não-chave dependa exclusivamente da chave primária, e não de outra coluna não-chave.

> [!question] Quando devemos usar um Snowflake Schema em vez de um Star Schema?
> [!success] Resposta
> Quando as dimensões são muito grandes e possuem hierarquias complexas que, se desnormalizadas, causariam redundância excessiva de dados, ou quando a consistência dos atributos da dimensão é mais crítica que a performance de leitura.

> [!question] O que é uma Surrogate Key (Chave Substituta)?
> [!success] Resposta
> É uma chave artificial (geralmente um `INT AUTO_INCREMENT`) criada para ser a PK de uma tabela, independentemente de qualquer dado de negócio. Ela protege a modelagem contra mudanças em chaves naturais (ex: mudança de e-mail do cliente).

> [!//question] Qual a diferença entre OLTP e OLAP em termos de modelagem?
> [!success] Resposta
> OLTP (Sistemas Transacionais) foca em Normalização para evitar anomalias de escrita. OLAP (Sistemas Analíticos) foca em Desnormalização (Star Schema) para maximizar a velocidade de leitura e agregação.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
