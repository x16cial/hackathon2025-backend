#animal.py
import random

class AnimalSmall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 'small'
        self.hp = 5
        self.ticks_alive = 0
        self.consecutive_ticks_without_consuming = 0
        self.state = 'live'

    def move(self, grid):
        """Se mueve aleatoriamente de 1 a 3 celdas en una dirección aleatoria."""
        if self.state == 'dead':
            return

        directions = ['up', 'down', 'left', 'right']
        direction = random.choice(directions)
        move_distance = random.randint(1, 3)

        nx, ny = self.x, self.y  # Posición actual

        if direction == 'up' and self.y - move_distance >= 0:
            ny -= move_distance
        elif direction == 'down' and self.y + move_distance < len(grid):
            ny += move_distance
        elif direction == 'left' and self.x - move_distance >= 0:
            nx -= move_distance
        elif direction == 'right' and self.x + move_distance < len(grid[0]):
            nx += move_distance

        # Asegurar que el movimiento no colisione con otro objeto
        if grid[ny][nx] is None:
            grid[self.y][self.x] = None  # Vaciar la celda anterior
            self.x, self.y = nx, ny
            grid[self.y][self.x] = self

        self.ticks_alive += 1  # Incrementar ticks

        # Revisión de consumo de plantas después del movimiento
        self.consume_plant(grid)

        # Evolución a AnimalBig después de 12 ticks
        if self.ticks_alive >= 12:
            self.size = 'big'
            grid[self.y][self.x] = AnimalBig(self.x, self.y)

        # Muerte si no come en 3 ticks
        if self.consecutive_ticks_without_consuming >= 3:
            self.state = 'dead'

    def consume_plant(self, grid):
        """Consume una planta aleatoria cerca del animal."""
        plants_nearby = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    cell = grid[ny][nx]
                    if hasattr(cell, 'plant_type') and cell.plant_type == 'low':
                        plants_nearby.append(cell)

        if plants_nearby:
            plant = random.choice(plants_nearby)
            plant.energy -= 1  # Small solo puede comer PlantLow
            self.consecutive_ticks_without_consuming = 0  # Reiniciar contador de hambre
        else:
            self.consecutive_ticks_without_consuming += 1  # No encontró comida, aumenta hambre

    def check_death(self):
        """El animal muere después de 24 ticks (+/-1 de variación)."""
        if self.ticks_alive >= 24 + random.randint(-1, 1):  # Límite de vida
            self.state = 'dead'

    def check_reproduction(self, grid):
        """Genera un nuevo animal si hay otro cerca con 50% de probabilidad."""
        if self.ticks_alive % 6 == 0:  # Cada 6 ticks
            nearby_animals = []
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx = self.x + dx
                    ny = self.y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        cell = grid[ny][nx]
                        if hasattr(cell, 'size') and cell.size in ['small', 'big']:
                            nearby_animals.append(cell)

            if nearby_animals and random.random() < 0.5:
                x, y = self.x, self.y
                while grid[y][x] is not None:  # Buscar una celda vacía
                    x = random.randint(0, len(grid[0]) - 1)
                    y = random.randint(0, len(grid) - 1)
                grid[y][x] = AnimalSmall(x, y)

class AnimalBig(AnimalSmall):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.size = 'big'
        self.hp = 10

    def consume_plant(self, grid):
        """Consume una planta aleatoria cerca del animal."""
        plants_nearby = []
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    cell = grid[ny][nx]
                    if hasattr(cell, 'plant_type') and cell.plant_type in ['low', 'high']:
                        plants_nearby.append(cell)

        if plants_nearby:
            plant = random.choice(plants_nearby)
            if plant.plant_type == 'high':
                plant.energy -= 2  # Big consume 2 de PlantHigh
            elif plant.plant_type == 'low':
                plant.energy -= 1  # Big consume 1 de PlantLow
            self.consecutive_ticks_without_consuming = 0  # Reiniciar contador de hambre
        else:
            self.consecutive_ticks_without_consuming += 1  # No encontró comida, aumenta hambre