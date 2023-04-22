import pygame
import config

class BoardSquare:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.set_color = 'light' if (x + y) % 2 == 0 else 'dark'
        self.color = (0, 0, 0) if self.set_color == 'light' else (255, 255, 255)
        # add color for highlighted squares later
        self.cur_piece = None
        # creates the Rectangle Object 
        self.square = pygame.Rect(
            self.x * config.SQUARE_W,
            self.y * config.SQUARE_H,
            config.SQUARE_W,
            config.SQUARE_H
        )
        self.highlight = False
    

    # function to update current square
    def update(self, surface):
        # generate visual representation of current square
        pygame.draw.rect(surface, self.color, self.square)
    