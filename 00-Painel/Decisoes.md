# Decisões de Design do Vault

Este arquivo registra as escolhas técnicas feitas durante a construção do vault para futura manutenção.

## 🛠 Escolhas Tecnológicas
- **PostgreSQL 16+:** Escolhido como banco alvo por ser o padrão da indústria para bancos relacionais open-source e possuir implementações robustas de Window Functions e CTEs.
- **Python 3.12+:** Utilizado para aproveitar as melhorias de performance e as novas funcionalidades de Type Hinting.
- **SQLAlchemy 2.0:** Implementado obrigatoriamente para garantir a transição para o estilo declarativo moderno (estilo `select()` em vez de `.query()`).
- **Pytest 8.x:** Escolhido para a autocorreção dos tickets por ser o padrão de fato para testes em Python.

## 📊 Dataset "Loja Aurora"
- **Abordagem:** Um único domínio (E-commerce) para todas as trilhas. Isso reduz a carga cognitiva do aluno, que não precisa aprender um novo contexto a cada capítulo.
- **Defeitos:** Introduzidos propositalmente (Nulos, datas futuras, nomes de colunas errados) para que a trilha de Engenharia de Dados (Camada Silver) tenha "trabalho real" de limpeza.

## 📐 Estrutura de Fixação
- **Intercalação:** O plano de estudos força a alternância entre Python e SQL para evitar a "ilusão de competência" que ocorre ao estudar a mesma coisa por dias seguidos.
- **Predição:** O método "Preveja $\rightarrow$ Execute $\rightarrow$ Compare" no Lab é baseado em evidências de neurociência para aumentar a retenção.

## 📁 Organização de Arquivos
- **Templates:** Separados para facilitar a criação de novos capítulos.
- **00-Painel:** Centraliza a gestão do estudo, transformando o vault em um software de gestão de aprendizado.
