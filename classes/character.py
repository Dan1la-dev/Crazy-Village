from math import floor
from random import randint
from typing import NoReturn


class Character:
    battle_class = None
    """ Base character class """
    def __init__(self):
        self.alive = True
        self.debt = False
        self.name = None
        self.battle_moves = ["Атаковать", "Защититься"]
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
        damage = floor(enemy_attack / (self.defense / 100 + 1))
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False
        return self.hp

    def get_defense(self) -> int:
        gotten_defense = randint(9, 20)
        self.defense += gotten_defense
        return self.defense

    def spend_money(self, spent_money: int) -> NoReturn:
        self.money -= spent_money
        if self.money < 0:
            self.debt = True

    def earn_money(self, earned_money) -> NoReturn:
        self.money += earned_money

    def earn_xp(self, earned_xp) -> NoReturn:
        self.xp += earned_xp


