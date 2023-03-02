from misc.consts import ATTENTION, PROMPT, NUMERATION, SHAPILOV
from time import sleep
from misc.consts import CLEAR_SCREEN, TEMP_NUMERATION


def death_screen(character_alive: bool):
    print(CLEAR_SCREEN)
    if not character_alive:
        # ask user if they want to continue or not
        print()
        print(f'{ATTENTION} Вы погибли... Играем еще?')
        sleep(1)
        print(f'{TEMP_NUMERATION[1]} Да ')
        print(f'{TEMP_NUMERATION[2]} Нет ')
        print()
        continued = input(PROMPT)
        if continued == '1':
            return True
        elif continued == '2':
            return False
        else:
            # handle invalid input
            print(f"Shapilov {SHAPILOV * 3}")
            return False
