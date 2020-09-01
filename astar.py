from queue import PriorityQueue
import pygame

# Pygame initialization
pygame.init()

# Screen
WIDTH = 500
WIN = pygame.display.set_mode((WIDTH, WIDTH))

# Colors
WHITE = (255, 255, 255)

# Draw method
def draw(win):
    win.fill(WHITE)
    pygame.display.update()

# Main method
def main(win):
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
