import pygame
from mecanix.constants import SQUARE_SIZE, WIDTH, HEIGHT
from mecanix.board import Board

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def get_pos_from_mouse(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
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
                pos = pygame.mouse.get_pos()
                row, col = get_pos_from_mouse(pos)
                gear = board.get_gear(row, col)
                board.move(gear, 'transparent', WIN)

        board.update(WIN)
        pygame.display.update()


    pygame.quit()

main()


