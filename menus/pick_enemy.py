from entities.enemies.barbarian import Barbarian
from entities.enemies.ghost import Ghost
from entities.enemies.goblin import Goblin
from entities.enemies.vasif_swine import VasifSwine
from random import choice


def pick_enemy():
    enemies = [Barbarian(), Ghost(), Goblin(), VasifSwine()]
    return choice(enemies)
