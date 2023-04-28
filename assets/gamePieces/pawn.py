from . import gamePiece

# NEED TO IMPLEMENT RULES FOR EN PASSANT


class Pawn(gamePiece.GamePiece):
    def __init__(self, pos, piece, color, board):
        #pawns can only move in one direction all other piece can move in any direction they want 
        super().__init__(pos, piece, color, board)
        # self.dir = 'UP' if color == "white" else "Down" 
        self.sprite_path = self.get_sprite()
        self.sprite = self.load_sprite(self.sprite_path)
        self.has_moved = False

    # get all potential forward moves for pawn
    def get_possible_moves(self, board):
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
            new_x = target[0]
            new_y = target[1]
            if new_y < 8 and new_y >= 0:
                res.append(board.get_rect_from_coords(target))
        return res
    
        # # check if pawn is blocked
    # def is_not_blocked(self, board):
    #     # front tile 
    #     front = [0, 1]
    #     # if white then move up
    #     if self.color == 'white':
    #         front[1] = -1
    #     front_coords = (self.x, self.y + front[1])
    #     front_tile = board.get_rect_from_coords(front_coords)
    #     # return True if front is not occupied, False if occupied
    #     return front_tile.cur_piece == None
    
    def get_moves(self, board):
        res = []
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
            if self.x - 1 >= 0 and self.y + 1 < 8:
                right = (self.x + 1, self.y - 1)
                target = board.get_rect_from_coords(right)
                if target.cur_piece != None and target.cur_piece.color == 'white':
                    res.append(target)
            # left take
            if self.x + 1 < 8 and self.y + 1 < 8:
                left = (self.x - 1, self.y - 1)
                target = board.get_rect_from_coords(left)
                if target.cur_piece != None and target.cur_piece.color == 'white':
                    res.append(target)
        return res

    