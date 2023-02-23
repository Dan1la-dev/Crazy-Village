from typing import NoReturn
from math import floor
from random import randint


class Enemy:
    def __init__(self):
        self.alive = True
        self.type = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.ultimate = None

    def take_damage(self, character_attack: int) -> int:
        damage = floor(character_attack / (self.defense / 100 + 1))
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        return self.hp

    def get_defense(self) -> int:
        self.defense += randint(5, 9)
        return self.defense


