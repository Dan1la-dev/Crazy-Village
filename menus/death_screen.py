from misc.consts import ATTENTION, PROMPT, NUMERATION, SHAPILOV


def death_screen(character_alive: bool):
    if not character_alive:
        # ask user if they want to continue or not
        print()
        print(f'{ATTENTION} Вы погибли... Играем еще?')
        print(f'{NUMERATION[1]} Да ')
        print(f'{NUMERATION[2]} Нет ')
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
