import os
import random
import math
from copy import deepcopy

def clear_screen(): os.system('clear||cls')

class Tictactoe:
    def __init__(self):
        self.board = [0 for i in range(9)]
        self.history = []
        self.n_moves = 0
        self.X = '\N{MATHEMATICAL BOLD CAPITAL X}'
        self.O = '\N{MATHEMATICAL BOLD CAPITAL O}'
    def __str__(self):
        symbol = lambda x: 'X' if x == 1 else 'O' if x == -1 else ' '
        board = f'{symbol(self.board[0])}|{symbol(self.board[1])}|{symbol(self.board[2])}\n{symbol(self.board[3])}|{symbol(self.board[4])}|{symbol(self.board[5])}\n{symbol(self.board[6])}|{symbol(self.board[7])}|{symbol(self.board[8])}\n'
        return board

    def reference(self):
        ref = [i for i in range(9)]
        print(f'{ref[0]}|{ref[1]}|{ref[2]}\n{ref[3]}|{ref[4]}|{ref[5]}\n{ref[6]}|{ref[7]}|{ref[8]}\n')

    def get_state(self): 
        return ''.join(str(cell) for cell in self.board)

    def available_moves(self): 
        return list(set(range(9)) - set(self.history))

    def check(self):
        #  1: player 1 wins | -1: player 2 wins | 3: game not completed | 0: draw
        win = lambda a, b, c: 1 if a + b + c == 3 else -1 if a + b + c == -3 else None
        combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8),
                        (0, 4, 8), (2, 4, 6)]
        if self.n_moves >= 5:
            for a, b, c in combinations:
                result = win(self.board[a], self.board[b], self.board[c])
                if result is not None:
                    return result
            if self.n_moves == 9:
                return 0
        return 3

    def move(self, choice, mark):
        #assert(choice not in self.history)
        assert(choice in range(9))
        self.history.append(choice)
        self.n_moves += 1
        self.board[choice] = mark





