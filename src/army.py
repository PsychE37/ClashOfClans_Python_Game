from time import sleep
from src import entity
from src import variables
from src import building

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Barbarian(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.height = 1
        self.width = 1
        self.arr = []
        self.color = Back.BLUE
        self.target = None
        self.target_x = None
        self.target_y = None
        self.range = 1
    
    def set_on_canvas(self,game):
        nbuildings = []
        for build in variables.buildings:
            if not build.destroyed:
                nbuildings.append(build)
        if self.target == None or self.target.destroyed:
            closest = nbuildings[0]
            for builds in nbuildings:
                if not builds.destroyed and not isinstance(builds, building.Wall) and variables.distance(self.x_pos,self.y_pos,closest.x_pos,closest.y_pos) >= variables.distance(self.x_pos,self.y_pos,builds.x_pos,builds.y_pos):
                    self.target_x = variables.closest_point(builds.points_arr_x,self.x_pos)
                    self.target_y = variables.closest_point(builds.points_arr_y,self.y_pos)
                    closest = builds
                    self.target = closest
        if self.target == None or self.target_x == None:
            return
        if self.target_y != self.y_pos:
            dx = variables.MULTIPLIER
            if self.target_x < self.x_pos:
                dx = -1
            elif self.target_x > self.x_pos:
                dx *= 1
            else:
                dx *= 0
            if dx != 0:
                if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLUE +'x')):
                    self.x_pos += dx 
                else:
                    self.attack(game,self.x_pos+dx,self.y_pos)
            else:
                dy = variables.MULTIPLIER
                if self.target_y+1 < self.y_pos:
                    dy = -1
                elif self.target_y-1 > self.y_pos:
                    dy *= 1
                else: 
                    dy *= 0
                if dy == 0:
                    self.attack(game,self.target_x,self.target_y)
                else:
                    if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos + dy][self.x_pos] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos + dy][self.x_pos] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos + dy][self.x_pos] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos + dy][self.x_pos] == Back.BLACK + Fore.BLUE +'x')):
                        self.y_pos += dy
                    else:
                        self.attack(game,self.x_pos,self.y_pos + dy)
        else:
            dx = variables.MULTIPLIER
            if self.target_x+1 < self.x_pos:
                dx = -1
            elif self.target_x-1 > self.x_pos:
                dx *= 1
            else:
                dx *= 0
            if dx != 0:
                if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLUE +'x')):
                    self.x_pos += dx 
                else:
                    self.attack(game,self.x_pos + dx,self.y_pos)
            else:
                self.attack(game,self.target_x,self.target_y)
        game.grid[self.y_pos][self.x_pos] = self.color + 'B'
        
    def attack(self, game, x , y):
        for build in variables.buildings:
            for i in range(len(build.points_arr_x)):
                if build.points_arr_x[i] == x and build.points_arr_y[i] == y:
                    if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                        build.cur_health = 0
                        build.destroyed = True
                        self.target_x = None
                        self.target_y = None
                    else:
                        build.cur_health -= self.damage*variables.MULTIPLIER
    
class Balloon(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.height = 1
        self.width = 1
        self.arr = []
        self.color = Back.RED
        self.flying = True
        self.target = None
        self.target_x = None
        self.target_y = None
    
    def set_on_canvas(self,game):
        threshold = -1
        nbuildings = []
        for build in variables.buildings:
            if not build.destroyed:
                nbuildings.append(build)
                if build.damage > 0:
                    threshold = 0              
        if self.target == None or self.target.destroyed:
            closest = nbuildings[0]
            for builds in nbuildings:
                if not builds.destroyed and builds.damage > threshold and not isinstance(builds, building.Wall) and variables.distance(self.x_pos,self.y_pos,closest.x_pos,closest.y_pos) >= variables.distance(self.x_pos,self.y_pos,builds.x_pos,builds.y_pos):
                    self.target_x = variables.closest_point(builds.points_arr_x,self.x_pos)
                    self.target_y = variables.closest_point(builds.points_arr_y,self.y_pos)
                    closest = builds
                    self.target = closest
        if self.target == None or self.target_x == None:
            return
        if self.target_y != self.y_pos:
            dx = variables.MULTIPLIER
            if self.target_x + 1 < self.x_pos:
                dx = -2
            elif self.target_x - 1 > self.x_pos:
                dx *= 2
            else:
                dx *= 0
            if dx != 0:
                if (False and (game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.GREEN + 'W' or game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.YELLOW + 'W' or game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.RED + 'W')):
                    self.attack(game,self.y_pos,self.x_pos+dx)
                elif (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2):
                    self.x_pos += dx 
            else:
                dy = variables.MULTIPLIER
                if self.target_y+1 < self.y_pos:
                    dy = -2
                elif self.target_y-1 > self.y_pos:
                    dy *= 2
                else: 
                    dy *= 0
                if dy == 0:
                    self.attack(game,self.target_x,self.target_y)
                else:
                    if (False and (game.grid[self.y_pos+dy][self.x_pos] == Fore.BLACK + Back.GREEN + 'W' or game.grid[self.y_pos+dy][self.x_pos] == Fore.BLACK + Back.YELLOW + 'W' or game.grid[self.y_pos+dy][self.x_pos] == Fore.BLACK + Back.RED + 'W')):
                        self.attack(game,self.y_pos + dy,self.x_pos)
                    elif (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2):
                        self.y_pos += dy
        else:
            dx = variables.MULTIPLIER
            if self.target_x+1 < self.x_pos:
                dx = -2
            elif self.target_x-1 > self.x_pos:
                dx *= 2
            else:
                dx *= 0
            if dx != 0:
                if (False and (game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.GREEN + 'W' or game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.YELLOW + 'W' or game.grid[self.y_pos][self.x_pos + dx] == Fore.BLACK + Back.RED + 'W')):
                    self.attack(game,self.y_pos,self.x_pos+dx)
                elif (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2):
                    self.x_pos += dx 
            else:
                self.attack(game,self.target_x,self.target_y)
        game.grid[self.y_pos][self.x_pos] = self.color + 'B'
            
    def attack(self, game, x , y):
        for build in variables.buildings:
            for i in range(len(build.points_arr_x)):
                if build.points_arr_x[i] == x and build.points_arr_y[i] == y:
                    if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                        build.cur_health = 0
                        build.destroyed = True
                        self.target_x = None
                        self.target_y = None
                    else:
                        build.cur_health -= self.damage*variables.MULTIPLIER
                        
class Archer(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.height = 1
        self.width = 1
        self.arr = []
        self.color = Back.BLUE
        self.target = None
        self.target_x = None
        self.target_y = None
        self.range = 4
    
    def set_on_canvas(self,game):
        x = self.x_pos
        y = self.y_pos
        nbuildings = []
        for build in variables.buildings:
            if not build.destroyed:
                nbuildings.append(build)
                
        if self.target == None or self.target.destroyed:
            closest = nbuildings[0]
            for builds in nbuildings:
                if not builds.destroyed and not isinstance(builds, building.Wall) and variables.distance(self.x_pos,self.y_pos,closest.x_pos,closest.y_pos) >= variables.distance(self.x_pos,self.y_pos,builds.x_pos,builds.y_pos):
                    self.target_x = variables.closest_point(builds.points_arr_x,self.x_pos)
                    self.target_y = variables.closest_point(builds.points_arr_y,self.y_pos)
                    closest = builds
                    self.target = closest
        else:
            if self.target == None or self.target_x == None:
                return
            if variables.distance(self.x_pos,self.y_pos,self.target_x,self.target_y) <= self.range:
                self.attack(game, self.target_x, self.target_y)
            else:
                x = 0
                y = 0
                if self.target_y != self.y_pos:
                    dx = variables.MULTIPLIER
                    if self.target_x + 1 < self.x_pos:
                        dx = -2
                    elif self.target_x - 1 > self.x_pos:
                        dx *= 2
                    else:
                        dx *= 0
                    if dx != 0:
                        if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLUE +'x') and (game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.BLACK + Fore.BLUE +'x')):
                            self.x_pos += dx 
                        else:
                            self.attack(game,self.x_pos+dx,self.y_pos)
                            self.attack(game,self.x_pos+int(dx/2),self.y_pos)
                    else:
                        dy = variables.MULTIPLIER
                        if self.target_y+1 < self.y_pos:
                            dy = -2
                        elif self.target_y-1 > self.y_pos:
                            dy *= 2
                        else: 
                            dy *= 0
                        if dy == 0:
                            self.attack(game,self.target_x,self.target_y)
                        else:
                            if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos + dy][self.x_pos] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos + dy][self.x_pos] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos + dy][self.x_pos] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos + dy][self.x_pos] == Back.BLACK + Fore.BLUE +'x') and (game.grid[self.y_pos + int(dy/2)][self.x_pos] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos + int(dy/2)][self.x_pos] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos + int(dy/2)][self.x_pos] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos + int(dy/2)][self.x_pos] == Back.BLACK + Fore.BLUE +'x')):
                                self.y_pos += dy
                            else:
                                self.attack(game,self.x_pos,self.y_pos + dy)
                                self.attack(game,self.x_pos,self.y_pos + int(dy/2))
                else:
                    dx = variables.MULTIPLIER
                    if self.target_x+1 < self.x_pos:
                        dx = -2
                    elif self.target_x-1 > self.x_pos:
                        dx *= 2
                    else:
                        dx *= 0
                    if dx != 0:
                        if (self.x_pos + dx <= variables.ORIGIN_X + variables.WIDTH - 3 and self.x_pos + dx >= variables.ORIGIN_X + 2 and (game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + dx] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + dx] == Back.BLACK + Fore.BLUE +'x') and (game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.BLACK + Fore.BLACK + " " or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.YELLOW + Fore.RED + 'Q' or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.YELLOW + Fore.RED + 'K' or game.grid[self.y_pos][self.x_pos + int(dx/2)] == Back.BLACK + Fore.BLUE +'x')):
                            self.x_pos += dx 
                        else:
                            self.attack(game,self.x_pos+dx,self.y_pos)
                            self.attack(game,self.x_pos+int(dx/2),self.y_pos)
                    else:
                        self.attack(game,self.target_x,self.target_y)
            if game.grid[self.y_pos][self.x_pos] != Back.BLACK + Fore.BLACK + " ":
                for i in range(3):
                    for j in range(3):
                        self.attack(game,self.x_pos-1+j,self.y_pos-1+i)
            else:
                game.grid[self.y_pos][self.x_pos] = self.color + "A"
            if self.x_pos == x and self.y_pos == y:
                for i in range(3):
                    for j in range(3):
                        self.attack(game,self.x_pos-1+j,self.y_pos-1+i)
                    
    def attack(self, game, x , y):
        for build in variables.buildings:
            for i in range(len(build.points_arr_x)):
                if build.points_arr_x[i] == x and build.points_arr_y[i] == y:
                    if build.cur_health - self.damage*variables.MULTIPLIER <= 0:
                        build.cur_health = 0
                        build.destroyed = True
                        self.target_x = None
                        self.target_y = None
                    else:
                        build.cur_health -= self.damage*variables.MULTIPLIER