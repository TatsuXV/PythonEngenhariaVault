# Guia de Estilo do Vault de Engenharia de Dados

Este documento define a padronização visual e estrutural de todas as notas do vault. A consistência é fundamental para a navegação rápida e a automação via Dataview.

## 📐 Estrutura de Arquivo
- **Nome:** `NN-Nome-da-Nota.md` (ex: `01-Setup-Git.md`).
- **H1:** Um único `# Título` por nota.
- **Hierarquia:** H2 $\rightarrow$ H3 $\rightarrow$ H4. Nunca pular níveis.

## 🏷 Frontmatter (YAML)
Toda nota deve iniciar com:
```yaml
---
tipo: aula | lab | ticket | flashcard | revisao | projeto
trilha: python | sql | ed | eds
capitulo: NN
titulo: "Título da Nota"
nivel: 1-5
tempo_estimado_h: X
dominio: 0 # 0=visto, 1=praticado, 2=dominado, 3=ensinado
status: nao-iniciado | em-andamento | concluido
verificado: true | false
versao_doc: "X.X"
proxima_revisao: YYYY-MM-DD
tags: [tag1, tag2]
---
```

## 📦 Componentes Visuais

### 1. Cabeçalho Padrão
Imediatamente após o H1, em um callout `[!abstract]`:
> [!abstract] Capítulo NN · Título
> ⏱ Xh · 🎯 Nível N/5 · 🔗 Pré-requisitos: [[...]] · 📦 Entrega: [[...]] · ✅ Verificado

### 2. Taxonomia de Callouts
| Callout | Uso | Ícone |
| :--- | :--- | :--- |
| `[!goal]` | Objetivo da aula/exercício | 🎯 |
| `[!pipeline]` | Onde isso se encaixa em um pipeline real de dados | ⚙️ |
| `[!example]` | Exemplos de código/estudo | 💡 |
| `[!question]` | Pergunta de predição ou reflexão | 🧠 |
| `[!bug]` | Correção de erro do material original | 🐛 |
| `[!warning]` | Armadilha técnica ou conteúdo não verificado | ⚠️ |
| `[!info]` | Conteúdo complementar (extra da doc oficial) | ℹ️ |
| `[!todo]` | Ticket de tarefa/exercício | 🎫 |
| `[!tip]` | Dica de performance ou atalho | 🚀 |
| `[!success]` | Critério de aceite/conclusão | ✅ |

### 3. Código e Tabelas
- **Linguagens:** Sempre especificar no fence (ex: ` ```python `, ` ```sql `, ` ```powershell `).
- **OS:** Comandos Windows em subseção "Windows (PowerShell)" e Linux/macOS em "Linux/macOS (Bash)".
- **Tabelas:** Usar para comparações (Ex: Java vs Python).

### 4. Navegação de Rodapé
Obrigatório em notas de capítulos:
`← [[anterior]] · [[MOC]] · [[próximo]] →`

## 🧪 Padrões de Prática (Lab e Tickets)
- **Predizer $\rightarrow$ Executar $\rightarrow$ Comparar:** Sempre usar `[!question]` dobrável antes de blocos de código no Lab.
- **Autocorreção:** 
  - Python: `test_*.py` (pytest).
  - SQL: `verificar.sql` (Retorno PASS/FAIL).
- **Quebre de Propósito:** Seção final de cada lab para análise de traceback.

## 🛠 Mermaid Diagrams
Usar para fluxos de dados e arquitetura:
- `graph TD` para fluxos simples.
- `sequenceDiagram` para interação API/DB.
- `erDiagram` para modelagem de dados.
