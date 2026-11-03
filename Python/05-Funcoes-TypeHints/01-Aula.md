---
tipo: aula
trilha: python
capitulo: 05
titulo: "Funções e Type Hints: Modularização Profissional"
nivel: 3
tempo_estimado_h: 6
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [funcoes, type-hints, modularizacao]
---
# Funções e Type Hints: Modularização Profissional

> [!abstract] Capítulo 05 · Funções e Type Hints: Modularização Profissional
> ⏱ 6h · 🎯 Nível 3/5 · 🔗 Pré-requisitos: [[Python/04-Colecoes/01-Aula]] · 📦 Entrega: [[Python/05-Funcoes-TypeHints/07-Entrega-Projeto|Biblioteca de Transformações de Dados]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] Qual a diferença entre um argumento `*args` e `**kwargs` em uma função Python?
> ?
> [!question] O que acontece se você alterar uma lista passada como argumento para uma função? A lista original é alterada? Por quê?
> ?
> [!question] Para que serve o módulo `typing` (ex: `List`, `Optional`, `Union`) e por que ele é essencial em pipelines de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Transformar scripts lineares em bibliotecas modulares, utilizando funções puras, tipagem rigorosa (Type Hints) e melhores práticas de design de software para garantir a manutenibilidade do pipeline de dados.

## ⚙️ No Pipeline
> [!pipeline]
> Em pipelines de produção, as transformações de dados são isoladas em funções pequenas e testáveis. Se você tem um script de 500 linhas fazendo tudo, você não tem um pipeline, você tem um "monólito frágil". Ao modularizar, você pode criar testes unitários para cada transformação (ex: `test_clean_currency`), garantindo que a lógica de negócio não quebre ao atualizar uma biblioteca ou mudar a fonte de dados.

## 📚 Teoria

### 1. Anatomia de uma Função Profissional
Diferente de scripts simples, funções de engenharia de dados devem ser **puras** (não alterar estados globais) e bem documentadas.

**Exemplo de Função Padrão Ouro:**
```python
from typing import List, Optional

def calculate_total(prices: List[float], tax: float = 0.05) -> float:
    """
    Calcula o valor total de uma lista de preços aplicando a taxa.
    
    Args:
        prices: Lista de valores flutuantes.
        tax: Taxa de imposto (default 5%).
        
    Returns:
        Soma total com impostos.
    """
    return sum(prices) * (1 + tax)
```

### 2. Type Hinting (A Segurança do Java no Python)
Type Hints não impedem o erro em tempo de execução (runtime), mas permitem que o IDE (VS Code/PyCharm) e ferramentas como `mypy` detectem erros **antes** de você rodar o código.

**Tipos Comuns do módulo `typing`:**
- `List[T]`, `Dict[K, V]`: Tipagem de coleções.
- `Optional[T]`: Quando o valor pode ser de tipo `T` ou `None`. Essencial para dados faltantes.
- `Union[T1, T2]`: Quando o valor pode ser de um de vários tipos.
- `Callable`: Para passar funções como argumentos.

### 3. Passagem de Argumentos
- **Posicionais vs Nomeados:** Use argumentos nomeados (`func(tax=0.1)`) para clareza em funções com muitos parâmetros.
- `*args`: Recebe múltiplos argumentos posicionais como uma tupla.
- `**kwargs`: Recebe múltiplos argumentos nomeados como um dicionário.

### 4. Escopo e Mutabilidade (A Armadilha)
Objetos mutáveis (listas, dicts) passados para funções são passados por **referência**.
**⚠️ Perigo:** Se você der `.append()` em uma lista dentro de uma função, a lista original fora da função também será alterada.
**Solução:** Crie uma cópia dentro da função `new_list = original_list[:]`.

## ⚠️ Armadilhas e Erros Comuns
- **Default Mutável:** Nunca use `def func(data=[])`. O Python cria a lista `[]` apenas uma vez na definição da função. Se você adicionar itens a ela, eles persistirão entre as chamadas da função. **Solução:** Use `data=None` e inicialize com `if data is None: data = []`.
- **Funções Muito Longas:** Funções com mais de 20 linhas geralmente devem ser divididas.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Type hints servem para forçar o Python a ser estático."
> **Por que está errado:** O Python continua sendo dinâmico. Type hints são apenas "metadados" para ferramentas de análise estática.
> **Correto:** Type hints servem para documentação automática e detecção precoce de bugs via `mypy`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Lambda Functions:** Funções anônimas de uma linha. Muito usadas com `map()`, `filter()` e `sorted()`.
> Ex: `sorted(data, key=lambda x: x[1])` ordena por valor.

## 📖 Fonte
Fonte: [Python Docs - Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) (Versão 3.12)

---
← [[Python/04-Colecoes/01-Aula]] · [[MOC-Python]] · [[Python/06-Arquivos-Pathlib/01-Aula]] →
