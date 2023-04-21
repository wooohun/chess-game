import pygame

# Game Piece parent class
class GamePiece:
    def __init__(self, color):
        self.color = color
        self.sprite = None
        
    # move function for piece
    def move(self, board):
        pass
    
#  ----------------------------------------------------- #
#  Child Classes describing each unique piece

class Pawn(GamePiece):
    def __init__(self):
        # self.sprite = 
        super().__init__(self)