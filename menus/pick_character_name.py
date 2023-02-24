from misc.consts import ALPHABET_RU, ALPHABET_EN, DIGITS, CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, YES, NO, PRESS_ENTER


def pick_character_name():
    """Sets character's name"""
    lenght = None
    first_symbol = None
    allowed_chars = None
    digits = None

    while True:
        print(CLEAR_SCREEN)
        print(f"{HEADER} Введите ваше имя")
        print()
        character_name = input(PROMPT)
        character_name_set = set(character_name.lower())

        # It checks if character_name_set has more than 5 symbols
        if len(character_name) > 5:
            lenght = True
        # It Checks if character_name_set the first symbol is letter
        if character_name[0].isalpha():
            first_symbol = True
        # It checks if character_name_set contains only allowed characters
        if character_name_set <= (ALPHABET_RU | ALPHABET_EN | DIGITS) and ' ' not in character_name:
            allowed_chars = True

        # It checks if character_name_set contains not only digits
        if not character_name.isdigit():
            digits = True

        # It checks if all checks are succesfull
        if lenght and first_symbol and allowed_chars and digits:
            return character_name

        else:
            print()
            print(f'{ATTENTION} Неверный ввод имени. Ваше имя должно удовлетворять условиям: ')
            print()
            print(f'{YES if lenght else NO} Больше 5 символов ')
            print(f'{YES if first_symbol else NO} Первый символ - буква ')
            print(f'{YES if allowed_chars else NO} Не содержать спец символы и пробелы')
            print(f'{YES if digits else NO} Не содержать только цифры ')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')

