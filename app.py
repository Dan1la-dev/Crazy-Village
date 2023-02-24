from menus.pick_character import pick_character
from menus.pick_location import pick_location
from menus.pick_enemy import pick_enemy
from menus.pick_battle_system import pick_battle_system
from menus.death_screen import death_screen
from menus.devs_info import devs_info

from typing import NoReturn

from misc.consts import *


class CrazyVillage:
    def __init__(self):
        """Initialize the main app class"""
        self.character = None
        self.enemy = None
        self.battle_system = None
        self.run_game = True

    def run(self) -> NoReturn:
        """Runs the entire game"""
        while self.run_game:
            self._show_menu()
            self._choose_location()
            self.run_game = death_screen(self.character.alive)

    def _show_menu(self) -> NoReturn:
        """Displays the game menu"""
        while True:
            print(CLEAR_SCREEN)
            print()
            print(f'{HEADER} Добро пожаловать в игру "Безумный посёлок')
            print()
            print(f'{NUMERATION[1]} Играть')
            print(f'{NUMERATION[2]} Выход')
            print(f'{NUMERATION[3]} Информация о игре')
            print()
            action = input('>>> ')
            if action == '1':
                print(CLEAR_SCREEN)
                print()
                self._set_battle_system()
                self._set_character()
                return
            elif action == '2':
                self.run_game = False
                return
            elif action == '3':
                # display information about the game and its developers
                devs_info()
            else:
                # handle invalid input
                print(f'{ATTENTION} Неверное значение. Повторите попытку...')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')

    def _set_character(self) -> NoReturn:
        """Sets class object character"""
        self.character = pick_character()

    def _set_enemy(self) -> NoReturn:
        """Sets class object enemy"""
        self.enemy = pick_enemy()

    def _set_battle_system(self) -> NoReturn:
        """Sets class object battle"""
        self.battle_system = pick_battle_system()

    def _choose_location(self) -> NoReturn:
        """Chooses player's location"""
        pick_location(self.character, self.battle_system)
