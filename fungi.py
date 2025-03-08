#fungi.py
import random

class Fungi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = 3  # Un hongo comienza con 3 de vida
        self.state = 'live'
        self.ticks_alive = 0  # Contador de ticks de vida

    def grow(self, grid):
        """Crece si hay entidades muertas cerca y las elimina con probabilidad."""
        if self.state == 'dead':
            return

        self.ticks_alive += 1  # Incrementar ticks de vida

        found_dead = False
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = self.x + dx
                ny = self.y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    cell = grid[ny][nx]
                    # Verificar si la celda contiene una entidad muerta
                    if hasattr(cell, 'state') and cell.state == 'dead':
                        self.hp += 1  # Absorbe nutrientes
                        found_dead = True

        # Si hay cadáveres, chance del 20% de eliminarlos
        if found_dead and random.random() < 0.2:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx = self.x + dx
                    ny = self.y + dy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        cell = grid[ny][nx]
                        if hasattr(cell, 'state') and cell.state == 'dead':
                            grid[ny][nx] = None  # Eliminar cadáver
                            break  # Solo elimina un cadáver por tick

    def check_death(self):
        """El hongo muere si su HP llega a 0 o negativo."""
        if self.hp <= 0:
            self.state = 'dead'