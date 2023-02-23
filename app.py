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
            self._choose_location()
            if not self.character.alive:
                print()
                print("[❗] Вы погибли... Играем еще?")
                print("1️⃣ Да ")
                print("2️⃣ Нет ")
                print()
                continued = input('>>> ')
                if continued == '1':
                    continue
                elif continued == '2':
                    self.run_game = False
                    return
                else:
                    print("Shapilov 🦌🦌🦌")
                    self.run_game = False
                    return

    def _show_menu(self) -> NoReturn:
        """ Displays the game menu """
        while True:
            print("\n" * 99999)
            print()
            print('👨‍💻 ЛЕВИЙ ➤ Добро пожаловать в игру "Безумный посёлок"')
            print()
            print('1️⃣ Играть')
            print('2️⃣ Выход')
            print('3️⃣ Информация о игре')
            print()
            action = input('>>> ')
            if action == '1':
                print("\n" * 99999)
                print()
                self._set_character()
                return
            elif action == '2':
                self.run_game = False
                return
            elif action == '3':
                print('🔥🔥 Создатель/разработчик №1🔥🔥: Матвей Пашинин')
                print('💎💎 Разработчик №2 💎💎: Шапилов Николай')
                print('🦸🦸 Разработчик №3 🦸🦸: Даниил Лавриненко')
            else:
                print('[❗] Неверное значение. Повторите попытку...')
            print()
            input('🧿 Нажмите Enter для продолжения...')

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
