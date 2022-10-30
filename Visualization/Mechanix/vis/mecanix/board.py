import pygame
from .constants import BLACK, RED, WIDTH, SQUARE_SIZE, MOUNT_SIZE
from .gear import Gear

class Board(pygame.sprite.Sprite):
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.green_left = self.blue_left = 12

    def draw_squares(self, win):
        for row in range(6):
            for col in range(row*2 + 1):
                pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE, SQUARE_SIZE*row + 50, SQUARE_SIZE, SQUARE_SIZE))

    def draw_gear_mounts(self, win):
        for row in range(6):
            for col in range(row*2 + 1):
                pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE, SQUARE_SIZE*row + 2*MOUNT_SIZE + 50), MOUNT_SIZE)

    def create_board(self, win):
        for row in range(6):
            self.board.append([])
            for col in range(row*2 + 1):
                new_gear = Gear(row, col, 'transparent', WIDTH//2 - SQUARE_SIZE//2 - (row - col)*SQUARE_SIZE + 2*MOUNT_SIZE,  SQUARE_SIZE*row + 2*MOUNT_SIZE + 50)
                self.board[row].append(new_gear)
                new_gear.draw(win)

    # def draw_squares(self, win):
    #     win.fill(BLACK)
    #     pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2, 50, SQUARE_SIZE, SQUARE_SIZE))
    #     for square in range(3):
    #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 1)*SQUARE_SIZE, SQUARE_SIZE + 50, SQUARE_SIZE, SQUARE_SIZE))
    #     for square in range(5):
    #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 2)*SQUARE_SIZE, SQUARE_SIZE*2 + 50, SQUARE_SIZE, SQUARE_SIZE))
    #     for square in range(7):
    #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 3)*SQUARE_SIZE, SQUARE_SIZE*3 + 50, SQUARE_SIZE, SQUARE_SIZE))
    #     for square in range(9):
    #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 4)*SQUARE_SIZE, SQUARE_SIZE*4 + 50, SQUARE_SIZE, SQUARE_SIZE))
    #     for square in range(11):
    #         pygame.draw.rect(win, RED, (WIDTH//2 - SQUARE_SIZE//2 - (square - 5)*SQUARE_SIZE, SQUARE_SIZE*5 + 50, SQUARE_SIZE, SQUARE_SIZE))


    # def draw_gear_mounts(self, win):
    #     pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 + 2*MOUNT_SIZE, 50 + 2*MOUNT_SIZE), MOUNT_SIZE)
    #     for square in range(3):
    #         pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 1)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
    #     for square in range(5):
    #         pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 2)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*2+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
    #     for square in range(7):
    #         pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 3)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*3+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
    #     for square in range(9):
    #         pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 4)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*4+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)
    #     for square in range(11):
    #         pygame.draw.circle(win, BLACK, (WIDTH//2 - SQUARE_SIZE//2 - (square - 5)*SQUARE_SIZE+ 2*MOUNT_SIZE, SQUARE_SIZE*5+ 2*MOUNT_SIZE + 50), MOUNT_SIZE)



