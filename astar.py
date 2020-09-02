""" Importing the Priority Queue """
from queue import PriorityQueue
import pygame

# Pygame initialization
pygame.init()

# Screen
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# Colors
WHITE = (255, 255, 255)

class Node():
    """ Class Node represents single cell in the grid """
    def __init__(self, row, col, width, total_rows):
        """ Init function """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.neighbours = []
        self.total_rows = total_rows

    def is_color(self, color):
        """ Checks the type of node by color """
        return self.color == color

    def set_color(self, color):
        """ Sets the type of node by color """
        self.color = color

    def draw(self, win):
        """ Drawing the individual nodes """
        pygame.draw.rect(win, self.color, (self.x, self.y , self.width, self.width))

    def update_neighbours(self):
        pass

    def __lt__(self, other):
        """ Dunder method __lt__ if a tie happens """
        return False

def draw(win):
    """ Draws elements on the screen """
    win.fill(WHITE)
    pygame.display.update()

def main(win):
    """ Main method which handles the function calls, also handles the input """
    run = True

    # Main loop
    while run:
        # Drawing the screen
        draw(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Game quit
    pygame.quit()

if __name__ == "__main__":
    main(WIN)
