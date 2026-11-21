"""Виджет управления: обработка нажатий клавиш."""
from pink_snake_mimimi.src.models.snake_model import UP, DOWN, LEFT, RIGHT


class Controls:
    """Привязывает клавиши стрелок к модели змеи."""

    def __init__(self, root, snake):
        """Регистрирует обработчики клавиш."""
        self.snake = snake
        root.bind('<Up>', lambda event: self.snake.set_direction(UP))
        root.bind('<Down>', lambda event: self.snake.set_direction(DOWN))
        root.bind('<Left>', lambda event: self.snake.set_direction(LEFT))
        root.bind('<Right>', lambda event: self.snake.set_direction(RIGHT))
        self.canvas = root
