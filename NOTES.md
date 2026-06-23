# NOTES.md

## Decisões tomadas

### Comportamento de borda
Escolhi bloquear o rover quando tenta sair da grade.
Justificativa: um rover real em Marte não pode teletransportar,
bloquear é o comportamento mais seguro e realista.

### Detecção de obstáculo
Quando o próximo passo é um obstáculo, o rover para imediatamente
e reporta a posição com "BLOCKED X Y DIREÇÃO".
Os comandos restantes são ignorados por segurança.

## Onde a IA ajudou
- Gerou a estrutura inicial do código e dos testes
- Sugeriu a lista de direções como array para facilitar rotação
- Identificou a necessidade do conftest.py para resolver o import

## Onde precisei corrigir
- O arquivo rover.py foi criado na pasta errada (specs/) em vez da raiz
- Foi necessário adicionar conftest.py para o pytest encontrar o módulo

## O que faria diferente
- Teria verificado a estrutura de pastas antes de rodar os testes
- Teria criado os testes antes do código (TDD de verdade)
- Teria feito commits menores, um por comportamento implementado