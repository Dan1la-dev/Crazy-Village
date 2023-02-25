from math import floor
from random import randint


class Enemy:
    type = None

    def __init__(self):
        """Initialize a character object with default values."""
        self.alive = True
        self.hp = None
        self.attack = None
        self.defense = None
        self.ultimate = None

    def take_damage(self, character_attack: int) -> int:
        """Reduce the character's hp by the amount of damage received.
        :param character_attack: it used to calculate characters's damage to enemy"""

        damage = floor(character_attack / (self.defense / 100 + 1))
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        return damage

    def show_hp(self):
        return self.hp

    def get_defense(self) -> int:
        """Increase the character's defense randomly."""
        defense = randint(5, 9)
        self.defense += randint(5, 9)
        return defense

    def show_defense(self):
        return self.defense

