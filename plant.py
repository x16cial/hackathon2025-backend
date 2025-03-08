#plant.py
import random

class Plant:
    def __init__(self, x, y, energy=5, plant_type='low'):
        self.x = x
        self.y = y
        self.energy = int(energy)  # ✅ Asegurar que siempre sea un número
        self.plant_type = plant_type  # 'low' o 'high'
        self.state = 'live'
        self.ticks_alive = 0  # Contador de ticks de vida

    def photosynthesize(self):
        """Gana energía a través de la fotosíntesis."""
        self.energy += 2  # Aumenta la energía con cada tick

    def update(self, grid):
        """Ejecuta sus acciones cada tick."""
        self.photosynthesize()
        self.grow(grid)

        # Si la energía llega a 0, la planta muere
        if self.energy <= 0:
            self.state = 'dead'

    def check_death(self):
        """La planta muere después de 30 ticks (+/-3 de variación)."""
        if self.ticks_alive >= 30 + random.randint(-3, 3):
            self.state = 'dead'

class PlantLow(Plant):
    def __init__(self, x, y, energy=5):
        super().__init__(x, y, plant_type='low', energy=energy)

    def grow(self, grid):
        """Crecimiento y reproducción de la planta."""
        if self.state == 'dead':
            return

        self.ticks_alive += 1  # Incrementar ticks de vida

        # Transformarse en PlantHigh después de 16-24 ticks
        if self.ticks_alive >= 16 and random.random() < 0.5:
            grid[self.y][self.x] = PlantHigh(self.x, self.y, energy=self.energy)
            return

        # Reproducción de la planta baja con 30% de probabilidad cada 8 ticks
        if self.ticks_alive % 8 == 0 and random.random() < 0.3:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            valid_positions = []
            for dx, dy in directions:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] is None:
                    valid_positions.append((nx, ny))

            if valid_positions:
                new_x, new_y = random.choice(valid_positions)
                grid[new_y][new_x] = PlantLow(new_x, new_y, energy=5)

class PlantHigh(Plant):
    def __init__(self, x, y, energy=10):
        super().__init__(x, y, plant_type='high', energy=energy)

    def grow(self, grid):
        """Crecimiento y reproducción de la planta."""
        if self.state == 'dead':
            return

        self.ticks_alive += 1  # Incrementar ticks de vida

        # Reproducción de la planta alta con 30% de probabilidad cada 8 ticks
        if self.ticks_alive % 8 == 0 and random.random() < 0.3:
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            valid_positions = []
            for dx, dy in directions:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and grid[ny][nx] is None:
                    valid_positions.append((nx, ny))

            if valid_positions:
                new_x, new_y = random.choice(valid_positions)
                grid[new_y][new_x] = PlantLow(new_x, new_y, energy=3)  # Usamos PlantLow directamente
                self.energy -= 1  # Usa energía al reproducirse

    def check_death(self):
        """La planta muere después de 30 ticks (+/-3 de variación)."""
        if self.ticks_alive >= 30 + random.randint(-3, 3):
            self.state = 'dead'