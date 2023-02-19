from menus.pick_character import pick_character


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
        print('Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        print('[1] Таверна')
        print('[2] Полигон')
        print('[3] Лес')
        location = input('➥ ')
        if location == '1':
            self.location = tavern.location_tavern()
        elif location == '2':
            self.location = polygon.location_polygon()
        else:
            self.location = forest.location_forest()
