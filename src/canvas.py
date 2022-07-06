import colorama
from colorama import Fore, Back, Style
from numpy import var
colorama.init(autoreset=True)

from src import variables

class Canvas:
    def __init__(self , a, b, x, y):
        self.rows = a
        self.columns = b
        self.origin_x = x
        self.origin_y = y
        self.grid = []
        
    def make_canvas(self):
        self.grid = []
        for i in range(self.rows + self.origin_y):
            rows = []
            if i < self.origin_y:
                for j in range(self.columns + self.origin_x):
                    rows.append(Back.RESET + " ")
            else:
                for j in range(self.columns + self.origin_x):
                    if j < self.origin_x:
                        rows.append(Back.RESET + " ")
                    else:
                        if i == self.origin_y or i == self.origin_y + self.rows -1 or  j == self.origin_x + self.columns -1 or j == self.origin_x:
                            rows.append(Back.WHITE + Fore.WHITE + " ")
                        else:
                            rows.append(Back.BLACK + Fore.BLACK + " ")
            self.grid.append(rows)
    
    def draw_canvas(self):
        canvas = ""
        extra = "LEVEL: " + str(variables.LEVEL)
        for i in range(len(extra)):
            self.grid[0][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Army Left:"
        for i in range(len(extra)):
            self.grid[10][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Archers:"
        for _ in range(variables.ARCHERS):
            extra += "| "
        for i in range(len(extra)):
            self.grid[12][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Balloons:"
        for _ in range(variables.BALLOONS):
            extra += "| "
        for i in range(len(extra)):
            self.grid[14][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Barbarians:"
        for _ in range(variables.BARBARIANS):
            extra += "| "
        for i in range(len(extra)):
            self.grid[16][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Spells Left:"
        for i in range(len(extra)):
            self.grid[19][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Rage:"
        for _ in range(variables.RAGE):
            extra += "| "
        for i in range(len(extra)):
            self.grid[21][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        extra = "Heal:"
        for _ in range(variables.HEAL):
            extra += "| "
        for i in range(len(extra)):
            self.grid[23][10 + i] = Back.WHITE + Fore.BLACK + extra[i]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                canvas += self.grid[i][j]
            canvas += '\n'   
        print('\033[H' + canvas)