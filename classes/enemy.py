from typing import NoReturn


class Enemy:
    type = None

    def __init__(self):
        """Initialize a character object with default values."""
        self.alive = True
        self.hp = None
        self.attack = None
        self.defense = None
        self.ultimate = None

    def get_damage(self, character_damage: int) -> NoReturn:
        """Reduce the character's hp by the amount of damage received.
        :param character_damage: it used to calculate characters's damage to enemy"""

        self.hp -= character_damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def get_defense(self, got_defense) -> NoReturn:
        """Increase the character's defense randomly."""
        self.defense += got_defense

    def show_hp(self):
        return self.hp

    def show_defense(self):
        return self.defense

    def show_attack(self) -> int:
        """Returns character's defense"""
        return self.attack

    def show_type(self):
        return self.type

