from misc.consts import CLEAR_SCREEN, HEADER, NUMERATION, TEMP_NUMERATION
from time import sleep


def welcome():
    print(CLEAR_SCREEN)
    print()
    sleep(0.35)
    print(f'{HEADER} Добро пожаловать в игру "Безумный посёлок" 🎪')
    sleep(0.35)
    print()
    print(f'{TEMP_NUMERATION[1]} Играть 🥁')
    sleep(0.35)
    print(f'{TEMP_NUMERATION[2]} Выход 🗿')
    sleep(0.35)
    print(f'{TEMP_NUMERATION[3]} Информация о игре 🪪')
    print()
