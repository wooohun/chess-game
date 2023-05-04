from . import gamePiece

class Rook(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        super().__init__(pos, piece, color, board)
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)

    # get all potential forward moves for pawn
    def get_possible_moves(self, board):
        res = []
        cur_x, cur_y = self.x, self.y
        
        # left
        left = []
        for l in range(cur_x - 1, -1, -1):
            target = (l, cur_y)
            left.append(board.get_rect_from_coords(target))

        # right
        right = []
        for r in range(cur_x + 1, 8):
            target = (r, cur_y)
            right.append(board.get_rect_from_coords(target))

        # up
        top = []
        for up in range(cur_y - 1, -1, -1):
            target = (cur_x, up)
            top.append(board.get_rect_from_coords(target))

        # down
        bot = []
        for down in range(cur_y + 1, 8):
            target = (cur_x, down)
            bot.append(board.get_rect_from_coords(target))

        res.append(left)
        res.append(right)
        res.append(top)
        res.append(bot)
        return res
    
                

        