import os
import pygame

# Game Piece parent class
class GamePiece:
    def __init__(self, pos, piece, color, board):
        # type is the type of the piece color is B or W and sprite will be the image
        self.piece = piece
        self.color = color
        self.sprite_path = None
        self.sprite = None
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
    
    def move(self, board):
        highlighted = self.highlight_moves(board)
        for square in highlighted:
            square.highlight = False
        return
    
    # def highlight_moves(self, board):
    #     res = []
    #     for square in self.get_moves(board):
    #         occupant = square.occupying_piece
    #         if occupant != None:
    #             if self.color == occupant.color:
    #                 continue
    #             else:
    #                 square.occupying_piece.highlight = True
    #                 res.append(square)
    #     return res
    

    # FUNCTION WILL BE OVERRIDDEN FOR ONLY THE PAWN SUB-CLASS
    # DUE TO ABILITY TO ONLY MOVE ONE SQUARE

    # get valid moves from set of possible moves
    # i.e get moves from vectors until collision happens
    # check if attackable, if able, then add to move set, end vector
    # else end vectore before possible move
    def get_moves(self, board):
        res = []
        for dir in self.get_possible_moves(board):
            for move in dir:
                target = move.cur_piece
                if target != None:
                    if target.color != self.color:
                        move.cur_piece.highlight = True
                        res.append(move)
                        break
                    else:
                        break
                else:
                    move.cur_piece.highlight = True
                    res.append(move)
        return res
