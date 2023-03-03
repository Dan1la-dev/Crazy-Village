from time import sleep
from random import choice
from misc.consts import *
from typing import NoReturn
from math import floor
from random import randint


class Battle:
    def __init__(self):
        # Define the available moves for the character and the enemy
        self.character_battle_moves = {
            '1': 'Атаковать',
            '2': 'Защититься',
            '3': 'Пропустить ход'
        }
        self.enemy_battle_moves = {
            '1': 'Атаковать',
            '2': 'Защититься'
        }

    @staticmethod
    def calculate_enemy_damage(enemy_attack: callable, character_defense: callable) -> int:
        """Func to calculate enemy damage to character with his defense
        :param enemy_attack: It used to divide character's percentages
        :param character_defense: It used to decrease damage to character"""
        move_damage = floor(enemy_attack / (character_defense / 100 + 1))
        return move_damage

    @staticmethod
    def calculate_character_damage(character_attack: callable, enemy_defense: callable) -> int:
        """Func to calculate enemy damage to character with his defense
        :param character_attack: It used to divide enemy's percentages
        :param enemy_defense: It used to decrease damage to enemy"""
        move_damage = floor(character_attack / (enemy_defense / 100 + 1))
        return move_damage

    @staticmethod
    def calculate_enemy_defense() -> int:
        """Func to calculate enemy damage to character with his defense"""
        move_defense = randint(5, 9)
        return move_defense

    @staticmethod
    def calculate_character_defense() -> int:
        """Func to calculate random defense"""
        move_defense = randint(9, 20)
        return move_defense

    @staticmethod
    def battle_info(character: callable, enemy: callable):
        """Func to inform player's and params of an enemy during battle
        :param character: It used to transmit character's params
        :param enemy: It used to transmit enemy's params"""
        print()
        print(f'{CHARACTER_TYPE} Персонаж: {character.show_battle_class()}')
        print(f'{CHARACTER_HEART} Здоровье: {character.show_hp()}')
        print(f'{CHARACTER_ATTACK} Атака: {character.show_attack()}')
        print(f'{CHARACTER_DEFENSE} Защита: {character.show_defense()}')
        print()
        print(f'{ENEMY_TYPE} Тип: {enemy.show_type()}')
        print(f'{ENEMY_HEART} Здоровье: {enemy.show_hp()}')
        print(f'{ENEMY_ATTACK} Атака: {enemy.show_attack()}')
        print(f'{ENEMY_DEFENSE} Защита: {enemy.show_defense()}')
        print()

    @staticmethod
    def pause(seconds: int) -> NoReturn:
        # Pause the game for 2 seconds and clear the console screen
        for i in range(seconds, 0, -1):
            print(f'\r{NOT_PRESS_ENTER} Идет анимация, не нажимайте Enter...', end='')
            sleep(1)
        return

    def character_perform(self, character: callable, enemy: callable) -> NoReturn:
        # Prompt the user for their move and print the available moves
        print(f"[{CHARACTER}] Ваш ход: ")
        print()

        for move in self.character_battle_moves:
            print(f'{TEMP_NUMERATION[int(move)]} {self.character_battle_moves[move]}')
        print()

        character_move = input(PROMPT)

        # Check the character's move and perform the corresponding action
        if self.character_battle_moves.get(character_move, '') == 'Атаковать':
            print(CLEAR_SCREEN)
            got_move_damage = self.calculate_character_damage(character.attack, enemy.defense)
            enemy.get_damage(got_move_damage)

            print(f'{CHARACTER_ATTACK} Вы нанесли {got_move_damage} {HEART} врагу.')
            print(f'{ENEMY_HEART_ATTENTION} Здоровье врага: {enemy.show_hp()}')
        elif self.character_battle_moves.get(character_move, '') == 'Защититься':
            print(CLEAR_SCREEN)
            got_move_defense = self.calculate_character_defense()
            character.get_defense(got_move_defense)
            print(f"{CHARACTER_DEFENSE} Вы укрепились на {got_move_defense} {DEFENSE}")

            print(f'{CHARACTER_DEFENSE_ATTENTION} Ваша защита: {character.show_defense()}')
        elif self.character_battle_moves.get(character_move, '') == 'Пропустить ход':
            pass

    def enemy_perform(self, character: callable, enemy: callable) -> NoReturn:
        # Randomly choose the enemy's move and print it
        print(f'[{ENEMY}] Ход врага: \n')
        sleep(0.3)

        enemy_move = choice(list(self.enemy_battle_moves.keys()))

        # Check the enemy's move and perform the corresponding action
        if self.enemy_battle_moves.get(enemy_move, '') == 'Атаковать':
            print(CLEAR_SCREEN)
            got_move_damage = self.calculate_enemy_damage(enemy.attack, character.defense)
            character.get_damage(got_move_damage)

            print(f'{ENEMY_ATTACK} Враг нанес вам: {got_move_damage} {HEART}')
            print(f'{CHARACTER_HEART_ATTENTION} Ваше здоровье: {character.show_hp()}')

        elif self.enemy_battle_moves.get(enemy_move, '') == 'Защититься':
            print(CLEAR_SCREEN)
            got_move_defense = self.calculate_enemy_defense()
            enemy.get_defense(got_move_defense)

            print(f'{ENEMY_DEFENSE} Враг укрепился на: {got_move_defense} {DEFENSE}')
            print(f'{ENEMY_DEFENSE_ATTENTION} Защита врага: {enemy.show_defense()}')

