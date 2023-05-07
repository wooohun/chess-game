from . import gamePiece

class Knight(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color, board)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)
    
    def get_possible_moves(self, board):
        res = []

        # knights can only move in an L shape
        # right/down/left/up 2 squares, then right/left or up/down 1 square

        # valid moves: 
        # (x increment, y increment)
        valid = [
            # right 2 spaces
            (2, -1),
            (2, 1),
            # down 2 spaces
            (1, 2),
            (-1, 2),
            # left 2 spaces
            (-2, -1),
            (-2, 1),
            # up 2 spaces
            (1, -2),
            (-1, -2)
        ]

        for coord in valid:
            target = [self.x + coord[0], self.y + coord[1]]

            # check that target is in board
            if (target[0] >= 0 and target[0] < 8 and target[1] >= 0 and target[1] < 8):
                res.append(board.get_rect_from_coords(target))

        return res