from classes.character import Character
from entities.characters import *


class CrazyVillage:
    """ The main app class """
    character = None

    def run(self):
        """ Runs the entire game """
        self._show_menu()

    def _show_menu(self):
        """ Displays the game menu """
        while True:
            print('Crazy Village\n'
                  '[1] Играть\n'
                  '[2] Выход')
            action = input('>>> ')
            if action == '1':
                self._set_character()
            if action == '2':
                return

    def _set_character(self):
        """ Sets player's character """
        print("👨‍💻 ЛЕВИЙ ➤ Введите ваше имя\n")
        name = input('>>> ')
        while True:
            print('Выберите класс:')
            print('1️⃣ Воин 🗡️ - мастер ближнего боя, выносит большое количество урона.')
            print('2️⃣ Лучник 🏹 - мастер дальнего боя, наносит большой урон на расстоянии.')
            print('3️⃣ Маг 🪄 - мастер магии, наносит огромный стихийный урон')
            battle_class = input('>>> ')
            if battle_class == '1':
                self.character = Character(WARRIOR)
                break
            if battle_class == '2':
                self.character = Character(ARCHER)
                break
            if battle_class == '3':
                self.character = Character(WIZARD)
                break
