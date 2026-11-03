# Setup do Obsidian para Engenharia de Dados

Este guia descreve a configuração necessária para que o vault funcione com todas as suas automações e métodos de fixação.

## 🔌 Plugins Obrigatórios (Community Plugins)

### 1. Dataview
**Função:** Transforma o vault em um banco de dados. Essencial para o Dashboard.
- **Instalação:** `Settings` $\rightarrow$ `Community Plugins` $\rightarrow$ `Browse` $\rightarrow$ `Dataview`.
- **Configuração:** 
  - Habilitar `Enable JavaScript Queries` (necessário para dashboards complexos).
  - Habilitar `Enable Inline Queries`.

### 2. Spaced Repetition
**Função:** Implementa o sistema de revisões espaçadas (Anki dentro do Obsidian).
- **Instalação:** `Settings` $\rightarrow$ `Community Plugins` $\rightarrow$ `Browse` $\rightarrow$ `Spaced Repetition`.
- **Configuração:** 
  - `Flashcard tag`: `#flashcards` (ou a tag definida no template).
  - `Review settings`: Ajustar intervalos conforme o Plano de Estudos.

## 🛠 Plugins Opcionais (Recomendados)
- **Tasks:** Para gestão de tickets e TODOs.
- **Templater:** Para automação avançada de templates.
- **Excalidraw:** Para desenho de arquiteturas de dados.

## 📁 Estrutura de Pastas
A estrutura deve seguir rigorosamente a hierarquia definida em `00-Painel/PROGRESSO.md`. Não mova arquivos de lugar sem atualizar os links.

## ⚙️ Configurações de Interface
- **Appearance:** Ativar "Readable line length".
- **Editor:** Ativar "Spell check" (Português Brasil).
- **Files & Links:** 
  - `Default location for new notes`: "Same folder as current file".
  - `New link format`: "WikiLinks".
  - `Use [[WikiLinks]] for internal links`: Ativado.
