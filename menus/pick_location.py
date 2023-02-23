from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest
from menus.pick_enemy import pick_enemy
from misc.consts import PRESS_ENTER, CLEAR_SCREEN, HEADER, PROMPT, ATTENTION


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
        print()
        print('1️⃣ Таверна 🏠')
        print('2️⃣ Полигон 💪')
        print('3️⃣ Лес 🌲')
        print('4️⃣ Статистика 🔆')
        print()

        # Get the player's input
        location = input(PROMPT)

        # Call the appropriate function based on the player's input
        if location == '1':
            tavern(character)
        elif location == '2':
            # Check if the player has a debt
            if character.debt:
                print(f'{HEADER} Охрана полигона не пускает вас из за вашего долга в размере {character.money} 🪙')
                print(f'{HEADER} Сказали, что, пустят, когда вы уплатите должок...\n')
            else:
                polygon(character)
        elif location == '3':
            forest(character, pick_enemy(), battle_system)
        elif location == '4':
            character.get_stats()
        else:
            print(f'{ATTENTION} Неверный ввод. Повторите попытку...')