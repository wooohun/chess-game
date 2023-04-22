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
        self.sprite = os.path.join(f'assets/images/{self.color}_{self.name}.png')

    # load sprite image
    def load_sprite(self, path):
        return pygame.image.load(path)
    
    # move function for piece
    def move(self, board):
        pass
    
#  ----------------------------------------------------- #
#  Child Classes describing each unique piece


class Pawn(GamePiece):
    def __init__(self, pos, piece, color):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)

class knight(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('Kn', color, sprite)

class Rook(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('R', color, sprite)

class Bishop(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('B', color, sprite)

class King(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('K', color, sprite)

class Queen(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('Q', color, sprite)
