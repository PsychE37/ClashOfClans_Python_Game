from src import entity
from src import variables

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class King(entity.Entity):
    def __init__(self):
        super().__init__(variables.ORIGIN_X + int(variables.WIDTH/2), variables.HEIGHT - 3, 1, 1, 200, 5000)
        self.color = Back.YELLOW + Fore.RED
        self.cross_color = Back.BLACK + Fore.BLUE
        self.arr = []
        self.aim_x = self.x_pos 
        self.aim_y = self.y_pos - 1
        self.sight = []

    def make(self):
        self.arr = []
        self.arr.append('K')
        self.sight = []
        self.sight.append('x')
         
    def set_on_canvas(self,game):
        self.health_bar = "King's Health:"
        x = int((self.cur_health*100)/self.max_health)
        for i in range(x):
            self.health_bar += " "      
        game.grid[self.y_pos][self.x_pos] = self.color + self.arr[0]
        if self.aim_x <= variables.ORIGIN_X + variables.WIDTH - 2 and self.aim_x >= variables.ORIGIN_X + 1 and self.aim_y <= variables.ORIGIN_Y + variables.HEIGHT- 2 and self.aim_y >= variables.ORIGIN_Y + 1:
            game.grid[self.aim_y][self.aim_x] = self.cross_color + self.sight[0]
        for i in range(14):
            game.grid[variables.HEIGHT - 1][variables.ORIGIN_X + 2 + i] = Fore.BLACK + self.health_bar[i]
        for i in range(len(self.health_bar)-14):
            game.grid[variables.HEIGHT - 1][variables.ORIGIN_X + 16 + i] = Back.GREEN + self.health_bar[i+14]
        
    def move(self, game , x , y):
        dx = variables.MULTIPLIER*x
        dy = variables.MULTIPLIER*y
        if (self.x_pos + x == self.aim_x and self.y_pos + y == self.aim_y):
            if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 2 and self.x_pos + dx >= variables.ORIGIN_X + 1 and game.grid[self.y_pos][self.x_pos + x] == self.cross_color + self.sight[0]):
                self.x_pos += dx 
                self.aim_x += dx
            if (self.y_pos + dy <= variables.ORIGIN_Y + variables.HEIGHT- 2 and self.y_pos + dy >= variables.ORIGIN_Y + 1 and game.grid[self.y_pos + y][self.x_pos] == self.cross_color + self.sight[0]):
                self.y_pos += dy  
                self.aim_y += dy    
        else:
            self.aim_x = self.x_pos + x 
            self.aim_y = self.y_pos + y

    def attack(self):
        attacked = []
        for k in range(6):
            for j in range(6):
                if variables.distance(self.x_pos + k,self.y_pos + j,self.x_pos,self.y_pos) <= 5:
                    for build in variables.buildings:
                        for i in range(len(build.points_arr_x)):
                            if build.points_arr_x[i] == self.x_pos + k and build.points_arr_y[i] == self.y_pos + j and attacked.count(build) == 0:
                                if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                    build.cur_health = 0
                                    build.destroyed = True
                                else:
                                    build.cur_health -= self.damage*variables.MULTIPLIER
                                attacked.append(build)
                            if build.points_arr_x[i] == self.x_pos - k and build.points_arr_y[i] == self.y_pos + j and attacked.count(build) == 0:
                                if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                    build.cur_health = 0
                                    build.destroyed = True
                                else:
                                    build.cur_health -= self.damage*variables.MULTIPLIER
                                attacked.append(build)
                            if build.points_arr_x[i] == self.x_pos + k and build.points_arr_y[i] == self.y_pos - j and attacked.count(build) == 0:
                                if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                    build.cur_health = 0
                                    build.destroyed = True
                                else:
                                    build.cur_health -= self.damage*variables.MULTIPLIER
                                attacked.append(build)
                            if build.points_arr_x[i] == self.x_pos - k and build.points_arr_y[i] == self.y_pos - j and attacked.count(build) == 0:
                                if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                    build.cur_health = 0
                                    build.destroyed = True
                                else:
                                    build.cur_health -= self.damage*variables.MULTIPLIER
                                attacked.append(build)
   

class Queen(entity.Entity):
    def __init__(self):
        super().__init__(variables.ORIGIN_X + int(variables.WIDTH/2), variables.HEIGHT - 3, 1, 1, 150, 5000)
        self.color = Back.YELLOW + Fore.RED
        self.cross_color = Back.BLACK + Fore.BLUE
        self.arr = []
        self.aim_x = self.x_pos 
        self.aim_y = self.y_pos - 8
        self.sight = []

    def make(self):
        self.arr = []
        self.arr.append('Q')
        self.sight = []
        self.sight.append('x')
         
    def set_on_canvas(self,game):
        self.health_bar = "Queen's Health:"
        x = int((self.cur_health*100)/self.max_health)
        for i in range(x):
            self.health_bar += " "      
        game.grid[self.y_pos][self.x_pos] = self.color + self.arr[0]
        if self.aim_x <= variables.ORIGIN_X + variables.WIDTH - 2 and self.aim_x >= variables.ORIGIN_X + 1 and self.aim_y <= variables.ORIGIN_Y + variables.HEIGHT- 2 and self.aim_y >= variables.ORIGIN_Y + 1:
            game.grid[self.aim_y][self.aim_x] = self.cross_color + self.sight[0]
        for i in range(15):
            game.grid[variables.HEIGHT - 1][variables.ORIGIN_X + 2 + i] = Fore.BLACK + self.health_bar[i]
        for i in range(len(self.health_bar)-15):
            game.grid[variables.HEIGHT - 1][variables.ORIGIN_X + 17 + i] = Back.GREEN + self.health_bar[i+15]
        
    def move(self, game , x , y):
        dx = variables.MULTIPLIER*x
        dy = variables.MULTIPLIER*y
        if (self.x_pos + x*8 == self.aim_x and self.y_pos + y*8 == self.aim_y):
            if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 2 and self.x_pos + dx >= variables.ORIGIN_X + 1 and game.grid[self.y_pos][self.x_pos + x] == Back.BLACK + Fore.BLACK + " " and game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLACK + " "):
                self.x_pos += dx 
                self.aim_x += dx
            if (self.y_pos + dy <= variables.ORIGIN_Y + variables.HEIGHT- 2 and self.y_pos + dy >= variables.ORIGIN_Y + 1 and game.grid[self.y_pos + y][self.x_pos] == Back.BLACK + Fore.BLACK + " " and game.grid[self.y_pos + dy][self.x_pos] == Back.BLACK + Fore.BLACK + " "):
                self.y_pos += dy 
                self.aim_y += dy    
        else:
            self.aim_x = self.x_pos + x*8
            self.aim_y = self.y_pos + y*8

    def attack(self):
        attacked = []
        for k in range(3):
            for j in range(3):
                for build in variables.buildings:
                    for i in range(len(build.points_arr_x)):
                        if build.points_arr_x[i] == self.aim_x + k and build.points_arr_y[i] == self.aim_y + j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True 
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x - k and build.points_arr_y[i] == self.aim_y + j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x + k and build.points_arr_y[i] == self.aim_y - j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x - k and build.points_arr_y[i] == self.aim_y - j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)                  
                            
    def eagle_attack(self):
        x = self.aim_x - self.x_pos
        y = self.aim_y - self.y_pos
        attacked = []
        for k in range(5):
            for j in range(5):
                for build in variables.buildings:
                    for i in range(len(build.points_arr_x)):
                        if build.points_arr_x[i] == self.aim_x + x + k and build.points_arr_y[i] == self.aim_y + y + j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True 
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x + x - k and build.points_arr_y[i] == self.aim_y + y + j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x + x + k and build.points_arr_y[i] == self.aim_y + y - j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)
                        if build.points_arr_x[i] == self.aim_x + x - k and build.points_arr_y[i] == self.aim_y + y - j and attacked.count(build) == 0:
                            if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                                build.cur_health = 0
                                build.destroyed = True
                            else:
                                build.cur_health -= self.damage*variables.MULTIPLIER
                            attacked.append(build)       