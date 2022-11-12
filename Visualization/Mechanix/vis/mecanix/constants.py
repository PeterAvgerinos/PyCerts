import pygame

#Game
WIDTH, HEIGHT = 1400, 1000
ROWS, COLS = 10,10
SQUARE_SIZE = 80
MOUNT_SIZE = SQUARE_SIZE//4

#RGB Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

#Images
BLUEGEAR = pygame.image.load("assets/blue-gear-md.png")
GREENGEAR = pygame.image.load("assets/imagination-movers-gears-md.png")
TARGETGEAR = pygame.image.load("assets/green-gear.svg.med.png")
TRANSPARENT = pygame.image.load("assets/block.png")

#Functions
def get_pos_from_mouse(pos):
    x, y = pos
    if (660 <= x <= 739) & (53 <= y <= 131):
        row, col = 0, 0
    elif (134 <= y <= 211):
        if (621 <= x <= 699):
            row, col = 1,0
        elif (702 <= x <= 777):
            row, col = 1,1
    elif (215 <= y <= 290):
        if (581 <= x <= 658):
            row, col = 2,0
        elif (663 <= x <= 737):
            row, col = 2,1
        elif (745 <= x <= 817):
            row, col = 2,2
    elif (295 <= y <= 369):
        if (541 <= x <= 618):
            row, col = 3,0
        elif (622 <= x <= 696):
            row, col = 3,1
        elif (703 <= x <=774):
            row, col = 3,2
        elif (785 <= x <= 857):
            row, col = 3,3
        pass

    row = x*SQUARE_SIZE
    col = y*SQUARE_SIZE
    return col, row
