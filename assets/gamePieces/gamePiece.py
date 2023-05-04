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
        self.under_attack = False
        self.pinned = True
        self.has_moved = False
    
    # get sprite path
    def get_sprite(self):
        return os.path.join(os.getcwd(), f'assets/images/{self.color}_{self.piece}.png')

    # load sprite image
    def load_sprite(self, path):
        sprite = pygame.image.load(path)
        return pygame.Surface.convert(sprite)
    

    # movement:
    # square objects dont move
    # only the pieces within the objects move
    def move(self, board, t_sq):
        # reset highlights
        for sq in board.board:
            sq.highlight = False

        moves = self.get_moves(board)
        if t_sq in moves:
            cur_sq = board.get_rect_from_coords(self.pos)
            self.pos = t_sq.coords
            self.x, self.y = self.pos[0], self.pos[1]
            cur_sq.cur_piece = None
            t_sq.cur_piece = self
            self.has_moved = True

            # handle castling
            # if self.piece == 'K':
            return True
        else:
            return False
    

    # FUNCTION WILL BE OVERRIDDEN FOR ONLY THE PAWN SUB-CLASS
    # DUE TO ABILITY TO ONLY MOVE ONE SQUARE

    # get valid moves from set of possible moves
    # i.e get moves from vectors until collision happens
    # check if attackable, if able, then add to move set, end vector
    # else end vectore before possible move
    def get_moves(self, board):
        res = []
        for dir in self.get_possible_moves(board):
            for idx, move in enumerate(dir):
                target = move.cur_piece
                if target != None:
                    if target.color != self.color:
                        move.highlight = True
                        move.cur_piece.under_attack = True
                        res.append(move)
                        break
                    else:
                        break
                else:
                    move.highlight = True
                    res.append(move)
        return res
    
    # determine if piece in attack vector has king behind it
    def is_pinned(self, vec, idx):
        last = len(vec) - 1
        # if current sq is last in attack vector, nothing is "behind" it
        if idx == last:
            return
        cur = vec[idx]
        next = vec[idx+1]
        # if square "behind" cur contains king, cur piece is pinned
        if next.cur_piece.piece == 'K':
            cur.cur_piece.pinned = True
        return


