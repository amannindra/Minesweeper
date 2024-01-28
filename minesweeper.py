import random


class Minesweeper():
    def __init__(self):
        self.grid = []
        self.bomb = []
        self.flagged = []
        self.probability = 20
        self.Total = 30
        self.game = True
    def create_grid(self):
        for row in range(10):
            row_grid = []
            row_flagged = []
            for col in range(10):
                row_grid.append("0")
                row_flagged.append(False)
            self.grid.append(row_grid)
            self.flagged.append(row_flagged)
        self.set_bomb()
    def set_bomb(self):
        for i in range(10):
            row_bomb = []
            for j in range(10):
                if random.randint(1, 100) < self.probability and self.Total != 0:
                    row_bomb.append(True)
                    self.Total -= 1
                else:
                    row_bomb.append(False)
            self.bomb.append(row_bomb)

    def reveal_all(self):
        for i in range(10):
            for j in range(10):
                self.around(i, j)

    def print_grid(self):
        for i in range(10):
            for j in range(10):
                print(self.grid[i][j])
        print()
        # for i in range(10):
        #   print(self.bomb[i])

    def get_x(self):
        user = int(input("From 1 to 10. Click Square(x): "))
        return user - 1
    def get_y(self):
        user = int(input("From 1 to 10. Click Square(y):"))
        return user - 1

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

    def Run(self):
        #self.probability = int(input("Probability of Mines?(In Percentage, no 0.25 only 25): "))
        self.set_bomb()
        while self.game:
            self.print_grid()
            x = self.get_x()
            y = self.get_y()
            self.around(x, y)
            self.game = False
        print("Done!")


Mine = Minesweeper()
Mine.Run()
