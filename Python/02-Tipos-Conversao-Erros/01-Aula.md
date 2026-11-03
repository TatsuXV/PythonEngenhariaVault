---
tipo: aula
trilha: python
capitulo: 02
titulo: "Tipos, Conversão e Gestão de Erros"
nivel: 1
tempo_estimado_h: 5
dominio: 0
status: concluido
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [tipos, casting, excecoes]
---
# Tipos, Conversão e Gestão de Erros

> [!abstract] Capítulo 02 · Tipos, Conversão e Gestão de Erros
> ⏱ 5h · 🎯 Nível 1/5 · 🔗 Pré-requisitos: [[Python/01-Setup-Git/01-Aula]] · 📦 Entrega: [[Python/02-Tipos-Conversao-Erros/07-Entrega-Projeto|Validador de Tipos de Dados]] · ✅ Verificado

## 🧠 Pré-Teste
> [!question] O que acontece se você tentar converter a string `"10,50"` (com vírgula) para `float` em Python?
> ?
> [!question] Qual a diferença entre `TypeError` e `ValueError`?
> ?
> [!question] Por que usar `try...except` em excesso pode prejudicar a performance de um pipeline de dados?
> ?

## 🎯 Objetivo
> [!goal]
> Dominar a tipagem dinâmica do Python, realizar conversões seguras (casting) e implementar a gestão de exceções profissional para evitar que pipelines de dados travem por causa de um único registro sujo.

## ⚙️ No Pipeline
> [!pipeline]
> Em engenharia de dados, a "sujeira" nos dados é a norma. Um CSV pode ter `10.5` em uma linha e `N/A` ou `10,5` na outra. Se o seu código não gerir a conversão de tipos com `try...except` ou validações prévias, o pipeline de 1 bilhão de linhas vai travar na linha 500.000.000, perdendo horas de processamento.

## 📚 Teoria

### 1. Tipagem Dinâmica vs Estática (Python vs Java)
No Java, você declara `int x = 10;`. No Python, você escreve `x = 10`. O tipo é associado ao **objeto**, não à variável.

| Tipo | Python | Java Equivalente | Observação |
| :--- | :--- | :--- | :--- |
| Inteiro | `int` | `int` / `long` | Precisão arbitrária (não estoura) |
| Flutuante | `float` | `double` | Padrão IEEE 754 |
| Texto | `str` | `String` | Imutável, UTF-8 por padrão |
| Booleano | `bool` | `boolean` | Subclasse de `int` (`True=1`, `False=0`) |

### 2. Conversão de Tipos (Casting)
Conversões explícitas são necessárias para garantir a integridade dos dados.
- `int("10")` $\rightarrow$ `10`
- `float("10.5")` $\rightarrow$ `10.5`
- `str(10.5)` $\rightarrow$ `"10.5"`

**⚠️ Armadilha:** `int("10.5")` gera `ValueError`. Você deve converter para `float` primeiro: `int(float("10.5"))`.

### 3. Gestão de Erros (Exceções)
A filosofia do Python é **EAFP** (*Easier to Ask Forgiveness than Permission*), ao contrário do Java que tende ao **LBYL** (*Look Before You Leap*).

**Estrutura Profissional:**
```python
try:
    # Código que pode falhar (ex: conversão de dado sujo)
    valor = float(dado_sujo)
except ValueError as e:
    # Tratamento específico para erro de conversão
    logging.error(f"Falha na conversão: {e}")
    valor = 0.0 # Valor default (imputação)
except Exception as e:
    # Captura qualquer outro erro inesperado
    logging.critical(f"Erro inesperado: {e}")
    raise e
finally:
    # Executa sempre (fechar arquivos, conexões)
    pass
```

## ⚠️ Armadilhas e Erros Comuns
- **Bare Except:** Usar `except:` sem especificar a exceção. Isso captura até o `KeyboardInterrupt` (Ctrl+C), tornando o programa impossível de parar.
- **Silenciar Erros:** Usar `pass` dentro do `except` sem logar o erro. Isso esconde bugs críticos em produção.

## 🐛 Correções do Material
> [!bug] Correção
> **Original:** "Use `try...except` para validar se um arquivo existe."
> **Por que está errado:** Verificar a existência de um arquivo com `try` é lento e sujeito a *race conditions*.
> **Correto:** Use `pathlib.Path("arquivo.txt").exists()`.

## ℹ️ Conteúdo Complementar
> [!info] Conteúdo complementar
> **Type Hinting (PEP 484):** Embora o Python seja dinâmico, podemos adicionar dicas de tipo para o IDE e para ferramentas como `mypy`:
> `def process_amount(value: str) -> float:`. Isso aproxima o Python da segurança do Java.

## 📖 Fonte
Fonte: [Python Docs - Built-in Types](https://docs.python.org/3/library/stdtypes.html) (Versão 3.12)

---
← [[Python/01-Setup-Git/01-Aula]] · [[MOC-Python]] · [[Python/03-Controle-Fluxo/01-Aula]] →
