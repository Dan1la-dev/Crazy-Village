from entities.enemies.simple.barbarian import Barbarian
from entities.enemies.simple.ghost import Ghost
from entities.enemies.simple.goblin import Goblin
from entities.enemies.Necron import ComradVorobey
from random import choice


def pick_enemy():
    """Sets enemy"""
    enemies = [Barbarian(), Ghost(), Goblin(), ComradVorobey()]
    return choice(enemies)
