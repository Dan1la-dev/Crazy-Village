from time import sleep
from random import choice
from misc.consts import *
from typing import NoReturn


class Battle:
    def __init__(self):
        # Define the available moves for the character and the enemy
        self.character_battle_moves = {
            '1': 'Атаковать',
            '2': 'Защититься'
        }
        self.enemy_battle_moves = {
            '1': 'Атаковать',
            '2': 'Защититься'
        }

    @staticmethod
    def battle_info(character: callable, enemy: callable):
        """Func to inform player's params during battle
        :param character: It used to transmit character's params
        :param enemy: It used to transmit enemy's params"""
        # Print the battle information for the character and enemy
        print()
        print(f'{CHARACTER_TYPE} Персонаж: {character.battle_class}')
        print(f'{CHARACTER_HEART} Здоровье: {character.hp}')
        print(f'{CHARACTER_ATTACK} Атака: {character.attack}')
        print(f'{CHARACTER_DEFENSE} Защита: {character.defense}')
        print()
        print(f'{ENEMY_TYPE} Тип: {enemy.type}')
        print(f'{ENEMY_HEART} Здоровье: {enemy.hp}')
        print(f'{ENEMY_ATTACK} Атака: {enemy.attack}')
        print(f'{ENEMY_DEFENSE} Защита: {enemy.defense}')
        print()

    @staticmethod
    def pause_clear():
        # Pause the game for 5 seconds and clear the console screen
        sleep(5)
        print(CLEAR_SCREEN)

    def character_perform(self, character: callable, enemy: callable) -> NoReturn:
        # Prompt the user for their move and print the available moves
        print(f"[{CHARACTER}] Ваш ход: ")
        print()

        for move in self.character_battle_moves:
            print(f'{move}️⃣  {self.character_battle_moves[move]}')
        print()

        character_move = input(PROMPT)
        print()

        # Check the character's move and perform the corresponding action
        if character_move == '1':
            enemy.take_damage(character.attack)
            print(f'{CHARACTER_ATTACK} Вы нанесли {enemy.take_damage(character.attack)} {HEART} врагу.')
            print(f'{ENEMY_HEART_ATTENTION} Здоровье врага: {enemy.show_hp()}')
            print()
        elif character_move == '2':
            print(f"{CHARACTER_DEFENSE} Вы укрепились на {character.get_defense()} {DEFENSE}")

            print(f'{CHARACTER_DEFENSE_ATTENTION} Ваша защита: {character.show_defense()}')
            print()

    def enemy_perform(self, character: callable, enemy: callable) -> NoReturn:
        # Randomly choose the enemy's move and print it
        print(f'[{ENEMY}] Ход врага: \n')
        sleep(0.3)

        enemy_move = choice(list(self.enemy_battle_moves.keys()))

        # Check the enemy's move and perform the corresponding action
        if enemy_move == '1':
            print(f'{ENEMY_ATTACK} Враг нанес вам: {character.take_damage(enemy.attack)} {HEART}')
            print(f'{CHARACTER_HEART_ATTENTION} Ваше здоровье: {character.show_hp()}')
        elif enemy_move == '2':
            print(f'{ENEMY_DEFENSE} Враг укрепился на: {enemy.get_defense()} {DEFENSE}')
            print(f'{ENEMY_DEFENSE_ATTENTION} Защита врага: {enemy.show_defense()}')



