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
GRAY = (200, 200, 200)

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


def get_clicked_pos(pos, rows, width):
    """ Get the row and column based on click position """
    gap = width // rows
    x, y = pos

    row = y // gap
    col = x // gap

    return row, col

def make_grid(rows, width):
    """ Initializng the grid """
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j, gap, rows) # Adding nodes to every cell
            grid[i].append(node)
    
    return grid

def draw_grid(win, width, rows):
    """ Draws the grid """
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GRAY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GRAY, (j * gap, 0), (j * gap, width))

def draw(win, grid, width, rows):
    """ Draws elements on the screen """
    win.fill(WHITE)

    """ Drawing the nodes """
    for row in grid:
        for node in row:
            node.draw(win)

    draw_grid(win, width, rows) # Drawing the grid

    pygame.display.update()

def main(win):
    """ Main method which handles the function calls, also handles the input """
    run = True

    ROWS = 20 # Rows val

    grid = make_grid(ROWS, WIDTH)

    # Main loop
    while run:
        # Drawing the screen
        draw(win, grid, WIDTH, ROWS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    # Game quit
    pygame.quit()

if __name__ == "__main__":
    main(WIN)
