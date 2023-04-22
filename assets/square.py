import pygame
import assets.utils.config as config

class BoardSquare:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coords = (x, y)
        self.fixed_x = x * config.SQUARE_W
        self.fixed_y = y * config.SQUARE_H
        self.fixed_coords = (self.fixed_x, self.fixed_y)
        self.set_color = 'dark' if (x + y) % 2 == 0 else 'light'
        self.color = (0, 0, 0) if self.set_color == 'light' else (255, 255, 255)
        # add color for highlighted squares later
        self.h_color = None
        self.cur_piece = None
        # creates the Rectangle Object 
        self.square = pygame.Rect(
            self.fixed_x,
            self.fixed_y,
            config.SQUARE_W,
            config.SQUARE_H
        )
        self.highlight = False
    

    # function to update current square
    def update(self, surface):
        # generate visual representation of current square
        if self.highlight:
            pygame.draw.rect(surface, self.h_color, self.square)
        else: 
            pygame.draw.rect(surface, self.color, self.square)
        
        # update with tile occupant
        if self.cur_piece != None:
            cur_rect = self.cur_piece.sprite.get_rect()
            cur_rect.center = self.square.center
            surface.blit(self.cur_piece.sprite, cur_rect)

    