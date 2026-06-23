# Spec: Mars Rover

## Visão geral
Um rover robótico pousa num platô retangular em Marte.
O software controla o movimento do rover dentro dessa grade.

## Grade
- Tamanho definido por largura W e altura H
- Coordenadas começam em (0, 0) no canto inferior esquerdo
- Coordenada máxima é (W-1, H-1)

## Rover
- Tem uma posição (x, y) e uma direção: N, S, L, O
- Recebe uma sequência de comandos em texto

## Comandos
- L: gira 90 graus à esquerda, sem mover
- R: gira 90 graus à direita, sem mover
- M: anda uma célula na direção atual

## Comportamento de borda
- Se o rover tentar sair da grade, o movimento é ignorado
- O rover fica na posição atual e continua processando os próximos comandos
- Decisão: bloquear é mais realista para um rover real em Marte

## Detecção de obstáculo
- A grade pode conter obstáculos em posições específicas
- Se o próximo passo for um obstáculo, o rover para imediatamente
- Os comandos restantes são ignorados
- O rover reporta a posição onde travou e o motivo

## Saída
- Posição final: "X Y DIREÇÃO" (ex: "1 3 N")
- Se travou em obstáculo: "BLOCKED X Y DIREÇÃO" (ex: "BLOCKED 2 2 N")

## Exemplos

### Exemplo 1 — movimento básico
- Grade: 5x5
- Posição inicial: 1 2 N
- Comandos: LMLMLMLMM
- Saída esperada: 1 3 N

### Exemplo 2 — bloqueio na borda
- Grade: 5x5
- Posição inicial: 0 0 S
- Comandos: MMM
- Saída esperada: 0 0 S
  (rover tenta ir pra sul mas já está na borda, fica no lugar)

### Exemplo 3 — obstáculo no caminho
- Grade: 5x5
- Obstáculos: (2, 2)
- Posição inicial: 0 2 L
- Comandos: MMM
- Saída esperada: BLOCKED 1 2 L
  (rover anda até (1,2), tenta ir pra (2,2) mas tem obstáculo, para e reporta)