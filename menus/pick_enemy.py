from entities.enemies.simple.barbarian import Barbarian
from entities.enemies.simple.ghost import Ghost
from entities.enemies.simple.goblin import Goblin
from entities.enemies.bosses.necron import Necron
from random import choice


def pick_enemy():
    """Sets enemy"""
    enemies = [Barbarian(), Ghost(), Goblin(), Necron()]
    return choice(enemies)
