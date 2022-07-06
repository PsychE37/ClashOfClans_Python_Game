from time import sleep
from os import system

from src import variables

def clean_up():
    system("clear")

def start_game():
    print("\t\t\t\t\t\t\t\tHello Chief, welcome to the world of CLASH OF CLANS")
    sleep(3)
    clean_up()

def win_game():
    print("\t\t\t\t\t\t\t\tCongratulations, you 3 starred all levels !!")
    sleep(3)
    clean_up()
    
def lose_game():
    print("\t\t\t\t\t\t\t\tIt's alright chief, we'll get those goblins next time")
    sleep(3)
    clean_up()
    
def end_game():
    print("\t\t\t\t\t\t\t\tPlease come again")
    sleep(3)
    clean_up()
    
def set_canvas(world , troops , buildings, spawns):
    world.make_canvas()
    variables.HERO.set_on_canvas(world)
    for build in buildings:
        if not build.destroyed:
            build.set_on_canvas(world)
    for troop in troops:
        if not troop.destroyed and (troop.__class__.__name__ != "King" and troop.__class__.__name__ != "Queen"):
            troop.set_on_canvas(world)
    for spawn in spawns:
        spawn.set_on_canvas(world)
            