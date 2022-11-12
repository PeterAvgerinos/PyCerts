import pygame
from mecanix.constants import SQUARE_SIZE, WIDTH, HEIGHT, MOUNT_SIZE
from mecanix.board import Board
from mecanix.game import Game

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def get_pos_from_mouse(pos):
    x, y = pos
    if (660 <= x <= 739) & (53 <= y <= 131):
        row, col = 0, 0
        return col, row
    elif (134 <= y <= 211):
        if (621 <= x <= 699):
            row, col = 1,0
            return col, row
        elif (702 <= x <= 777):
            row, col = 1,1
            return col, row
    elif (215 <= y <= 290):
        if (581 <= x <= 658):
            row, col = 2,0
            return col, row
        elif (663 <= x <= 737):
            row, col = 2,1
            return col, row
        elif (745 <= x <= 817):
            row, col = 2,2
            return col, row
    elif (295 <= y <= 369):
        if (541 <= x <= 618):
            row, col = 3,0
            return col, row
        elif (622 <= x <= 696):
            row, col = 3,1
            return col, row
        elif (703 <= x <=774):
            row, col = 3,2
            return col, row
        elif (785 <= x <= 857):
            row, col = 3,3
            return col, row
    else:
        row = x*SQUARE_SIZE
        col = y*SQUARE_SIZE
        return col, row

def main():
    run = True
    clock = pygame.time.Clock()
    # game = Game(WIN)
    board = Board()
    board.create_board(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    pos = pygame.mouse.get_pos()
                    print(pos)
                    row, col = get_pos_from_mouse(pos)
                    gear = board.get_gear(row, col)
                    # print(gear.x, gear.y)
                    board.move(gear, 'green', WIN)
                except TypeError:
                    pass
                except IndexError:
                    pass

        board.update_board(WIN)
        pygame.display.update()


    pygame.quit()

main()


