import os
import pygame

# Game Piece parent class
class GamePiece:
    def __init__(self, pos, piece, color):
        # type is the type of the piece color is B or W and sprite will be the image
        self.piece = piece
        self.color = color
        self.sprite_path = None
        self.sprite = None
        # may need to access piece location in future, adding as safety
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
    
    # get sprite path
    def get_sprite(self):
        return os.path.join(os.getcwd(), f'assets/images/{self.color}_{self.piece}.png')

    # load sprite image
    def load_sprite(self, path):
        sprite = pygame.image.load(path)
        return pygame.Surface.convert(sprite)
    
    # move function for piece
    def move(self, board):
        pass