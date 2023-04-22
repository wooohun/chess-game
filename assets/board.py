from assets.square import BoardSquare
import assets.utils.config as config
from assets.gamePieces.pawn import Pawn

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
        self.init_board()
    
    # create board, want list of rect instead of matrix for pygame.display.update
    def create_board(self):
        board = []
        for i in range(config.ROWS):
            for j in range(config.COLS):
                board.append(BoardSquare(i, j))
        return board
    
    # setup pieces
    def init_board(self):
        # traverse through config and board at same time, initialize using pieces classes
        rows = config.ROWS
        cols = config.COLS
        for i in range(rows):
            for j in range(cols):
                tile = self.init[i][j]
                if tile != '':
                    color = 'white' if tile[0] == 'w' else 'black'
                    piece = tile[1:]
                    cur_sq = self.board[(i*8) + j]
                    if piece == 'P':
                        cur_sq.cur_piece = Pawn((i, j), piece, color)
        return
    
    def draw(self, screen):
        for square in self.board:
            square.update(screen)
    