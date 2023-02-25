from misc.consts import CLEAR_SCREEN, HEADER, NUMERATION


def welcome():
    print(CLEAR_SCREEN)
    print()
    print(f'{HEADER} Добро пожаловать в игру "Безумный посёлок" 🎪')
    print()
    print(f'{NUMERATION[1]} Играть 🥁')
    print(f'{NUMERATION[2]} Выход 🗿')
    print(f'{NUMERATION[3]} Информация о игре 🪪')
    print()
