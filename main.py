from rover import Rover

# Configuração
grid_w = 5
grid_h = 5
obstaculos = [(3, 3)]

# Posição inicial
x = int(input("Posição X inicial: "))
y = int(input("Posição Y inicial: "))
direcao = input("Direção inicial (N/S/L/O): ").upper()
comandos = input("Comandos (ex: MMLMRM): ").upper()

# Executa
rover = Rover(x, y, direcao, grid_w, grid_h, obstaculos)
rover.execute(comandos)

print(f"\nResultado: {rover.status()}")