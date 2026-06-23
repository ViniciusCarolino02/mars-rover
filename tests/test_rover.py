import sys
sys.path.insert(0, r'C:\Users\vinic\mars-rover')

from rover import Rover

# Testes de rotação
def test_turn_left():
    rover = Rover(0, 0, 'N', 5, 5)
    rover.turn_left()
    assert rover.direction == 'L'

def test_turn_right():
    rover = Rover(0, 0, 'N', 5, 5)
    rover.turn_right()
    assert rover.direction == 'O'

# Teste do exemplo básico da spec
def test_exemplo_basico():
    rover = Rover(1, 2, 'N', 5, 5)
    rover.execute('LMLMLMLMM')
    assert rover.status() == '1 3 N'

# Testes de borda
def test_borda_sul():
    rover = Rover(0, 0, 'S', 5, 5)
    rover.execute('MMM')
    assert rover.status() == '0 0 S'

def test_borda_oeste():
    rover = Rover(0, 0, 'L', 5, 5)
    rover.execute('MMM')
    assert rover.status() == '0 0 L'

def test_borda_norte():
    rover = Rover(0, 4, 'N', 5, 5)
    rover.execute('MMM')
    assert rover.status() == '0 4 N'

def test_borda_leste():
    rover = Rover(4, 0, 'O', 5, 5)
    rover.execute('MMM')
    assert rover.status() == '4 0 O'

# Testes de obstáculo
def test_obstaculo_para_rover():
    rover = Rover(0, 2, 'O', 5, 5)
    rover.obstacles = [(2, 2)]
    rover.execute('MMM')
    assert rover.status() == 'BLOCKED 1 2 O'

def test_obstaculo_ignora_comandos_restantes():
    rover = Rover(0, 2, 'O', 5, 5)
    rover.obstacles = [(1, 2)]
    rover.execute('MMMM')
    assert rover.status() == 'BLOCKED 0 2 O'