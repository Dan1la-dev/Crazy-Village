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

    def get_stats(self) -> NoReturn:
        print(f'Enemy Type: {self.type}')
        print(f'HP: {self.hp}')
        print(f'Attack: {self.attack}')
        print(f'Defense: {self.defense}')
        print(f'Ultimate: {self.ultimate}')

    def take_damage(self, character_attack: int) -> NoReturn:
        damage = floor(character_attack / (self.defense / 100 + 1))
        self.hp -= damage

    def check_hp(self):
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        return self.alive

    def get_defense(self) -> NoReturn:
        self.defense += randint(2, 6)


