from src import entity
from src import variables

import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

class Cannon(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.arr = []
        self.color = Fore.BLACK
        self.color_alt = Fore.GREEN
        self.target = None
        
    def make(self):
        self.points_arr_x = []
        self.points_arr_y = []
        for i in range(self.width):
            for j in range(self.height):
                self.points_arr_x.append(self.x_pos + i)
                self.points_arr_y.append(self.y_pos + j)
        self.destroyed = False
    
    def set_on_canvas(self,game):
        if float(self.cur_health/self.max_health)*100 > 50:
            self.color += Back.GREEN
        elif float(self.cur_health/self.max_health)*100 > 20:
            self.color += Back.YELLOW
        elif float(self.cur_health/self.max_health)*100 > 0:
            self.color += Back.RED
        for i in range(self.width):
            for j in range(self.height):
                if self.target == None:
                    game.grid[self.y_pos + i][self.x_pos + j] = self.color + 'C'
                else:
                    game.grid[self.y_pos + i][self.x_pos + j] = self.color + '*'
                                    
    def attack(self):
        if not self.destroyed:
            if self.target == None:
                for i in variables.troops:
                    if not i.flying and variables.distance(self.x_pos,self.y_pos,i.x_pos,i.y_pos) <= 6 and self.target == None:
                        if i.cur_health > self.damage:
                            self.target = i
                            i.cur_health -= self.damage
                        else:
                            i.cur_health = 0
                            i.destroyed = True
                            self.target = None
            else:
                if variables.distance(self.x_pos,self.y_pos,self.target.x_pos,self.target.y_pos) <= 6:
                    if self.target.cur_health > self.damage:
                        self.target.cur_health -= self.damage
                    else:
                        self.target.cur_health = 0
                        self.target.destroyed = True
                        self.target = None
                else:
                    self.target = None
                    
class Tower(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.arr = []
        self.color = Fore.BLACK
        self.color_alt = Fore.GREEN
        self.target = None
        
    def make(self):
        self.points_arr_x = []
        self.points_arr_y = []
        for i in range(self.width):
            for j in range(self.height):
                self.points_arr_x.append(self.x_pos + i)
                self.points_arr_y.append(self.y_pos + j)
        self.destroyed = False
    
    def set_on_canvas(self,game):
        if float(self.cur_health/self.max_health)*100 > 50:
            self.color += Back.GREEN
        elif float(self.cur_health/self.max_health)*100 > 20:
            self.color += Back.YELLOW
        elif float(self.cur_health/self.max_health)*100 > 0:
            self.color += Back.RED
        for i in range(self.width):
            for j in range(self.height):
                if self.target == None:
                    game.grid[self.y_pos + i][self.x_pos + j] = self.color + 'Z'
                else:
                    game.grid[self.y_pos + i][self.x_pos + j] = self.color + '*'
                            
    def attack(self):
        if not self.destroyed:
            if self.target == None:
                for i in variables.troops:
                    if variables.distance(self.x_pos,self.y_pos,i.x_pos,i.y_pos) <= 6 and self.target == None:
                        if i.cur_health > self.damage:
                            self.target = i
                            i.cur_health -= self.damage
                            for troop in variables.troops:
                                if variables.distance(self.target.x_pos,self.target.y_pos,troop.x_pos,troop.y_pos) <= math.sqrt(2) and variables.distance(self.target.x_pos,self.target.y_pos,troop.x_pos,troop.y_pos) > 0:
                                    if troop.cur_health > self.damage:
                                        troop.cur_health -= self.damage
                                    else:
                                        troop.cur_health = 0
                                        troop.destroyed = True
                        else:
                            i.cur_health = 0
                            i.destroyed = True
                            self.target = None
            else:
                if variables.distance(self.x_pos,self.y_pos,self.target.x_pos,self.target.y_pos) <= 6:
                    if self.target.cur_health > self.damage:
                        self.target.cur_health -= self.damage
                        for troop in variables.troops:
                            if variables.distance(self.target.x_pos,self.target.y_pos,troop.x_pos,troop.y_pos) <= math.sqrt(2) and variables.distance(self.target.x_pos,self.target.y_pos,troop.x_pos,troop.y_pos) > 0:
                                if troop.cur_health > self.damage:
                                    troop.cur_health -= self.damage
                                else:
                                    troop.cur_health = 0
                                    troop.destroyed = True
                    else:
                        self.target.cur_health = 0
                        self.target.destroyed = True
                        self.target = None
                else:
                    self.target = None
                    
class TownHall(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.arr = []
        self.color = Fore.BLACK
        
    def make(self):
        self.points_arr_x = []
        self.points_arr_y = []
        for i in range(self.width):
            for j in range(self.height):
                self.points_arr_x.append(self.x_pos + i)
                self.points_arr_y.append(self.y_pos + j)
        self.destroyed = False
    
    def set_on_canvas(self,game):
        if float(self.cur_health/self.max_health)*100 > 50:
            self.color += Back.GREEN
        elif float(self.cur_health/self.max_health)*100 > 20:
            self.color += Back.YELLOW
        elif float(self.cur_health/self.max_health)*100 > 0:
            self.color += Back.RED
        for i in range(self.width):
            for j in range(self.height):
                game.grid[self.y_pos + i][self.x_pos + j] = self.color + 'T'
                
class Hut(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.arr = []
        self.color = Fore.BLACK
        
    def make(self):
        self.points_arr_x = []
        self.points_arr_y = []
        for i in range(self.width):
            for j in range(self.height):
                self.points_arr_x.append(self.x_pos + i)
                self.points_arr_y.append(self.y_pos + j)
        self.destroyed = False
    
    def set_on_canvas(self,game):
        if float(self.cur_health/self.max_health)*100 > 50:
            self.color += Back.GREEN
        elif float(self.cur_health/self.max_health)*100 > 20:
            self.color += Back.YELLOW
        elif float(self.cur_health/self.max_health)*100 > 0:
            self.color += Back.RED
        for i in range(self.width):
            for j in range(self.height):
                game.grid[self.y_pos + i][self.x_pos + j] = self.color + 'H'
                
class Wall(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.height = 1
        self.width = 1
        self.arr = []
        self.color = Fore.BLACK
        
    def make(self):
        self.points_arr_x = [self.x_pos]
        self.points_arr_y = [self.y_pos]
        self.destroyed = False
    
    def set_on_canvas(self,game):
        if float(self.cur_health/self.max_health)*100 > 50:
            self.color += Back.GREEN
        elif float(self.cur_health/self.max_health)*100 > 20:
            self.color += Back.YELLOW
        elif float(self.cur_health/self.max_health)*100 > 0:
            self.color += Back.RED
        game.grid[self.y_pos][self.x_pos] = self.color + 'W'
        
class Spawnpoint(entity.Entity):
    def __init__(self, x_pos, y_pos, height, width, damage, health):
        super().__init__(x_pos, y_pos, height, width, damage, health)
        self.height = 1
        self.width = 1
        self.color = Fore.RED + Back.WHITE
        
    def make(self):
        self.points_arr_x = [self.x_pos]
        self.points_arr_y = [self.y_pos]
        self.destroyed = False
    
    def set_on_canvas(self,game):
        game.grid[self.y_pos][self.x_pos] = self.color + 'S'