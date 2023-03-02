from time import sleep
from random import randint
from misc.consts import *
from menus.pick_enemy import pick_enemy


def forest(character: callable, enemy: callable, battle_system: callable):
    """One of three locations
    :param battle_system: It used to transmit battle class methods
    :param character: It used to transmit character's params
    :param enemy: It used to transmit enemy's params"""

    # Prompt user to continue and clear the screen
    input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
    print(CLEAR_SCREEN)

    # Print location description
    print(f'{HEADER} Вы стоите на опушке огромного леса, деревья шумят своими огромными кронами...')
    sleep(3)
    print(f'{HEADER} тут начинается ваш путь авантюриста...')
    sleep(3)

    # Introduce the enemy
    print()
    print(f'{HEADER} О НЕТ, {character.name}, вас атаковал {enemy.type}!')
    sleep(3)
    print(CLEAR_SCREEN)

    # Start battle loop
    while True:
        # Display battle information and prompt character to perform an action
        battle_system.battle_info(character, enemy)
        battle_system.character_perform(character, enemy)
        # Check if the enemy is defeated
        if not enemy.alive:
            # Print victory message and reward the character
            print()

            print(f'{HEADER} Вы победили!!! Вы - настоящий боец')
            sleep(3)
            earned_money = randint(10, 100)
            character.earn_money(earned_money)
            earned_xp = randint(13, 50)
            character.earn_xp(earned_xp)
            print()

            print(f'{DIAMOND} ВАШИ НАГРАДЫ {DIAMOND}  ')
            print()
            sleep(0.35)
            print(f'{PROMPT} {earned_money} {MONEY}')
            sleep(0.35)
            print(f'{PROMPT} {earned_xp} {XP}')
            print()

            print(f'{HEADER} Хотите продолжить гулять по лесу?')
            print()
            print(f'{TEMP_NUMERATION[1]} Да')
            print(f'{TEMP_NUMERATION[2]} Нет')
            print()

            continued = input(f'{PROMPT}')
            if continued == '1':
                forest(character, pick_enemy(), battle_system)
            elif continued == '2':
                return
            else:
                print(f"Shapilov {SHAPILOV * 3}")
                return

        # Clear the screen and pause before the enemy's turn
        battle_system.sleep_clear(2)

        # Enemy performs its action
        battle_system.enemy_perform(character, enemy)
        battle_system.sleep_clear(2)

        # Check if the character is defeated
        if not character.alive:
            return
