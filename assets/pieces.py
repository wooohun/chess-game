import os

# Game Piece parent class
class GamePiece:
    def __init__(self, type, color, sprite = None):
        #type is the type of the piece color is B or W and sprite will be the image
        self.type = type
        self.color = color
        self.sprite = sprite
        self.get_sprite()

    #sprite of each piece
    def get_sprite(self):
        self.sprite = os.path.join(f'assets/images/{self.color}_{self.name}.png')

    # move function for piece
    def move(self, board):
        pass
    
#  ----------------------------------------------------- #
#  Child Classes describing each unique piece


class Pawn(GamePiece):
    def __init__(self, color):
        self.dir = 'UP' if color == "White" else "Down" 
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__('pawn', color)

class knight(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('knight', color, sprite)

class Rook(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('rook', color, sprite)

class Bishop(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('bishop', color, sprite)

class King(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('king', color, sprite)

class Queen(GamePiece):
    def __init__(self, type, color, sprite=None):
        super().__init__('queen', color, sprite)
