import pygame

class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)),
                           ((0,400), (600,400)),
                           ((200,0), (200,600)),
                           ((400,0), (400,600))]
        self.grid = [[0 for x in range(3)] for y in range(3)]

    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface,(200,200,200), line[0], line[1], 4)
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                cell_lines = [((x * 200, y * 200), (x * 200 + 200, y * 200 + 200)),
                      ((x * 200 + 200, y * 200), (x * 200, y * 200 + 200))]
                if self.get_cell_value(x,y) == "X" :
                    for line in cell_lines:
                        pygame.draw.line(surface, (255, 0, 0), line[0], line[1], 10)
                elif self.get_cell_value(x,y) == "O":
                    pygame.draw.ellipse(surface, (0, 255, 0), (x*200, y*200, 200, 200), 10)

    def print_grid(self):
        for row in self.grid:
            print(row)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def is_grid_full(self):
        for row in self.grid:
            for value in row:
                if value == 0:
                    return False
        return True

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range (len(self.grid[y])):
                self.set_cell_value(x, y, 0)

    def available(self, x, y):
        if(self.get_cell_value(x,y) != 0):
            return False
        else:
            return True
    def equal3(self, a, b, c):
        if (a==b and b==c and a!=0):
            return True

    def checkWinner(self):
        self.winner = 0
        for j in range(3):
            if(self.equal3(self.grid[j][0],self.grid[j][1],self.grid[j][2])):
                self.winner = self.grid[j][0]
        for i in range(3):
            if (self.equal3(self.grid[0][i],self.grid[1][i],self.grid[2][i])):
                self.winner = self.grid[0][i]
        if (self.equal3(self.grid[0][0],self.grid[1][1],self.grid[2][2])):
            self.winner = self.grid[1][1]

        if (self.equal3(self.grid[0][2],self.grid[1][1],self.grid[2][0])):
            self.winner = self.grid[1][1]

        return self.winner


    def get_mouse(self, x, y, player):
            if player == "X":
                self.set_cell_value(x, y, "X")
            elif player == "O":
                self.set_cell_value(x, y, "O")

