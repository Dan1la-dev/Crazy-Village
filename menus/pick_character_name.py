from misc.consts import ALPHABET_RU, ALPHABET_EN, DIGITS, SPECIAL_SYMBOLS
from misc.consts import CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, NO, PRESS_ENTER


def pick_character_name():
    """Sets character's name"""
    length_limit = 2

    while True:
        print(CLEAR_SCREEN)
        print(f"{HEADER} Введите ваше имя:")
        print()
        character_name = input(PROMPT).strip()
        character_name_set = set(character_name.lower())

        # A list with conditions that are in the tuples
        conditions = [
            (len(character_name) >= length_limit, f'Больше или равно {length_limit} символам'),
            (character_name_set <= (ALPHABET_RU | ALPHABET_EN | DIGITS | SPECIAL_SYMBOLS),
             'Не содержать запрещенные символы'),
            (any(char.isalpha() for char in character_name), 'Не содержать только цифры')
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
                    print(f'{NO} {condition[1]}')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')

