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
        self._pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.has_moved = False


    #######################################################
    # set instance property decorators for position updates

    # position getter
    @property
    def pos(self):
        return self._pos
    # position setter
    @pos.setter
    def pos(self, coords):
        self._pos = coords
        self.x = self.pos[0]
        self.y = self.pos[1]
    
    
    # get sprite path
    def get_sprite(self):
        return os.path.join(os.getcwd(), f'assets/images/{self.color}_{self.piece}.png')

    # load sprite image
    def load_sprite(self, path):
        sprite = pygame.image.load(path)
        return pygame.Surface.convert(sprite)
    

    # FUNCTION WILL BE OVERRIDDEN FOR ONLY THE PAWN SUB-CLASS
    # DUE TO ABILITY TO ONLY MOVE ONE SQUARE

    # get valid moves from set of possible moves
    # i.e get moves from vectors until collision happens
    # check if attackable, if able, then add to move set, end vector
    # else end vector before possible move
    def get_moves(self, board):
        """ Targetable set of moves from all possible, returns List"""
        res = []
        for dir in self.get_possible_moves(board):
            for move in dir:
                target = move.cur_piece
                if target != None:
                    if target.color != self.color:
                        res.append(move)
                        break
                    else:
                        break
                else:
                    res.append(move)
        return res
    
    def get_valid_moves(self, board):
        """ get moves from board.pieces, return set of valid moves"""
        res = []
        cur_sq = board.get_rect_from_coords(self.pos)
        for t_sq in self.get_moves(board):
            if not board.is_in_check(cur_sq, t_sq):
                res.append(t_sq)
        return res

    # movement:
    # square objects dont move
    # only the pieces within the objects move
    def move(self, board, t_sq):
        """Move Piece, Return bool if successful"""
        moves = self.get_valid_moves(board)
        if t_sq in moves:
            cur_sq = board.get_rect_from_coords(self.pos)
            self.pos = t_sq.coords
            cur_sq.cur_piece = None
            t_sq.cur_piece = self
            self.has_moved = True

            # handle castling
            if self.piece == 'K':
                if cur_sq.x - self.x == 2:
                    # moving left
                    target = board.get_rect_from_coords((3, self.y))
                    rook = board.get_piece_from_coords((0, self.y))
                    rook.force_move(board, target)
                elif cur_sq.x - self.x == -2:
                    # moving right
                    target = board.get_rect_from_coords((5, self.y))
                    rook = board.get_piece_from_coords((7, self.y))
                    rook.force_move(board, target)
            return True
        else:
            return False
        

