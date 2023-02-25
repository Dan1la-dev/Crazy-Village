from time import sleep
from random import randint
from misc.consts import HEADER, CLEAR_SCREEN, PRESS_ENTER


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
    print(f'{HEADER} тут начинается ваш путь авантюриста...')
    sleep(0.5)

    # Introduce the enemy
    print()
    print(HEADER, f'О НЕТ, {character.name}, вас атаковал {enemy.type}!')

    # Start battle loop
    while True:
        # Display battle information and prompt character to perform an action
        battle_system.battle_info(character, enemy)
        battle_system.character_perform(character, enemy)

        # Check if the enemy is defeated
        if not enemy.alive:
            # Print victory message and reward the character
            print(f'{HEADER} Вы победили!!! Вы - настоящий боец')
            earned_money = randint(10, 100)
            character.earn_money(earned_money)
            earned_xp = randint(13, 50)
            character.earn_xp(earned_xp)
            print()
            print(f'💎 НАГРАДЫ 💎  ')
            print()
            print(f'➡️ {earned_money} 🪙')
            print(f'➡️ {earned_xp} ✨')
            return

        # Clear the screen and pause before the enemy's turn
        battle_system.pause_clear()

        # Enemy performs its action
        battle_system.enemy_perform(character, enemy)
        battle_system.pause_clear()

        # Check if the character is defeated
        if not character.alive:
            return
