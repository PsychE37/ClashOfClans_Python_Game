from os import system
import sys
import time
from time import sleep

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

from src import canvas,useme,variables,building,heroes,army

system("stty -echo")
sys.stdout.write("\033[?25l")
sys.stdout.flush()

inp = []
fi = input("Which replay would you like to watch ?")
with open("replays/" + fi+ ".txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        inp.append(line)
    f.close()
inp.append('q')

while 1:
    useme.start_game()
    hero = input("Which hero would you like to play with ?(K/Q)")
    getch = inp.Get()
    world = canvas.Canvas(variables.HEIGHT , variables.WIDTH , variables.ORIGIN_X , variables.ORIGIN_Y)
    world.make_canvas()
    cannon1 = building.Cannon(variables.ORIGIN_X+30,variables.ORIGIN_Y+10,3,3,80,1000)
    cannon1.make()
    variables.buildings.append(cannon1)
    cannon2 = building.Cannon(variables.ORIGIN_X+50,variables.ORIGIN_Y+30,3,3,80,1000)
    cannon2.make()
    variables.buildings.append(cannon2)
    tower1 = building.Tower(variables.ORIGIN_X+34,variables.ORIGIN_Y+21,3,3,80,1000)
    tower1.make()
    variables.buildings.append(tower1)
    tower2 = building.Tower(variables.ORIGIN_X+68,variables.ORIGIN_Y+29,3,3,80,1000)
    tower2.make()
    variables.buildings.append(tower2)
    if hero[0] == 'K':
        hero_dis = heroes.King()
        hero_dis.make()
    else:
        hero_dis = heroes.Queen()
        hero_dis.make()
    variables.HERO = hero_dis
    variables.troops.append(hero_dis)
    town_hall = building.TownHall(variables.ORIGIN_X+40,variables.ORIGIN_Y+20,4,3,0,1500)
    town_hall.make()
    variables.buildings.append(town_hall)
    hut1 = building.Hut(variables.ORIGIN_X+20,variables.ORIGIN_Y+31,3,3,0,300)
    hut1.make()
    variables.buildings.append(hut1)
    hut2 = building.Hut(variables.ORIGIN_X+80,variables.ORIGIN_Y+33,3,3,0,300)
    hut2.make()
    variables.buildings.append(hut2)
    hut3 = building.Hut(variables.ORIGIN_X+70,variables.ORIGIN_Y+5,3,3,0,300)
    hut3.make()
    variables.buildings.append(hut3)
    hut4 = building.Hut(variables.ORIGIN_X+10,variables.ORIGIN_Y+19,3,3,0,300)
    hut4.make()
    variables.buildings.append(hut4)
    hut5 = building.Hut(variables.ORIGIN_X+43,variables.ORIGIN_Y+14,3,3,0,300)
    hut5.make()
    variables.buildings.append(hut5)
    spawns = []
    sp1 = building.Spawnpoint(variables.ORIGIN_X+3,variables.ORIGIN_Y+24,1,1,0,0)
    sp1.make()
    sp2 = building.Spawnpoint(variables.ORIGIN_X+55,variables.ORIGIN_Y+35,1,1,0,0)
    sp2.make()
    sp3 = building.Spawnpoint(variables.ORIGIN_X+30,variables.ORIGIN_Y+4,1,1,0,0)
    sp3.make()
    spawns.append(sp1)
    spawns.append(sp2)
    spawns.append(sp3)
    walls = []
    for i in range(41):
        walls.append(building.Wall(variables.ORIGIN_X+20+i,variables.ORIGIN_Y+8,1,1,0,2000))
        walls.append(building.Wall(variables.ORIGIN_X+20+i,variables.ORIGIN_Y+25,1,1,0,2000))
        
    for i in range(16):
        walls.append(building.Wall(variables.ORIGIN_X+20,variables.ORIGIN_Y+9+i,1,1,0,2000))
        walls.append(building.Wall(variables.ORIGIN_X+60,variables.ORIGIN_Y+9+i,1,1,0,2000))
    for i in walls:
        i.make()
        variables.buildings.append(i)
    quit = 0
    player_win = 0
    player_lose = 0
    for line in inp:
        ch = line[0]
        if ch:
            if ch == 'q' or ch == 'Q':
                quit = 1
                break
        if (ch == 'a' or ch == 'A') and hero_dis.cur_health > 0:
            hero_dis.move(world,-1,0)
        if (ch == 'w' or ch == 'W') and hero_dis.cur_health > 0:
            hero_dis.move(world,0,-1)
        if (ch == 's' or ch == 'S') and hero_dis.cur_health > 0:
            hero_dis.move(world,0,1)
        if (ch == 'd' or ch == 'D') and hero_dis.cur_health > 0:
            hero_dis.move(world,1,0)
        if ch == ' ' and hero_dis.cur_health > 0:
            hero_dis.attack()
        if (ch == 'e' or ch == 'E') and variables.EAGLE_START_POINT == 0 and hero_dis.cur_health > 0 and hero_dis.__class__.__name__ == "Queen":
            variables.EAGLE_START_POINT = time.time()
        if (ch == 'r' or ch == 'R') and variables.RAGE_START_POINT == 0 and variables.RAGE > 0:
            variables.RAGE_START_POINT = time.time()
            variables.MULTIPLIER = 2
            variables.RAGE -= 1
        if (ch == 'h' or ch == 'H') and variables.HEAL > 0:
            variables.HEAL -= 1
            for i in variables.troops:
                i.cur_health = min(1.5 * i.cur_health, i.max_health)
        if ch == '1' and variables.BARBARIANS > 0:
            variables.troops.append(army.Barbarian(variables.ORIGIN_X+3,variables.ORIGIN_Y+24,1,1,50,300))
            # variables.barbarians.append(barbarian)
            variables.BARBARIANS -= 1
        if ch == '2' and variables.BARBARIANS > 0:
            variables.troops.append(army.Barbarian(variables.ORIGIN_X+55,variables.ORIGIN_Y+35,1,1,50,300))
            # variables.barbarians.append(barbarian)
            variables.BARBARIANS -= 1
        if ch == '3' and variables.BARBARIANS > 0:
            variables.troops.append(army.Barbarian(variables.ORIGIN_X+30,variables.ORIGIN_Y+4,1,1,50,300))
            # variables.barbarians.append(barbarian)
            variables.BARBARIANS -= 1
        if ch == '4' and variables.BALLOONS > 0:
            variables.troops.append(army.Balloon(variables.ORIGIN_X+3,variables.ORIGIN_Y+24,1,1,100,300))
            # variables.balloons.append(balloon)
            variables.BALLOONS -= 1
        if ch == '5' and variables.BALLOONS > 0:
            variables.troops.append(army.Balloon(variables.ORIGIN_X+55,variables.ORIGIN_Y+35,1,1,100,300))
            # variables.balloons.append(balloon)
            variables.BALLOONS -= 1
        if ch == '6' and variables.BALLOONS > 0:
            variables.troops.append(army.Balloon(variables.ORIGIN_X+30,variables.ORIGIN_Y+4,1,1,100,300))
            # variables.balloons.append(balloon)
            variables.BALLOONS -= 1
        if ch == '7' and variables.ARCHERS > 0:
            variables.troops.append(army.Archer(variables.ORIGIN_X+3,variables.ORIGIN_Y+24,1,1,25,150))
            # variables.archers.append(archer)
            variables.ARCHERS -= 1
        if ch == '8' and variables.ARCHERS > 0:
            variables.troops.append(army.Archer(variables.ORIGIN_X+55,variables.ORIGIN_Y+35,1,1,25,150))
            # variables.archers.append(archer)
            variables.ARCHERS -= 1
        if ch == '9' and variables.ARCHERS > 0:
            variables.troops.append(army.Archer(variables.ORIGIN_X+30,variables.ORIGIN_Y+4,1,1,25,150))
            # variables.archers.append(archer)
            variables.ARCHERS -= 1
        if time.time() - variables.RAGE_START_POINT > 5:
            variables.MULTIPLIER = 1
            variables.RAGE_START_POINT = 0
        if time.time() - variables.EAGLE_START_POINT > 1 and variables.EAGLE_START_POINT:
            hero_dis.eagle_attack()
            variables.EAGLE_START_POINT = 0
        cannon1.attack()
        cannon2.attack()
        if variables.LEVEL >= 2:
            cannon3.attack()
            if variables.LEVEL == 3:
                cannon4.attack()    
        tower1.attack()
        tower2.attack()
        if variables.LEVEL >= 2:
            tower3.attack()
            if variables.LEVEL == 3:
                tower4.attack()    
        win = 1
        lose = 1   
        for build in variables.buildings:
            if not build.destroyed and not isinstance(build, building.Wall):
                win = 0
        if win and variables.LEVEL == 3:
            player_win = 1
            break
        if win:
            variables.LEVEL += 1
            for build in variables.buildings:
                build.cur_health = build.max_health
                build.target = None
                build.destroyed = False
            for x in variables.troops:
                x.destroyed = True
                x.cur_health = 0
            variables.troops.clear()
            variables.ARCHERS = 10
            variables.BARBARIANS = 10
            variables.BALLOONS = 5
            variables.RAGE = 2
            variables.HEAL = 2
            variables.MULTIPLIER = 1
            variables.RAGE_START_POINT = 0
            if hero[0] == 'K':
                hero_dis = heroes.King()
                hero_dis.make()
            else:
                hero_dis = heroes.Queen()
                hero_dis.make()
            variables.troops.append(hero_dis)
            variables.HERO = hero_dis
            if variables.LEVEL == 2:
                    cannon3 = building.Cannon(variables.ORIGIN_X+16,variables.ORIGIN_Y+29,3,3,80,2000)
                    cannon3.make()
                    variables.buildings.append(cannon3)
                    tower3 = building.Tower(variables.ORIGIN_X+47,variables.ORIGIN_Y+11,3,3,80,2000)
                    tower3.make()
                    variables.buildings.append(tower3)
            elif variables.LEVEL == 3:
                    cannon4 = building.Cannon(variables.ORIGIN_X+11,variables.ORIGIN_Y+14,3,3,80,2000)
                    cannon4.make()
                    variables.buildings.append(cannon4)
                    tower4 = building.Tower(variables.ORIGIN_X+72,variables.ORIGIN_Y+21,3,3,80,2000)
                    tower4.make()
                    variables.buildings.append(tower4)
        useme.set_canvas(world, variables.troops, variables.buildings, spawns)
        world.draw_canvas()
        
    if player_win:
        for x in variables.troops:
            if not x.destroyed:
                lose = 0
        if lose:
            player_lose = 1
            break
        useme.win_game()
        break
    if player_lose:
        useme.lose_game()
        break
    if quit:
        useme.end_game()
        break
    
system("stty echo")
sys.stdout.write("\033[?25h")
sys.stdout.flush()