from misc.consts import ATTENTION, PROMPT


def death_screen(character_alive: bool):
    if not character_alive:
        # ask user if they want to continue or not
        print()
        print(f'{ATTENTION} Вы погибли... Играем еще?')
        print('1️⃣ Да ')
        print('2️⃣ Нет ')
        print()
        continued = input(PROMPT)
        if continued == '1':
            return True
        elif continued == '2':
            return False
        else:
            # handle invalid input
            print("Shapilov 🦌🦌🦌")
            return False
