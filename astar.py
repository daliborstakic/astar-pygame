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

def draw(win):
    """ Draws elements on the screen """
    win.fill(WHITE)
    pygame.display.update()

def main(win):
    """ Main method which handles all the function calls """
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
