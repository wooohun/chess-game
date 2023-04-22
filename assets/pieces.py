
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
