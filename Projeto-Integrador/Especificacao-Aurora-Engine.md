---
tipo: especificacao
projeto: Aurora-DAG-Engine
versao: 1.0
status: rascunho
tags: [architecture, dag, orchestration, data-engineering]
---
# 📘 Especificação Técnica: Aurora DAG Engine

## 1. Visão Geral
O **Aurora DAG Engine** é um motor de orquestração de tarefas baseado em Grafos Acíclicos Direcionados (DAGs). O sistema permite a definição de dependências entre tarefas, valida a integridade do fluxo (ausência de ciclos) e executa as tarefas na ordem correta de dependência, otimizando a execução via paralelismo.

## 2. Objetivos de Engenharia (High Standards)
- **Integridade:** Garantia matemática de que não existam ciclos nas dependências.
- **Eficiência:** Execução de tarefas independentes em paralelo.
- **Abstração:** Desacoplamento entre o orquestrador e a implementação da tarefa (estratégia de Command Pattern).
- **Observabilidade:** Rastreabilidade total de cada execução via logs estruturados.

## 3. Arquitetura de Componentes

### 3.1. Camada de Modelo (`models.py`)
- **`Task` (Abstract Base Class):**
    - Atributos: `name`, `status` (PENDING, RUNNING, SUCCESS, FAILED), `retry_count`, `max_retries`.
    - Métodos: `execute()` (abstrato).
- **`SQLTask` & `PythonTask`:** Implementações concretas de `Task`.
- **`DAG`:**
    - Atributos: `nodes` (mapa de nome $\rightarrow$ Task), `edges` (lista de adjacência).
    - Métodos: `add_task()`, `add_dependency()`, `validate()`.

### 3.2. Camada de Validação (`validator.py`)
- **`CycleDetector`:**
    - Algoritmo: DFS com marcação de três cores (Branco, Cinza, Preto).
    - Objetivo: Lançar `CircularDependencyError` se um nó "Cinza" for reencontrado.

### 3.3. Camada de Orquestração (`scheduler.py`)
- **`AuroraScheduler`:**
    - Algoritmo: Ordenação Topológica (Kahn's Algorithm).
    - Fluxo:
        1. Calcula `in-degree` de todos os nós.
        2. Alimenta uma `ReadyQueue` com nós de `in-degree == 0`.
        3. Dispara a execução via `ThreadPoolExecutor`.
        4. Ao finalizar uma tarefa, decrementa o `in-degree` dos filhos.
        5. Adiciona novos nós prontos à `ReadyQueue`.

### 3.4. Camada de Observabilidade (`logger.py`)
- **`PipelineLogger`:**
    - Implementação de logs formatados: `[TIMESTAMP] [TASK_NAME] [STATUS] -> Message`.
    - Exportação de um sumário final de execução.

## 4. Fluxo de Execução (Life Cycle)
1. **Definição:** O usuário instancia a `DAG` e adiciona as `Tasks` e suas dependências.
2. **Validação:** O `AuroraScheduler` chama o `CycleDetector`. Se falhar $\rightarrow$ Stop.
3. **Planejamento:** O Scheduler gera a ordem topológica inicial.
4. **Execução:**
    - As tarefas prontas são enviadas para o pool de threads.
    - O sistema monitora a conclusão e libera as dependências subsequentes.
5. **Finalização:** O sistema gera o relatório de performance e status.

## 5. Critérios de Aceite (Definição de Pronto)
- [ ] O sistema detecta ciclos e impede a execução.
- [ ] Tarefas independentes rodam em paralelo (verificável via timestamps de log).
- [ ] Falhas em tarefas são tratadas com a lógica de retry configurada.
- [ ] O sistema suporta a execução de scripts SQL e funções Python.
- [ ] Complexidade de agendamento mantida em $O(V + E)$.

---
**Aprovação:** 
- [ ] Arquitetura validada por: [User]
- [ ] Data: 2026-11-03
