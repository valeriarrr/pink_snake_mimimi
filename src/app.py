"""Класс App: окно и главный игровой цикл."""
import tkinter as tk

from pink_snake_mimimi.src.models.snake_model import SnakeModel
from pink_snake_mimimi.src.models.apple_model import AppleModel
from pink_snake_mimimi.src.renderers.renderer import Renderer
from pink_snake_mimimi.src.widgets.controls import Controls


class App:
    """Главное окно приложения и игровой цикл."""

    SCREEN_WIDTH = 640
    SCREEN_HEIGHT = 480
    SPEED_MS = 100  # задержка между кадрами в миллисекундах

    def __init__(self):
        """Инициализирует окно, модели, рендерер и управление."""
        self.root = tk.Tk()
        self.root.title('Змейка')
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(
            self.root,
            width=self.SCREEN_WIDTH,
            height=self.SCREEN_HEIGHT,
            bg='black',
        )
        self.canvas.pack()

        self.snake = SnakeModel(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.apple = AppleModel(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self.renderer = Renderer(self.canvas, self.snake, self.apple)
        self.controls = Controls(self.root, self.snake)

        self.running = True

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.after(self.SPEED_MS, self._game_loop)
        self.root.mainloop()

    def _game_loop(self):
        """Один шаг игрового цикла."""
        if not self.running:
            return

        self.snake.update_direction()

        if self.snake.get_head_position() == self.apple.position:
            self.snake.length += 1
            self.apple.randomize_position()

        self.snake.move()
        self.renderer.draw()
        self.root.after(self.SPEED_MS, self._game_loop)
