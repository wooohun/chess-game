import pygame
# import assets.config as config
from assets.board import GameBoard
from assets.config import *

# WIDTH, HEIGHT = 800, 800
# ROWS, COLS = 8, 8
# SQUARE = 100

class Main:

    def __init__(self):
        pygame.init() #initializeing the pygame
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT)) #initializing the display
        pygame.display.set_caption('Chess') 
        self.game = Game() #initializing the game class
    
    def check_exit(self):
        while True:
            self.game.display_board(self.screen) #displaying the chessboard from the game class
        
            for event in pygame.event.get(): #constantly keep checking if the user exited the game
                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update() #constantly update the state of the display until the game is exited


class Game: 
#This class will be used to create the chess board
    def __init__(self):
        self.board = GameBoard()
        pass


    def display_board(self, surface):
        self.board.draw(surface)

main = Main()
main.check_exit()