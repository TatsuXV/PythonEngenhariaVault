---
tipo: flashcard
trilha: python
capitulo: 11
titulo: "Flashcards: APIs & REST"
nivel: 4
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-10
tags: [flashcards, api, fastapi, requests]
---
# Flashcards: APIs & REST

## 🧠 Conceitos
O que caracteriza uma API como sendo "RESTful"?::Ela utiliza a arquitetura REST, baseando-se no protocolo HTTP, usa URIs para identificar recursos e métodos HTTP (GET, POST, etc) para definir a ação.
Qual a diferença entre os métodos PUT e PATCH?::O `PUT` substitui o recurso completo por uma nova versão; o `PATCH` aplica modificações parciais a um recurso existente.
O que é a "Idempotência" em APIs?::É a propriedade de que múltiplas requisições idênticas têm o mesmo efeito que uma única requisição (ex: GET e DELETE são idempotentes, POST não é).

## ⌨️ Código & Sintaxe
Como fazer uma requisição POST enviando um JSON com a biblioteca `requests`?::`requests.post(url, json={'chave': 'valor'})`
Qual decorador do FastAPI é usado para definir uma rota de recuperação de dados?::`@app.get("/rota")`
Como validar a entrada de dados em uma rota do FastAPI?::Definindo um schema utilizando a biblioteca Pydantic (`class MySchema(BaseModel): ...`) e usando-o como tipo do argumento da função da rota.

## ⚠️ Erros e Correções
Erro: `422 Unprocessable Entity`. Causa?::Erro de validação de dados. O cliente enviou dados em formato ou tipo diferente do esperado pelo Pydantic no FastAPI.
Erro: `401 Unauthorized`. Causa?::Falta de autenticação ou token de API inválido/expirado. Correção: Verificar os Headers de Authorization.
Erro: `429 Too Many Requests`. Causa?::O cliente excedeu o limite de requisições (Rate Limit) da API. Correção: Implementar Exponential Backoff ou reduzir a frequência de chamadas.

## 🧩 Cloze (Preencher)
O formato ==JSON== (JavaScript Object Notation) é o padrão mais utilizado para troca de dados em APIs REST por ser leve e fácil de ler tanto por humanos quanto por máquinas?
resposta: JSON
