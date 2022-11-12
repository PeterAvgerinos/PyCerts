import pygame
from .board import Board

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def _init(self):
        self.selected = None
        self.board = Board(self.win)
        self.turn = 'blue'
        self.valid_moves = {}

    def update(self):
        self.board.update(self.win)
        pygame.display.update()

    def reset(self):
        self._init()
