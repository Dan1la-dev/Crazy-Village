from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest
from menus.pick_enemy import pick_enemy
from misc.consts import *
from time import sleep


def pick_location(character: callable, battle_system: callable):
    """Sets player's location and allows them to choose where to go
    :param battle_system: A function that is used to transmit battle class methods
    :param character: A function that is used to transmit character's parameters"""

    while character.alive:
        print()
        input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
        print(CLEAR_SCREEN)

        # Display options for the player to choose from
        print(f'{HEADER} Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        sleep(0.4)
        print()
        print(f'{TEMP_NUMERATION[1]} Таверна {TAVERN}')
        sleep(0.4)
        print(f'{TEMP_NUMERATION[2]} Полигон {POLYGON}')
        sleep(0.4)
        print(f'{TEMP_NUMERATION[3]} Лес {FOREST}')
        sleep(0.4)
        print(f'{TEMP_NUMERATION[4]} Статистика {STATS}')
        sleep(0.4)
        print()

        # Get the player's input
        location = input(PROMPT)

        # Call the appropriate function based on the player's input
        if location == '1':
            tavern(character)
        elif location == '2':
            # Check if the player has a debt
            if character.money < 0:
                print(f'{HEADER} Охрана полигона не пускает вас из-за вашего долга в {-character.show_money()} {MONEY}')
                sleep(1)
                print(f'{HEADER} Сказали, что, пустят, когда вы уплатите должок...\n')
            else:
                polygon(character)
        elif location == '3':
            forest(character, pick_enemy(), battle_system)
        elif location == '4':
            character.get_stats()
        else:
            print(f'{GAME_ATTENTION} Неверный ввод. Повторите попытку...')