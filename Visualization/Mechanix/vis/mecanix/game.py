import pygame
from .board import Board

class Game:
    def __init__(self, win):
        self.win = win
        self._init()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.board.create_board(self.win)
        self.turn = 'blue'
        self.valid_moves = {}

    def update(self):
        self.board.update_board(self.win)
        pygame.display.update()

    def reset(self):
        self._init()

    def quit(self):
        pygame.quit()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col, self.turn)
            if not result:
                self.selected = None
                self.select(row, col)
        else:
            gear = self.board.get_gear(row, col)
            if gear != None and gear.color == 'transparent':
                self.selected = gear
                # self.valid_moves = self.board.get_valid_moves(gear)
                return True
        return False


    def _move(self, row, col, color):
        gear = self.board.get_gear(row, col)
        if self.selected and gear == 'transparent'

    def change_turn(self):
        if self.turn == 'blue':
            self.turn = 'green'
        else:
            self.turn = 'blue'
