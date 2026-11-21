"""Базовый класс для моделей игры."""


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self, screen_width, screen_height):
        """Инициализирует общие атрибуты."""
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.position = (screen_width // 2, screen_height // 2)
        self.body_color = None
