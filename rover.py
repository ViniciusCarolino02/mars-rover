DIRECTIONS = ['N', 'L', 'S', 'O']

class Rover:
    def __init__(self, x, y, direction, grid_w, grid_h, obstacles=None):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.obstacles = obstacles or []
        self.blocked = False

    def turn_left(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx + 1) % 4]

    def turn_right(self):
        idx = DIRECTIONS.index(self.direction)
        self.direction = DIRECTIONS[(idx - 1) % 4]

    def next_position(self):
        moves = {'N': (0, 1), 'S': (0, -1), 'L': (-1, 0), 'O': (1, 0)}
        dx, dy = moves[self.direction]
        return self.x + dx, self.y + dy

    def move(self):
        nx, ny = self.next_position()
        if nx < 0 or nx >= self.grid_w or ny < 0 or ny >= self.grid_h:
            return  # bloqueia na borda
        if (nx, ny) in self.obstacles:
            self.blocked = True
            return  # bloqueia no obstáculo
        self.x = nx
        self.y = ny

    def execute(self, commands):
        for cmd in commands:
            if self.blocked:
                break
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'M':
                self.move()

    def status(self):
        if self.blocked:
            return f"BLOCKED {self.x} {self.y} {self.direction}"
        return f"{self.x} {self.y} {self.direction}"