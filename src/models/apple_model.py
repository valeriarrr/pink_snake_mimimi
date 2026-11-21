"""Модель яблока."""
from random import randint

from pink_snake_mimimi.src.models.animation_model import GameObject


GRID_SIZE = 20


class AppleModel(GameObject):
    """Логика и положение яблока."""

    def __init__(self, screen_width, screen_height):
        """Инициализирует яблоко и его положение."""
        super().__init__(screen_width, screen_height)
        self.body_color = 'red'
        self.randomize_position()

    def randomize_position(self):
        """Случайно выбирает новое положение яблока в пределах поля."""
        cols = self.screen_width // GRID_SIZE
        rows = self.screen_height // GRID_SIZE
        self.position = (randint(0, cols - 1) * GRID_SIZE,
                         randint(0, rows - 1) * GRID_SIZE)
