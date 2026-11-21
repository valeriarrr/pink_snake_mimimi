"""Класс Renderer: отрисовка игры на Canvas."""

GRID_SIZE = 20
BORDER_COLOR = '#B39DDB'
BOARD_BACKGROUND_COLOR = '#0A0F2C'
SNAKE_COLOR = '#FFB6C1'
APPLE_COLOR = '#FF3333'
APPLE_LEAF_COLOR = '#4CAF50'
EYE_COLOR = '#000000'


class Renderer:
    """Рисует модели на tkinter.Canvas."""

    def __init__(self, canvas, snake, apple):
        """Сохраняет canvas и модели."""
        self.canvas = canvas
        self.snake = snake
        self.apple = apple

    def _draw_apple(self, position):
        """Рисует яблоко (круг, палочка, листик)."""
        x, y = position
        cx = x + GRID_SIZE / 2
        cy = y + GRID_SIZE / 2
        r = GRID_SIZE / 2 - 1

        self.canvas.create_oval(x, y, x + GRID_SIZE, y + GRID_SIZE, fill=APPLE_COLOR, outline='')
        self.canvas.create_line(cx, cy - r, cx, cy - r - 4, fill='#8B4513', width=2)
        self.canvas.create_oval(cx, cy - r - 3, cx + 6, cy - r + 3, fill=APPLE_LEAF_COLOR, outline='')

    def _draw_snake(self):
        """Рисует змею, добавляя глаза на голову."""
        for i, position in enumerate(self.snake.positions):
            x, y = position
            
            # Рисуем сегмент змеи (квадрат)
            self.canvas.create_rectangle(
                x, y, x + GRID_SIZE, y + GRID_SIZE,
                fill=SNAKE_COLOR, outline=BORDER_COLOR, width=2
            )
            
            # Если это голова - рисуем глаза
            if i == 0:
                eye_r = 3
                
                # Левый глаз
                self.canvas.create_oval(
                    x + 4, y + 4, 
                    x + 4 + eye_r*2, y + 4 + eye_r*2, 
                    fill=EYE_COLOR, outline=''
                )
                # Правый глаз
                self.canvas.create_oval(
                    x + GRID_SIZE - 4 - eye_r*2, y + 4, 
                    x + GRID_SIZE - 4, y + 4 + eye_r*2, 
                    fill=EYE_COLOR, outline=''
                )

    def draw(self):
        """Полностью перерисовывает кадр."""
        self.canvas.delete('all')
        self.canvas.configure(bg=BOARD_BACKGROUND_COLOR)
        self._draw_apple(self.apple.position)
        self._draw_snake()
