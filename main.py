import pygame
from assets.square import BoardSquare

#defining the constant
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE = WIDTH // COLS

class Main:

    def __init__(self):
        pygame.init() #initializeing the pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT)) #initializing the display
        pygame.display.set_caption('Chess') 
        self.game = Game() #initialinzing the game class
    
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
        # create board object.
        # self.board = [[ BoardSquare for j in range(8)] for i in range(8)]
        pass

    def display_board(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (0,0,0)
                else:
                    color = (255,255,255)

                dims = (col * SQUARE, row * SQUARE, SQUARE, SQUARE)

                pygame.draw.rect(surface, color, dims)

main = Main()
main.check_exit()