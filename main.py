import pygame

#defining the constant
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE = WIDTH // COLS

class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    def check_exit(self):

        while True:
            self.game.display_board(self.screen)
        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


class Game:

    def __init__(self):
        pass

    def display_board(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    color = (0,0,0)
                else:
                    color = (119, 154, 88)

                dims = (col * SQUARE, row * SQUARE, SQUARE, SQUARE)

                pygame.draw.rect(surface, color, dims)

main = Main()
main.check_exit()