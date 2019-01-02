import random

class Sim(object):
    def __init__(self, x=40, y=40):
        self.board = []
        self.x = x
        self.y = y

        self.clear()

    def clear(self):
        for x in range(self.x):
            r = []
            for y in range(self.y):
                r.append(0)
            self.board.append(r)

    def run(self):
        for x in range(self.x):
            for y in range(self.y):
                self.board[x][y] = random.randint(0,1)

    def get(self, x, y):
        return self.board[x][y]

    def getn(self, x, y, direction):
        if direction == "n":
            return self.board[x-1][y]
        elif direction == "s":
            return self.boaed[x+1][y]
        elif direction == "w":
            return self.board[x][y-1]
        elif direction == "e":
            return self.board[x][y+1]

    def print(self):
        for row in self.board:
            print(row)
