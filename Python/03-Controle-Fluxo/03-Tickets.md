---
tipo: ticket
trilha: python
capitulo: 03
titulo: "Tickets de Controle de Fluxo"
nivel: 2
tempo_estimado_h: 2
dominio: 0
status: nao-iniciado
verificado: true
versao_doc: "3.12"
proxima_revisao: 2026-11-16
tags: [ticket, loops, performance]
---
# Tickets: Controle de Fluxo

> [!abstract] Capítulo 03 · Tickets de Controle de Fluxo
> ⏱ 2h · 🎯 Nível 2/5 · 🔗 Pré-requisitos: [[Python/03-Controle-Fluxo/02-Lab]] · 📦 Entrega: [[Python/03-Controle-Fluxo/07-Entrega-Projeto]] · ✅ Verificado

## 🎫 TICKET P03-01: O Filtro de Junk Data (PREDIZER)
**Prioridade:** Média | **Tipo:** Feature | **Tempo:** 30min
> **Contexto:** O dataset de clientes contém linhas vazias ou com a palavra `"NULL"`. Precisamos de uma lista apenas com clientes válidos.
> **Entrada:** `["Alice", "NULL", "Bob", "", "Charlie", "NULL"]`.
> **Saída Esperada:** `["Alice", "Bob", "Charlie"]`.

**✅ Critério de Aceite:** 
- [ ] Usar list comprehension.
- [ ] Filtrar strings vazias e a string `"NULL"`.

**💡 Dicas:**
> [!tip] Nível 1
> Use `if item and item != "NULL"`.
> 
> [!tip] Nível 2
> Lembre-se que em Python, strings vazias são avaliadas como `False`.

**🧪 Como Verificar:** 
Rodar o script e comparar a saída com a lista esperada.

---

## 🎫 TICKET P03-02: Alerta de Pico de Carga (ESCREVER)
**Prioridade:** Alta | **Tipo:** Feature | **Tempo:** 60min
> **Contexto:** Um sistema de monitoramento de CPU envia valores a cada segundo. Precisamos de um script que dispare um alerta se a CPU ficar acima de 90% por 3 leituras consecutivas.
> **Entrada:** Fluxo de valores `[70, 85, 92, 95, 91, 60, 99]`.
> **Saída Esperada:** Imprimir "ALERTA: Pico de Carga!" no momento em que a 3ª leitura consecutiva ocorrer.

**✅ Critério de Aceite:** 
- [ ] Não disparar alerta se houver apenas 1 ou 2 leituras altas.
- [ ] Resetar o contador se houver uma leitura abaixo de 90%.

**💡 Dicas:**
> [!tip] Nível 1
> Use um contador externo ao loop `for`.
> 
> [!tip] Nível 2
> Quando o contador chegar a 3, dispare o alerta e resete-o (ou use `break`).

**🧪 Como Verificar:** 
Testar com as sequências `[91, 91, 91]` (Alerta) e `[91, 91, 80, 91]` (Sem alerta).

---

## 🎫 TICKET P03-03: Otimização de Busca (OTIMIZAR)
**Prioridade:** Média | **Tipo:** Performance | **Tempo:** 60min
> **Contexto:** Um script busca um ID de transação em uma lista de 1 milhão de itens usando um loop `for`. O processo está lento.
> **Entrada:** Lista de 1M de IDs e um `target_id`.
> **Saída Esperada:** O índice do ID ou -1 se não encontrado.

**✅ Critério de Aceite:** 
- [ ] Reduzir o tempo de execução.
- [ ] Implementar a busca usando a palavra-chave `in` ou o método `.index()`.

**💡 Dicas:**
> [!tip] Nível 1
> O loop `for` manual é lento. O operador `in` é implementado em C e é muito mais rápido.
> 
> [!tip] Nível 2
> Se a busca for repetitiva, a melhor solução é converter a lista para um `set` (Hash Set), mudando a complexidade de $O(n)$ para $O(1)$.

**🧪 Como Verificar:** 
Usar o módulo `time` para medir a execução do loop `for` vs o operador `in`.

---

## 🆘 Travei!
Se travar 2 vezes, revise: [[Python/03-Controle-Fluxo/01-Aula]] ou [[Python/03-Controle-Fluxo/02-Lab]].
