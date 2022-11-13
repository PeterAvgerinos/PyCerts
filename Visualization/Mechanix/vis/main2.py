import pygame
import math
from mecanix.constants import SQUARE_SIZE, WIDTH, HEIGHT, MOUNT_SIZE, ROWS
from mecanix.board import Board
from mecanix.game import Game

pygame.init()

FPS = 60

def convert_pos(ROWS, board):
    ROW, COL = 0,0
    m_x, m_y = pygame.mouse.get_pos()
    for row in range(ROWS):
        for col in range(row + 1):
            center_x, center_y = board.get_gear(row, col).x, board.get_gear(row, col).y
            dis = math.sqrt((center_x - m_x)**2 + (center_y - m_y)**2)
            if dis < SQUARE_SIZE//2:
                ROW, COL = row, col
    print(ROW, COL)
    return ROW, COL



WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mecanix: The Gear Game')

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = convert_pos(ROWS, game.board)
                gear = game.board.get_gear(row, col)
                game.board.move(gear, 'green', WIN)

        game.update()


    pygame.quit()

main()


