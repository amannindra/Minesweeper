import random


class Minesweeper():
    def __init__(self):
        self.grid = []
        self.bomb = []
        self.flagged = []
        self.probability = 30
        self.game = True
        self.x = 1
        self.y = 1

    def create_grid(self):
        for i in range(10):
            row_grid = []
            row_flagged = []
            for i in range(10):
                row_grid.append("0")
                row_flagged.append(False)
            self.grid.append(row_grid)
            self.flagged.append(row_flagged)
        self.set_bomb()

    def set_flags(self):
        for i in range(10):
            row_flagged = []
            for i in range(10):
                row_flagged.append(False)
            self.flagged.append(row_flagged)

    def set_bomb(self):
        for i in range(10):
            row_bomb = []
            for i in range(10):
                if random.randint(1, 100) < self.probability:
                    row_bomb.append(True)
                else:
                    row_bomb.append(False)
            self.bomb.append(row_bomb)

    def change(self):
        for i in range(10):
            self.x = i
            for j in range(10): 
                self.y = j
                self.around(self.x, self.y)
    def print_grid(self):
        self.change()
        for i in range(10):
            print(self.grid[i])
    
        for i in range(10):
            print(self.bomb[i])
        print()
        for i in range(10):
            print(self.flagged[i])
    def get_x(self):
        self.x = input("Click Square(x): ")

    def get_y(self):
        self.y = input("Click Square(y): ")

    def check(self):
        for i in range(10):
            for j in range(10):
                if (self.bomb[i][j]):
                    self.game = False
    def around(self, x, y):
        bomb_count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 10 and 0 <= ny < 10 and (dx != 0 or dy != 0) and self.bomb[nx][ny]:
                    bomb_count += 1
        self.grid[x][y] = bomb_count
    

Mine = Minesweeper()
Mine.create_grid()
Mine.set_bomb()
Mine.set_flags()
Mine.print_grid()

