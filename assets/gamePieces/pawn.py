from . import gamePiece
from . import bishop
from . import knight
from . import queen
from . import rook

# NEED TO IMPLEMENT RULES FOR EN PASSANT


class Pawn(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color, board)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)

    def get_possible_moves(self, board):
        """ Get all possible moves for piece, return list of moves"""
        res = []
        # forward movement
        moves = [(0, 1)]
        # pawn can only move two squares if it has never moved and is not currently blocked
        if self.has_moved == False:
            moves.append([0, 2])
        if self.color == 'white':
            moves = [[move[0], -move[1]] for move in moves]

        for move in moves:
            target = (self.x, self.y + move[1])
            new_y = target[1]
            if new_y < 8 and new_y >= 0:
                res.append(board.get_rect_from_coords(target))
        return res
    
    def get_moves(self, board):
        """ Get set of valid moves from list of possible moves, return list """
        res = []
        print(self.x, self.y)
        # will at most be list of len == 2, less lines of code than is_not_blocked function
        for move in self.get_possible_moves(board):
            # if front square has unit, cant move 1 or 2 squares
            if move.cur_piece != None:
                break
            else:
                res.append(move)
        if self.color == 'white':
            # handle diagonal moves if pieces are there to take
            # right take
            if self.x + 1 < 8 and self.y - 1 >= 0:
                right = (self.x + 1, self.y - 1)
                target = board.get_rect_from_coords(right)
                if target.cur_piece != None and target.cur_piece.color == 'black':
                    res.append(target)
            # left take
            if self.x - 1 >= 0 and self.y - 1 >= 0:
                left = (self.x - 1, self.y - 1)
                target = board.get_rect_from_coords(left)
                if target.cur_piece != None and target.cur_piece.color == 'black':
                    res.append(target)
        elif self.color == 'black':
            # right take
            if self.x + 1 < 8 and self.y + 1 < 8:
                right = (self.x + 1, self.y + 1)
                print(f'Black Right: {right}, Coords: {self.pos}, Piece: {self.piece}')
                target = board.get_rect_from_coords(right)
                if target.cur_piece != None and target.cur_piece.color == 'white':
                    res.append(target)
            # left take
            if self.x - 1 >= 0 and self.y + 1 < 8:
                left = (self.x - 1, self.y + 1)
                target = board.get_rect_from_coords(left)
                if target.cur_piece != None and target.cur_piece.color == 'white':
                    res.append(target)
        return res
    
    # pawn movement
    def move(self, board, t_sq):
        """Normal Move Logic with Pawn Promotion, return bool"""
        moves = self.get_valid_moves(board)
        if t_sq in moves:
            cur_sq = board.get_rect_from_coords(self.pos)
            self.pos = t_sq.coords
            cur_sq.cur_piece = None
            t_sq.cur_piece = self
            self.has_moved = True
            # handle promotion
            if self.y == 7 or self.y == 0:
                # make promotion selection
                choice = None
                if choice == 'B':
                    t_sq.cur_piece = bishop.Bishop((self.x, self.y), choice, self.color, board)
                elif choice == 'Kn':
                    t_sq.cur_piece = knight.Knight((self.x, self.y), choice, self.color, board)
                elif choice == 'R':
                    t_sq.cur_piece = rook.Rook((self.x, self.y), choice, self.color, board)
                elif choice == 'Q':
                    t_sq.cur_piece = queen.Queen((self.x, self.y), choice, self.color, board)
            return True
        else:
            return False
            


    