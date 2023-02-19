from menus.pick_character import pick_character
from menus.pick_location import pick_location


class CrazyVillage:
    """ The main app class """
    character = None
    location = None

    def run(self):
        """ Runs the entire game """
        self.__show_menu()

    def __show_menu(self):
        """ Displays the game menu """
        while True:
            print('Crazy Village\n'
                  '[1] Играть\n'
                  '[2] Выход')
            action = input('>>> ')
            if action == '1':
                self.__set_character()
            if action == '2':
                return

    def __set_character(self):
        self.character = pick_character()

    def __choose_location(self):
        self.location = pick_location(self.character)
