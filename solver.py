import numpy as np


class Game:
    def __init__(self):
        self.size = 5
        self.board = np.zeros((self.size, self.size), dtype=int)

    def disp(self):
        print('+-----------------------+')
        for i in range(len(self.board[0])):
            print(0)

    def main(self):
        self.disp()

game = Game()
game.main()

