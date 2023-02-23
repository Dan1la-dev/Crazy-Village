from time import sleep
from random import choice
from misc.consts import *


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
        print(f'[🧑 🥋] Ваш персонаж: {character.battle_class}\t[👺 🥋] Тип врага: {enemy.type}')
        print(f'[🧑 ❤️] Ваше здоровье: {character.hp}  \t[👺 ❤️] Здоровье врага: {enemy.hp} ')
        print(f'[🧑 🗡️] Ваша атака: {character.attack}     \t[👺 🗡️] Атака врага: {enemy.attack} ')
        print(f'[🧑 🛡️] Ваша защита: {character.defense}     \t[👺 🛡️] Защита врага: {enemy.defense}')
        print()

    @staticmethod
    def pause_clear():
        # Pause the game for 5 seconds and clear the console screen
        sleep(5)
        print(CLEAR_SCREEN)

    def character_perform(self, character: callable, enemy: callable):
        # Prompt the user for their move and print the available moves
        print("[🧑] Ваш ход: ")
        print()

        for move in self.character_battle_moves:
            print(f'{move}️⃣  {self.character_battle_moves[move]}')
        print()

        character_move = input(PROMPT)
        print()

        # Check the character's move and perform the corresponding action
        if character_move == '1':
            enemy.take_damage(character.attack)
            print(f'[🧑] Вы уменьшили 👺 ❤️ с {enemy.hp} {PROMPT} {enemy.take_damage(character.attack)}')

            print(f'[👺 ❤️ ❗] Здоровье врага: {enemy.hp}')
            print()
        elif character_move == '2':
            print(f"[🧑🛡️🛡️] Вы повысили свою 🛡️🛡️🛡️ c {character.defense} {PROMPT} {character.get_defense()}")

            print(f'[🧑🛡️❗] Ваша защита: {character.defense}')
            print()

    def enemy_perform(self, character: callable, enemy: callable):
        # Randomly choose the enemy's move and print it
        print('[👺] Ход врага: \n')
        sleep(0.3)

        enemy_move = choice(list(self.enemy_battle_moves.keys()))

        # Check the enemy's move and perform the corresponding action
        if enemy_move == '1':
            print(f'[👺] Враг уменьшил ваше ❤️❤️❤️ с {character.hp} {PROMPT} {character.take_damage(enemy.attack)}')
            print(f'[🧑❤️❗] Ваше здоровье: {character.hp}')
        elif enemy_move == '2':
            print(f'[👺] Враг повысил свою 🛡️🛡️🛡️ с {enemy.defense} {PROMPT} {enemy.get_defense()}')
            print(f'[👺🛡️❗] Защита врага: {enemy.defense}')



