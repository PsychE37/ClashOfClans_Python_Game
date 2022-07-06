import os
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# COLUMNS, ROWS = os.get_terminal_size()

WIDTH = 120
HEIGHT = 40

ORIGIN_X = 50
ORIGIN_Y = 0

MULTIPLIER = 1

RAGE_START_POINT = 0
EAGLE_START_POINT = 0

LEVEL = 1

ARCHERS = 10
BARBARIANS = 10
BALLOONS = 5
RAGE = 2
HEAL = 2

buildings = []
troops = []

barbarians = []
archers = []
balloons = []

HERO = None

def distance(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def manhattan_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def closest_point(lst, K):
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

def damage_points(x , y , damage):
    for build in buildings:
            for i in range(len(build.points_arr_x)):
                 if build.points_arr_x[i] == x and build.points_arr_y[i] == y:
                    if build.cur_health - damage*MULTIPLIER <= 0:
                        build.cur_health = 0
                        build.destroyed = True
                    else:
                        build.cur_health -= damage*MULTIPLIER
                    break
    