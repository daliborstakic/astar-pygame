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
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (255, 0, 255)
RED = (255, 0, 0)

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

    def get_pos(self):
        """ Returns the position in the grid """
        return self.row, self.col

    def is_color(self, color):
        """ Checks the type of node by color """
        return self.color == color

    def set_color(self, color):
        """ Sets the type of node by color """
        self.color = color

    def draw(self, win):
        """ Drawing the individual nodes """
        pygame.draw.rect(win, self.color, (self.x, self.y , self.width, self.width))

    def update_neighbours(self, grid):
        self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_color(BLACK): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_color(BLACK): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_color(BLACK): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_color(BLACK): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        """ Dunder method __lt__ if a tie happens """
        return False


def h(p1, p2):
    """ Aproximated distance """
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def get_clicked_pos(pos, rows, width):
    """ Get the row and column based on click position """
    gap = width // rows
    x, y = pos

    row = x // gap
    col = y // gap

    return row, col

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.set_color(PURPLE)
        draw()

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

def algorithm(draw, grid, start, end):
    """ The A* Pathfinding algorithm """
    count = 0
    open_set = PriorityQueue() # Setting the inital PriorityQueue
    open_set.put((0, count, start))
    came_from = {} # This actually represents the shortest path

    g_score = {spot: float("inf") for row in grid for spot in row} # Infinite g_score
    g_score[start] = 0
    f_score = {spot: float("inf") for row in grid for spot in row} # Infinite f_score
    f_score[start] = h(start.get_pos(), end_get_pos())

    open_set_hash = {start} # Hash for getting values fron open_set

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2] # Get the current node
        open_set_hash.remove(current)

        if current == end: # If it reached the end
            reconstruct_path(came_from, end, draw)
            end.set_color(YELLOW)
            start.set_color(BLUE)
            return True

        for neighbour in current.neighbours: # Looping through every neighbour
            temp_g_score = g_score[current] + 1

            # Calculating the neighbours f_score
            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + h(neighbour.get_pos(), end.get_pos())

                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put(neighbour)
                    open_set_hash.add(neighbour)
                    neighbour.set_color(GREEN)

        draw()

        if current != start: # Closes nodes
            current.set_color(RED)

        return False


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

    ROWS = 50 # Rows val

    # Start and end nodes
    start = None
    end = None

    grid = make_grid(ROWS, WIDTH)

    # Main loop
    while run:
        # Drawing the screen
        draw(win, grid, WIDTH, ROWS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]: # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]

                if not start and spot != end:
                    start = spot
                    start.set_color(BLUE)
                elif not end and spot != start:
                    end = spot
                    end.set_color(YELLOW)
                elif spot != end and spot != start:
                    spot.set_color(BLACK)

            if pygame.mouse.get_pressed()[2]: # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, WIDTH)
                spot = grid[row][col]
                spot.set_color(WHITE)

                if spot == start:
                    start = None
                elif spot == end:      
                    end = None              

    # Game quit
    pygame.quit()

if __name__ == "__main__":
    main(WIN)
