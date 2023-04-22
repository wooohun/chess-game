from . import gamePiece

class Rook(gamePiece.GamePiece):
    def __init__(self, pos, color, sprite=None):
        super().__init__(pos, color, sprite)
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)