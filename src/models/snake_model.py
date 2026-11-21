"""Модель змеи."""
from random import choice

from pink_snake_mimimi.src.models.animation_model import GameObject


GRID_SIZE = 20

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class SnakeModel(GameObject):
    """Логика движения, роста и сброса змеи."""

    def __init__(self, screen_width, screen_height):
        """Инициализирует змею."""
        super().__init__(screen_width, screen_height)
        self.body_color = 'green'
        self.length = 1
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None

    def update_direction(self):
        """Применяет отложенное направление."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def get_head_position(self):
        """Возвращает координаты головы."""
        return self.positions[0]

    def move(self):
        """Двигает змею на одну клетку."""
        head = self.get_head_position()
        new_head = (
            (head[0] + self.direction[0] * GRID_SIZE) % self.screen_width,
            (head[1] + self.direction[1] * GRID_SIZE) % self.screen_height,
        )
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

        if new_head in self.positions[1:]:
            self.reset()

    def reset(self):
        """Возвращает змею в начальное состояние."""
        self.length = 1
        self.positions = [self.position]
        self.direction = choice([UP, DOWN, LEFT, RIGHT])
        self.next_direction = None

    def set_direction(self, direction):
        """Устанавливает новое направление, если оно не противоположное."""
        opposites = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
        if opposites.get(direction) != self.direction:
            self.next_direction = direction
