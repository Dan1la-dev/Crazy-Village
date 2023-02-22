from menus.pick_character import pick_character
from menus.pick_location import pick_location
from menus.pick_enemy import pick_enemy


class CrazyVillage:
    """ The main app class """
    character = None
    enemy = None
    run_game = True

    def run(self):
        """ Runs the entire game """
        while self.run_game:
            self.__show_menu()
            self.character.get_stats()
            self.__choose_location()

    def __show_menu(self):
        """ Displays the game menu """
        while True:
            print('Crazy Village\n'
                  '[1] Играть\n'
                  '[2] Выход')
            action = input('>>> ')
            if action == '1':
                self.__set_character()
                return
            if action == '2':
                self.run_game = False
                return

    def __set_character(self):
        """Sets class object character"""
        self.character = pick_character()

    def __set_enemy(self):
        """Sets class object enemy"""
        self.enemy = pick_enemy()

    def __choose_location(self):
        """Chooses player's location"""
        pick_location(self.character)
