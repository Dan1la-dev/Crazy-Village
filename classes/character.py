from typing import NoReturn
from misc.consts import *
from time import sleep


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
        print(f'⬇ Ваша статистика ⬇')
        sleep(0.4)
        print(f'{CHARACTER} Имя: {self.name}')
        sleep(0.4)
        print(f'{TYPE} Персонаж: {self.battle_class}')
        sleep(0.4)
        print(f'{HEART} Здоровье: {self.hp}')
        sleep(0.4)
        print(f'{ATTACK} Атака: {self.attack}')
        sleep(0.4)
        print(f'{DEFENSE} Защита: {self.defense}')
        sleep(0.4)
        print(f'{LVL} Текущий уровень: {self.lvl}')
        sleep(0.4)
        print(f'{XP} Текущий опыт: {self.xp}')
        sleep(0.4)
        print(f'{INVENTORY} Инвентарь: {IN_DEVELOPING}')
        sleep(0.4)
        print(f'{MANA} Мана: {IN_DEVELOPING}')
        sleep(0.4)
        print(f'{MONEY} Деньги: {self.money}')
        sleep(0.4)
        print(f'{FIRE} Способность: {IN_DEVELOPING}')
        sleep(0.4)
        print()

    def get_damage(self, enemy_damage: int) -> NoReturn:
        """Reduce the character's hp by the amount of damage received.
        :param enemy_damage: The amount of damage the enemy is attacking the character with."""
        self.hp -= enemy_damage
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def get_defense(self, got_defense) -> NoReturn:
        """Increase the character's defense randomly."""
        self.defense += got_defense

    def get_hp(self, got_hp) -> NoReturn:
        self.hp += got_hp

    def get_attack(self, got_attack) -> NoReturn:
        self.attack += got_attack

    def get_mp(self, got_mp) -> NoReturn:
        self.mp += got_mp

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

    def show_hp(self) -> int:
        """Returns character's hp"""
        return self.hp

    def show_attack(self) -> int:
        """Returns character's defense"""
        return self.attack

    def show_defense(self) -> int:
        """Returns character's defense"""
        return self.defense

    def show_inventory(self) -> int:
        """Returns character's defense"""
        return self.inventory

    def show_mp(self) -> int:
        """Returns character's defense"""
        return self.mp

    def show_ultimate(self) -> int:
        """Returns character's defense"""
        return self.ultimate

    def show_money(self) -> int:
        return self.money

    def show_lvl(self) -> int:
        return self.lvl

    def show_xp(self) -> int:
        return self.xp

    def show_battle_class(self):
        return self.battle_class


