from menus.pick_character import pick_character
from menus.pick_location import pick_location
from menus.pick_enemy import pick_enemy
from typing import NoReturn


class CrazyVillage:
    def __init__(self):
        """ The main app class """
        self.character = None
        self.enemy = None
        self.run_game = True

    def run(self) -> NoReturn:
        """ Runs the entire game """
        while self.run_game:
            self._show_menu()
            self.character.get_stats()
            self._choose_location()

    def _show_menu(self) -> NoReturn:
        """ Displays the game menu """
        while True:
            print('Crazy Village\n'
                  '[1] Играть\n'
                  '[2] Выход')
            action = input('>>> ')
            if action == '1':
                self._set_character()
                return
            elif action == '2':
                self.run_game = False
                return
            else:
                print('Invalid input. Please choose a valid option.')

    def _set_character(self) -> NoReturn:
        """Sets class object character"""
        self.character = pick_character()
        return self.character

    def _set_enemy(self) -> NoReturn:
        """Sets class object enemy"""
        self.enemy = pick_enemy()
        return self.enemy

    def _choose_location(self) -> NoReturn:
        """Chooses player's location"""
        pick_location(self.character)
