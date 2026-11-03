---
tipo: flashcards
trilha: SQL
capitulo: 06
titulo: "Flashcards: Stored Procedures"
nivel: 4
tempo_estimado_h: 0.5
dominio: 0
status: concluido
verificado: false
versao_doc: "MySQL 8.0"
proxima_revisao: 
tags: [mysql, flashcards]
---
# Flashcards: Stored Procedures

> [!question] Qual a diferença entre parâmetros IN, OUT e INOUT?
> [!success] Resposta
> `IN`: Valor entra na procedure (leitura). `OUT`: Valor é calculado e devolvido para quem chamou (escrita). `INOUT`: Valor entra, é modificado e devolvido.

> [!question] Por que é necessário alterar o DELIMITER ao criar procedures no MySQL?
> [!success] Resposta
> Para que o cliente SQL não interprete o primeiro ponto-e-vírgula (`;`) interno da procedure como o fim do comando de criação, permitindo que todo o bloco seja enviado ao servidor.

> [!question] Quando devemos preferir uma FUNCTION em vez de uma PROCEDURE?
> [!success] Resposta
> Quando o objetivo é apenas calcular e retornar um ÚNICO valor que possa ser usado dentro de um SELECT (ex: `SELECT get_tax(salary) FROM employees`). Procedures são para ações e rotinas.

> [!question] Qual o risco de colocar lógica de negócio excessiva dentro de Stored Procedures?
> [!//success] Resposta
> Sobrecarga da CPU do servidor de Banco de Dados. Processamento intensivo deve ser feito na camada de aplicação (Python, Java, Spark) para permitir a escalabilidade horizontal do app.

---
← [[04-Gabarito]] · [[MOC-SQL]] · [[06-Revisao]] →
