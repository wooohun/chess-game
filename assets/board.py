from collections import defaultdict
from assets.square import BoardSquare
import assets.utils.config as config
from assets.gamePieces.pawn import Pawn
from assets.gamePieces.knight import Knight
from assets.gamePieces.bishop import Bishop
from assets.gamePieces.rook import Rook
from assets.gamePieces.queen import Queen
from assets.gamePieces.king import King
from assets.movement import Mover

class GameBoard:
    def __init__(self):
        self.board = self.create_board()
        # better to have config matrix to help set up board?
        # or just write logic to configure from the created board @ self.board
        # 2 (n^2) vs n^2 traversal time, but n is fixed at 8 so time is negligible
        # only consideration is space usage from self.config, also negligible since its set at 8x8 matrix
        self.init = [
            ['bR', 'bKn', 'bB', 'bQ', 'bK', 'bB', 'bKn', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['','','','','','','',''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wKn', 'wB', 'wQ', 'wK', 'wB', 'wKn', 'wR']
        ]
        # dict of pieces
        # key: color, value: list of pieces
        self.pieces = defaultdict(list)
        self.init_board()
        self.mover = Mover()
        self.turn = 'white'
    
    # create board, want list of rect instead of matrix for pygame.display.update
    def create_board(self):
        board = []
        # constructor for RECT: Rect(left, top, wid, height),
        # i = left most point of current rect, j = top most point of current rect
        # construct board w/ black up, white down
        # make board row by row, meaning for each j, make i in range 8
        for j in range(config.ROWS):
            for i in range(config.COLS):
                board.append(BoardSquare(j, i))
        return board
    
    # setup pieces
    def init_board(self):
        # traverse through config and board at same time, initialize using pieces classes
        rows = config.ROWS
        cols = config.COLS
        for x in range(rows):
            for y in range(cols):
                tile = self.init[y][x]
                if tile != '':
                    color = 'white' if tile[0] == 'w' else 'black'
                    piece = tile[1:]
                    cur_sq = self.board[(x*8) + y]
                    if piece == 'P':
                        cur_sq.cur_piece = Pawn((x, y), piece, color, self)
                    elif piece == 'Kn':
                        cur_sq.cur_piece = Knight((x, y), piece, color, self)
                    elif piece == 'B':
                        cur_sq.cur_piece = Bishop((x, y), piece, color, self)
                    elif piece == 'R':
                        cur_sq.cur_piece = Rook((x, y), piece, color, self)
                    elif piece == 'Q':
                        cur_sq.cur_piece = Queen((x, y), piece, color, self)
                    elif piece == 'K':
                        cur_sq.cur_piece = King((x, y), piece, color, self)
                    self.pieces[cur_sq.cur_piece] = cur_sq.cur_piece.get_valid_moves(self)
                    # self.pieces[color].append(cur_sq.cur_piece) if color == 'white' else self.pieces[color].append(cur_sq.cur_piece)
        return
    
    def get_rect_from_coords(self, coords):
        x, y = coords[0], coords[1]
        return self.board[(x*8) + y] if ((x*8) + y) < 64 else None
    
    def draw(self, screen):
        for square in self.board:
            square.update(screen)

    # returns True if under attack, false if not
    def is_in_check(self, cur_sq, t_sq):
        """ Simulates piece movement to check board state, returns T/F"""
        res = False
        cur_piece = cur_sq.cur_piece
        t_piece = t_sq.cur_piece

        # simulate movement
        t_sq.cur_piece = cur_piece
        cur_sq.cur_piece = t_piece

        # check if currently in check
        for moves in self.pieces.values():
            for sq in moves:
                if sq.cur_piece == 'K':
                    res = True

        # reset board state
        t_sq.cur_piece = t_piece
        cur_sq.cur_piece = cur_piece
        return res

    
    def get_piece_from_coords(self, coords):
        x, y = coords[0], coords[1]
        return self.board[(8*x) + y].cur_piece
    
    def update_moves(self):
        for piece in self.pieces.keys():
            self.pieces[piece] = piece.get_valid_moves(self)

    def clear_highlights(self):
        for sq in self.board:
            sq.highlight = False
            
    def show_highlights(self, piece):
        for sq in self.pieces[piece]:
            sq.highlight = True


    #change the piece at the coordinates to a queen
    def promote_pawn(self, x, y, color):
        self.board[8*x + y].cur_piece = Queen((x, y), 'Q', color, self)
