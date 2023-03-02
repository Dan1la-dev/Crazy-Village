from misc.consts import DIGITS, VALID_SYMBOLS
from misc.consts import CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, NO, PRESS_ENTER
from time import sleep


def pick_character_name():
    """Sets character's name"""
    length_limit = 2

    while True:
        print(CLEAR_SCREEN)
        print(f"{HEADER} Введите ваше имя:")
        print()
        character_name = input(PROMPT)
        character_name_set = set(character_name.lower())

        # A list of conditions that the character's name must meet
        # Each condition is a tuple, where the first element is a boolean expression
        # that evaluates to True if the condition is met, and the second element is
        # a string that describes the condition in case it is not met
        conditions = [
            (len(character_name) >= length_limit, f'Больше или равно {length_limit} символам'),
            (character_name.isalnum() or character_name_set <= VALID_SYMBOLS, 'Не содержать спецсимволы или пробелы'),
            (not character_name_set <= DIGITS, 'Не содержать только цифры')
        ]

        # Check if all conditions are met
        if all(condition[0] for condition in conditions):
            return character_name
        else:
            print(f'{ATTENTION} Неверный ввод имени. Ваше имя должно удовлетворять условиям:')
            print()
            # It prints unperforme conditions
            for condition in conditions:
                if not condition[0]:
                    sleep(0.2)
                    print(f'{NO} {condition[1]}')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')