import pygame
from .constants import BLACK, BLUEGEAR, RED, TARGETGEAR, TRANSPARENT, WIDTH, SQUARE_SIZE, MOUNT_SIZE, ROWS, BLUEGEAR, TARGETGEAR
from .gear import Gear

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.board = []
        self.gear_group = pygame.sprite.Group()
        self.selected_piece = None
        self.green_left = self.blue_left = 12

    def __repr__(self):
        for row in range(ROWS):
            for col in range(row + 1):
                print(self.board[row][col])

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(row + 1):
                if row != 0:
                    pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + (SQUARE_SIZE//2)*row, SQUARE_SIZE*row + 50, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE, SQUARE_SIZE*row + 50, SQUARE_SIZE, SQUARE_SIZE))


    def draw_gear_mounts(self, win):
        for row in range(ROWS):
            for col in range(row + 1):
                if row != 0:
                    pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE + (SQUARE_SIZE//2)*row, SQUARE_SIZE*row + 2*MOUNT_SIZE + 50), MOUNT_SIZE)
                else:
                    pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE, SQUARE_SIZE*row + 2*MOUNT_SIZE + 50), MOUNT_SIZE)

    def create_board(self, win):
        self.draw_squares(win)
        self.draw_gear_mounts(win)
        for row in range(ROWS):
            self.board.append([])
            for col in range(row + 1):
                if row != 0:
                    new_gear = Gear(row, col, 'transparent', WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE + (SQUARE_SIZE//2)*row,  SQUARE_SIZE*row + 2*MOUNT_SIZE + 50, TRANSPARENT)
                    if row == ROWS - 1:
                        if col == 0 or col == ROWS-1:
                            new_gear.make_fixed()
                else:
                    new_gear = Gear(row, col, 'target', WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE,  SQUARE_SIZE*row + 2*MOUNT_SIZE + 50, TARGETGEAR)
                    new_gear.make_fixed()
                self.board[row].append(new_gear)
                self.gear_group.add(new_gear)
                # new_gear.draw(win)
        self.gear_group.draw(win)

    def update_board(self):
        self.gear_group.update()

    def move(self, gear, color, win):
        selected_gear = self.board[gear.row][gear.col]
        if not selected_gear.fixed:
            selected_gear.set_color(color)
            win.blit(selected_gear(selected_gear.image, (selected_gear.x, selected_gear.y)))

    def get_gear(self, row, col):
        return self.board[row][col]

