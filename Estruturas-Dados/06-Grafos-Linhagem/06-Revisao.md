---
tipo: revisao
trilha: estruturas-dados
capitulo: 06
titulo: "Revisão: Grafos & Linhagem"
nivel: 5
tempo_estimado_h: 1
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-12-30
tags: [revisao, graphs, dag, linetage]
---
# Revisão: Grafos & Linhagem

> [!abstract] Capítulo 06 · Revisão de Orquestração de Dados
> ⏱ 1h · 🎯 Nível 5/5 · 🔗 Pré-requisitos: [[Estruturas-Dados/06-Grafos-Linhagem/01-Aula]] · 📦 Entrega: [[Estruturas-Dados/06-Grafos-Linhagem/07-Entrega-Projeto]] · ✅ Verificado

## 🎯 Checklist de Competências
Verifique se você consegue responder "Sim" para cada item abaixo:

- [ ] **Representação:** Sei quando usar Matriz de Adjacência vs Lista de Adjacência?
- [ ] **Busca:** Consigo implementar BFS para caminhos mínimos e DFS para exploração profunda?
- [ ] **DAGs:** Entendo por que ciclos são proibidos em orquestradores de dados?
- [ ] **Ordenação:** Sei implementar a Ordenação Topológica para definir a sequência de execução de tarefas?
- [ ] **Linhagem:** Consigo modelar a propagação de impacto (downstream) em um grafo de tabelas?

## 🧠 Mapa Mental de Conceitos

**Grafos $\rightarrow$**
- **Básico $\rightarrow$** Vértices (Nós) $\rightarrow$ Arestas (Conexões) $\rightarrow$ Pesos.
- **Busca $\rightarrow$** BFS (Queue $\rightarrow$ Nível) $\rightarrow$ DFS (Stack $\rightarrow$ Profundidade).
- **Orquestração $\rightarrow$** DAG $\rightarrow$ Sem Ciclos $\rightarrow$ Ordenação Topológica $\rightarrow$ Fluxo de Trabalho.
- **Linhagem $\rightarrow$** Upstream (Origem) $\rightarrow$ Downstream (Impacto).

**Algoritmos Chave $\rightarrow$**
- **Kahn's Algorithm:** Base para a execução de DAGs.
- **BFS:** Ideal para achar o menor caminho em saltos.
- **DFS:** Ideal para detectar ciclos e explorar caminhos completos.

## 🚀 Desafio de Fixação Rápida
**Cenário:** Você tem 5 tabelas (A, B, C, D, E). 
- B e C dependem de A.
- D depende de B.
- E depende de C e D.

**Pergunta:** Qual a ordem de execução correta e quem é a "folha" final do pipeline?
**Resposta:** A $\rightarrow$ B $\rightarrow$ C (ou C $\rightarrow$ B) $\rightarrow$ D $\rightarrow$ E. A folha final é a tabela E.

## 🔗 Links Rápidos
- Aula Teórica: [[Estruturas-Dados/06-Grafos-Linhagem/01-Aula]]
- Lab Prático: [[Estruturas-Dados/06-Grafos-Linhagem/02-Lab]]
- Tickets de Orquestração: [[Estruturas-Dados/06-Grafos-Linhagem/03-Tickets]]

---
← [[Estruturas-Dados/06-Grafos-Linhagem/05-Flashcards]] · [[MOC-Estruturas-Dados]] · [[Estruturas-Dados/06-Grafos-Linhagem/07-Entrega-Projeto]] →
