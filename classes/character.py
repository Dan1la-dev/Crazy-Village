from math import floor
from random import randint
from typing import NoReturn


class Character:
    battle_class = None

    def __init__(self):
        """Initialize a character object with default values."""

        self.alive = True
        self.name = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.inventory = None
        self.mp = None
        self.ultimate = None
        self.money = 1000
        self.lvl = 1
        self.xp = 0

    def get_stats(self) -> NoReturn:
        """Prints the character's statistics."""
        print()
        print(f'⬇️ Ваша статистика ⬇️')
        print(f'🧑 Имя: {self.name}')
        print(f'🥋 Персонаж: {self.battle_class}')
        print(f'❤️ Здоровье: {self.hp}')
        print(f'🗡️ Атака: {self.attack}')
        print(f'🛡️ Защита: {self.defense}')
        print(f'🥇 Текущий уровень: {self.lvl}')
        print(f'✨ Текущий опыт: {self.xp}')
        print(f'🎒 Инвентарь: {self.inventory}')
        print(f'💧 Мана: {self.mp}')
        print(f'🪙 Деньги: {self.money}')
        print(f'🔥 Способность: {self.ultimate}')
        print()

    def take_damage(self, enemy_attack: int) -> int:
        """Reduce the character's hp by the amount of damage received.
        :param enemy_attack: The amount of damage the enemy is attacking the character with."""

        damage = floor(enemy_attack / (self.defense / 100 + 1))
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        return self.hp

    def get_defense(self) -> int:
        """Increase the character's defense randomly."""

        gotten_defense = randint(9, 20)
        self.defense += gotten_defense
        return self.defense

    def spend_money(self, spent_money: int) -> NoReturn:
        """Reduce the character's money by the amount spent.
        :param spent_money: it used to calculate character's balance"""
        self.money -= spent_money

    def earn_money(self, earned_money) -> NoReturn:
        """Increase the character's money by the amount earned.
         :param earned_money: it used to calculate character's balance"""
        self.money += earned_money

    def earn_xp(self, earned_xp) -> NoReturn:
        """Increase the character's xp by the amount earned.
         :param earned_xp: it used to calculate character's xp"""
        self.xp += earned_xp
