from math import floor
from typing import NoReturn


class Character:
    """ Base character class """
    def __init__(self):
        self.alive = True
        self.debt = False
        self.name = None
        self.battle_class = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.inventory = None
        self.mp = None
        self.ultimate = None
        self.money = 0
        self.lvl = 1
        self.xp = 0

    def get_stats(self) -> NoReturn:
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

    def take_damage(self, enemy_damage: int) -> int:
        self.hp -= enemy_damage
        if self.hp <= 0:
            print('Ваша мать сдохла')
            self.alive = False
        return self.hp

    def give_damage(self, enemy_hp: int, enemy_defense: int) -> int:
        enemy_hp -= floor(self.attack / (enemy_defense / 100 + 1))
        return enemy_hp

    def spend_money(self, spent_money: int) -> int:
        self.money -= spent_money
        if self.money < 0:
            self.debt = True
        return self.money
    
