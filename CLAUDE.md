# Mars Rover — CLAUDE.md

## Objetivo
Implementar o controle de um rover robótico numa grade retangular,
seguindo a metodologia SDD (Spec-Driven Development).

## Linguagem e ferramentas
- Python 3
- pytest para testes
- Sem dependências externas além do pytest

## Decisões de design
- **Borda:** o rover bloqueia ao tentar sair da grade (não executa o movimento)
- **Obstáculo:** se o próximo passo for um obstáculo, o rover para imediatamente
  e sinaliza a posição onde travou. Os comandos restantes são ignorados.

## Convenções
- Todo comportamento novo começa com um teste que falha
- Commits a cada marco que funciona
- A spec em specs/mars-rover.md é a fonte da verdade

## Definição de "pronto"
- Todos os testes passando
- Comportamento base implementado
- Detecção de obstáculo implementada
- Comportamento de borda implementada
- NOTES.md preenchido