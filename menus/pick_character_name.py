from misc.consts import ALPHABET_RU, ALPHABET_EN, DIGITS, SPECIAL_SYMBOLS
from misc.consts import CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, YES, NO, PRESS_ENTER


def pick_character_name():
    """Sets character's name"""
    length = None
    length_limit = 3
    allowed_chars = None
    digits = None

    while True:
        print(CLEAR_SCREEN)
        print(f"{HEADER} Введите ваше имя")
        print()
        character_name = input(PROMPT)
        character_name_set = set(character_name.lower())

        # It checks if character_name_set has more than 5 symbols
        if len(character_name) > length_limit:
            length = True
        # It checks if character_name_set contains only allowed characters
        if character_name_set <= (ALPHABET_RU | ALPHABET_EN | DIGITS | SPECIAL_SYMBOLS):
            allowed_chars = True

        # It checks if character_name_set contains not only digits
        if not character_name.isdigit():
            digits = True

        # It checks if all checks are succesfull
        if length and allowed_chars and digits:
            return character_name

        else:
            print()
            print(f'{ATTENTION} Неверный ввод имени. Ваше имя должно удовлетворять условиям: ')
            print()
            print(f'{YES if length else NO} Больше {length_limit} символов ')
            print(f'{YES if allowed_chars else NO} Не содержать запрещенные символы или пробелы')
            print(f'{YES if digits else NO} Не содержать только цифры ')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')

