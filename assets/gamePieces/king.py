from . import gamePiece

class King(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color, board)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)

    def get_possible_moves(self, board):
        """ Get all possible moves for piece, return list of moves"""

        res = []
        valid = [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1)
        ]

        for move in valid:
            target = [self.x + move[0], self.y + move[1]]
            if (target[0] >= 0 and target[0] < 8 and target[1] >= 0 and target[1] < 8):
                res.append([board.get_rect_from_coords(target)])
        # get castling moves
        for move in self.can_castle(board):
            res.append([move])
        return res
    

    # castling is always directionally the same
    # queenside rook is left of king (perspective of white piece player)
    # kingside rook is right of king
    def can_castle(self, board):
        res = []
        if not self.has_moved:
            # get rooks
            lrook = board.get_piece_from_coords((0, self.y))
            rrook = board.get_piece_from_coords((7, self.y))
            # kingside
            if rrook != None:
                if not rrook.has_moved and rrook.piece == 'R':
                    if [board.get_piece_from_coords((i, self.y)) for i in range(5, 7)] == [None, None]:
                        res.append(board.get_rect_from_coords((self.x + 2, self.y)))
            #queenside
            if lrook != None:
                if not lrook.has_moved and lrook.piece == 'R':
                    if [board.get_piece_from_coords((i, self.y)) for i in range(1, self.x)] == [None, None, None]:
                        res.append(board.get_rect_from_coords((self.x - 2, self.y)))
        return res

