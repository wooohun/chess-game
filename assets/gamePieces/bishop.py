from . import gamePiece

class Bishop(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color, board)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)

    # get all possible moves for piece
    def get_possible_moves(self, board):
        res = []
        cur_x, cur_y = self.x, self.y

       # north-west
        nw = []
        for i in range(1, min(cur_x, cur_y) + 1):
            target = (cur_x-i, cur_y-i)
            nw.append(board.get_rect_from_coords(target))

        # north-east
        ne = []
        for i in range(1, min(8-cur_x, cur_y)):
            target = (cur_x+i, cur_y-i)
            ne.append(board.get_rect_from_coords(target))
                
        # south-west
        sw = []
        for i in range(1, min(cur_x, 7-cur_y) + 1):
            target = (cur_x-i, cur_y+i)
            sw.append(board.get_rect_from_coords(target))

        # south-east
        se = []
        for i in range(1, min(8-cur_x, 8-cur_y)):
            target = (cur_x+i, cur_y+i)
            se.append(board.get_rect_from_coords(target))
            
        res.append(nw)
        res.append(ne)
        res.append(sw)
        res.append(se)

        return res