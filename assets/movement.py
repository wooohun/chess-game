import pygame
from .gamePieces.gamePiece import GamePiece

from assets.utils.config import *
import assets.board as GameBoard

class Mover:

    def __init__(self) -> None:
        self.pos = (0, 0)
        self.mouseX = 0
        self.mouseY = 0
        self.rel_x = self.mouseX // SQUARE_W
        self.rel_y = self.mouseY // SQUARE_H
        self.initial_row = 0
        self.initial_col = 0
        self.piece = None
        self.moving = False


    @property 
    def pos(self):
        return self._pos
    
    @pos.setter
    def pos(self, coords):
        self._pos = coords
        self.mouseX = self.pos[0]
        self.mouseY = self.pos[1]
        self.rel_x = self.pos[0] // SQUARE_W
        self.rel_y = self.pos[1] // SQUARE_H


    def update_blit(self, surface):
        pass


    def update(self, pos):
        self.mouseX, self.mouseY = pos

    def save_initial(self, pos):
        self.initial_row = pos[1] // SQUARE_W
        self.initial_col = pos[0] // SQUARE_H

    def move_piece(self, piece):
        self.piece = piece
        self.moving = True

    def unmove_piece(self):
        self.piece = None
        self.moving = False
    
    def is_targeting_board(self):
        if self.mouseX <= 800 and self.mouseY <= 800:
            return True
        return False


    # def move_piece(self, old_c, old_r, new_c, new_r, piece):
    #     self.piece = piece
    #     self.moving = True
    #     self.initial_col = old_c
    #     self.initial_row = old_r
    #     self.mouseX = new_c
    #     self.mouseY = new_r

    #     self.game.board.remove_piece(old_r, old_c)

    #function when mouse button is pressed to select the piece
    def mouse_button_down(self, pos):
        self.update(pos)
        self.save_initial(pos)

        clicked_row = self.mouseY // SQUARE_W
        clicked_col = self.mouseX // SQUARE_H

        self.piece = self.game.board.get_piece(clicked_row, clicked_col)

        return self.piece