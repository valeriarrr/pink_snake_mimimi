"""Класс Renderer: отрисовка игры на Canvas."""
from pink_snake_mimimi.src.models.snake_model import RIGHT  # noqa: F401 (необязательно)


GRID_SIZE = 20
BORDER_COLOR = '#5dd8e4'
BOARD_BACKGROUND_COLOR = 'black'


class Renderer:
    """Рисует модели на tkinter.Canvas."""

    def __init__(self, canvas, snake, apple):
        """Сохраняет canvas и модели."""
        self.canvas = canvas
        self.snake = snake
        self.apple = apple

    def _draw_cell(self, position, color):
        """Рисует одну клетку с рамкой."""
        x, y = position
        self.canvas.create_rectangle(
            x, y, x + GRID_SIZE, y + GRID_SIZE,
            fill=color, outline=BORDER_COLOR,
        )

    def draw(self):
        """Полностью перерисовывает кадр."""
        self.canvas.delete('all')
        self._draw_cell(self.apple.position, self.apple.body_color)
        for position in self.snake.positions:
            self._draw_cell(position, self.snake.body_color)
