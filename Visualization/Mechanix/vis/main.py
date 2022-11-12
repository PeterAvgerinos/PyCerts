import pygame
from mecanix.constants import SQUARE_SIZE, WIDTH, HEIGHT, MOUNT_SIZE
from mecanix.board import Board

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def get_pos_from_mouse(pos):
    x, y = pos
    row = WIDTH//2 - SQUARE_SIZE//2 - (y - x)*SQUARE_SIZE + 2*MOUNT_SIZE + (SQUARE_SIZE//2)*y
    col = SQUARE_SIZE*y + 2*MOUNT_SIZE + 50,
    return col, row

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    board.create_board(WIN)
    board.move(board.get_gear(3,2), 'green', WIN)
    board.move(board.get_gear(4,2), 'green', WIN)
    board.move(board.get_gear(5,2), 'green', WIN)
    board.move(board.get_gear(6,2), 'green', WIN)

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
                    print(gear.x, gear.y)
                    board.move(gear, 'green', WIN)
                except TypeError:
                    pass

        board.update(WIN)
        pygame.display.update()


    pygame.quit()

main()


