import pygame
from mecanix.constants import WIDTH, HEIGHT
from mecanix.board import Board

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    # board.draw_squares(WIN)
    # board.draw_gear_mounts(WIN)
    board.create_board(WIN)
    board.move(board.get_gear(2,2), 'green', WIN)
    board.move(board.get_gear(2,2), 'blue', WIN)
    board.move(board.get_gear(2,2), 'transparent', WIN)

    board.move(board.get_gear(9,0), 'transparent', WIN)


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.update(WIN)
        pygame.display.update()


    pygame.quit()

main()


