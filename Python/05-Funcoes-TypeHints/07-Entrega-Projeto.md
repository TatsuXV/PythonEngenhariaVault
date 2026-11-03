---
tipo: projeto
trilha: python
capitulo: 05
titulo: "Entrega: Biblioteca de Transformações de Dados"
nivel: 3
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [projeto, modularizacao, type-hints]
---
# Entrega: Biblioteca de Transformações de Dados

> [!abstract] Parte do Projeto Python
> ⏱ 2h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/05-Funcoes-TypeHints/06-Revisao]] · ✅ Verificado

## 🎯 Objetivo de Entrega
> [!success]
> Desenvolver um módulo Python (`transformations.py`) que centralize todas as lógicas de limpeza, normalização e validação de dados da Loja Aurora. Este módulo deve ser totalmente independente, tipada e testável.

## 🛠 Implementação
Você deve construir a biblioteca com as seguintes funções puras:

1. **`clean_currency(value: str) -> float`**: Remove símbolos monetários e converte para float (usando o conhecimento do Cap 02).
2. **`normalize_text(text: Optional[str]) -> Optional[str]`**: Remove espaços extras e converte para lowercase (estilo padronizado).
3. **`validate_date(date_str: str) -> bool`**: Verifica se a data segue o padrão ISO (YYYY-MM-DD).
4. **`apply_business_rule(value: float, rule_func: Callable[[float], float]) -> float`**: Aplica uma regra de negócio dinâmica (ex: desconto ou acréscimo).

**Requisitos Técnicos:**
- **Zero Efeitos Colaterais:** Nenhuma função deve alterar as listas ou dicionários de entrada.
- **Type Hints Rigorosos:** Uso de `Optional`, `List`, `Callable` e `Union`.
- **Documentação:** Cada função deve possuir uma Docstring no padrão Google ou NumPy.

## 📝 README (Para Portfólio)
Escreva aqui o parágrafo explicativo sobre a implementação deste módulo, focando no "porquê" das decisões técnicas.
> [!todo] Redação do Aluno
> "Para este módulo de transformações, adotei a abordagem de Programação Funcional, implementando funções puras e imutáveis. A decisão de utilizar Type Hints rigorosos visa reduzir a incidência de erros de tipo em tempo de execução, permitindo a detecção de bugs via análise estática. Ao isolar a lógica de negócio em funções pequenas e independentes, facilitei a criação de testes unitários granulares, garantindo que cada etapa da limpeza de dados seja verificada isoladamente antes da integração no pipeline final."

## ✅ Checklist de Aceite
- [ ] O módulo `transformations.py` roda sem erros de sintaxe.
- [ ] `mypy transformations.py` não reporta erros de tipo.
- [ ] Funções tratam `None` sem causar `AttributeError`.
- [ ] Nenhuma função altera a variável de entrada original.
- [ ] Todas as funções possuem Docstrings claras.
