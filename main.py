import pygame
# import assets.config as config
from assets.board import GameBoard
from assets.utils.config import *

class Main:

    def __init__(self):
        pygame.init() #initializeing the pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #initializing the display
        pygame.display.set_caption('Chess') 
        self.game = Game() #initializing the game class
        self.selected_piece = None
    
    def check_exit(self):
        #mover is in game board which is in game class which is in main class

        mover = self.game.board.mover

        while True:
            self.game.display_board(self.screen) #displaying the chessboard from the game class
        
            for event in pygame.event.get(): #constantly keep checking if the user made any change

                #if the user want to quit
                if event.type == pygame.QUIT:
                    pygame.quit()
                
                # if user clicks
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.game.board.update_moves()
                        #TODO create a new function to take the position of the mouse and check if it has piece or not then save initial pos if it has piece and move the piece

                        # piece = mover.mouse_button_down(event.pos)

                        # mover.update(event.pos)
                        mover.pos = event.pos


                        #check if the square has a piece
                        target = self.game.board.get_piece_from_coords((mover.rel_x, mover.rel_y))
                        if (target != None) and (target.color == self.game.board.turn):
                            mover.save_initial(event.pos)
                            mover.move_piece(target)
                            self.game.board.show_highlights(target)
                        else:
                            print('no piece')
                            mover.piece = None

                    


                #TODO create a new function for all the mouse button up tasks
                #if the user releases the mouse
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        # MOVEMENT LOGIC
                        
                         # on mousebutton up
                        # if not holding a piece, continue
                        if mover.piece == None:
                            continue

                        # update position of mover
                        mover.pos = event.pos                  
                        # get target square
                        t_sq = self.game.board.get_rect_from_coords((mover.rel_x, mover.rel_y))


                        ### held piece ###
                        # if piece can move, move
                        if mover.piece.move(self.game.board, t_sq):
                            # update turn
                            self.game.board.turn = 'white' if self.game.board.turn == 'black' else 'black'
                        mover.piece = None
                        
                        if self.game.board.get_piece_name((mover.rel_x, mover.rel_y)) == 'P':
                            self.check_promotion(mover.rel_x, mover.rel_y)


                        # clear highlights
                        self.game.board.clear_highlights()

                #if the user moves the mouse
                elif event.type == pygame.MOUSEMOTION:
                    if mover.moving:
                        mover.update(event.pos)
                        mover.update_blit(self.screen)

            pygame.display.update() #constantly update the state of the display until the game is exited

    def check_promotion(self, row, col):
        if col == 0:
            self.game.board.promote_pawn(row, col, color='white')
            print('promoted')
        elif col == 7:
            self.game.board.promote_pawn(row, col, color='black')
            print('promoted')
class Game: 
#This class will be used to create the chess board
    def __init__(self):
        self.board = GameBoard()
        pass


    def display_board(self, surface):
        self.board.draw(surface)

main = Main()
main.check_exit()