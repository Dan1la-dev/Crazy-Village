from entities.enemies.barbarian import Barbarian
from entities.enemies.ghost import Ghost
from entities.enemies.goblin import Goblin
from entities.enemies.vasif_swine import VasifSwine
from random import randint


def pick_enemy():
    enemies = {
        1: Barbarian(),
        2: Ghost(),
        3: Goblin(),
        4: VasifSwine(),
    }
    return enemies[randint(1, 4)]
