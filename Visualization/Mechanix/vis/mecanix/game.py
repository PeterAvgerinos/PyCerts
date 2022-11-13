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
        gear = self.board.get_gear(row, col)
        self.selected = gear
        if gear.fixed:
            print('oopsie daisy this gear is fixed to the board')
        elif gear.occupied:
            if self.turn == gear.color:
                self.board.move(row, col, 'transparent')
        else:
            self._move(row, col)
            print(self.turn, 'is playing')
            self.change_turn()




    # def select(self, row, col):
    #     if self.selected:
    #         result = self._move(row, col)
    #         if not result:
    #             self.selected = None
    #             self.select(row, col)
    #     else:
    #         gear = self.board.get_gear(row, col)
    #         if gear.color == 'transparent':
    #             self.selected = gear
    #             self._move(row, col)
    #             # self.valid_moves = self.board.get_valid_moves(gear)
    #             return True
    #     return False


    def _move(self, row, col):
        gear = self.board.get_gear(row, col)
        if self.selected and gear == 'transparent':
            self.board.move(gear, self.turn, self.win)
        elif self.selected and gear.color == self.turn:
            self.board.move(gear, 'transparent', self.win)

    def move(self, row, col):
        gear = self.board.get_gear(row, col)
        if self.selected and gear == 'transparent':
            self.board.move(gear, self.turn, self.win)

    def change_turn(self):
        if self.turn == 'blue':
            self.turn = 'green'
        else:
            self.turn = 'blue'
