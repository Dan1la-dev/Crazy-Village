from random import randint
from misc.consts import *
from time import sleep

FOOD_OPTIONS = {
    '1': {NAME: 'Мясное рагу', PRICE_KEY: 10, HEALTH_KEY: 5},
    '2': {NAME: 'Кружка кваса', PRICE_KEY: 2, HEALTH_KEY: 2},
}

SPECIAL_VALUES = {
    '0': {FREE_COUNT_FOOD: 1},
    '1': {HAVE_FREE_FOOD: False},
}


def tavern(character: callable):
    """One of three locations
    :param character: It used to transmit character's params"""
    while True:
        if character.money < 0 and SPECIAL_VALUES.get('0', {}).get(FREE_COUNT_FOOD, 0) >= 1:
            SPECIAL_VALUES['1'][HAVE_FREE_FOOD] = True
            print(f'{HEADER} Обобранный и побитый вы приходите в таверну...:')
            sleep(3)
            print(f'{HEADER} Хозяин таверны, увидев вас в таком лице, решил бесплатно вас накормить')
            sleep(3)
            FOOD_OPTIONS['1'][PRICE_KEY] = 0
            FOOD_OPTIONS['2'][PRICE_KEY] = 0
            SPECIAL_VALUES['0'][FREE_COUNT_FOOD] -= 1

        input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
        print(CLEAR_SCREEN)
        print(f'{HEADER} Вы входите в большой дом, около барной стойки стоит хозяин таверны, он предлагает вам обед:')
        sleep(3)
        print()

        print(f'{TEMP_NUMERATION[0]} Выход из локации')
        sleep(0.35)
        for key, option in FOOD_OPTIONS.items():
            print(f"{TEMP_NUMERATION[int(key)]}️ [{option.get(NAME)}] ➤ "
                  f"{option.get(PRICE_KEY)} 🪙 "
                  f"➕ {option.get(HEALTH_KEY)} ❤️")
            sleep(0.35)
        print()

        meal = input(PROMPT)
        print()

        if meal == '0':
            return

        # Look up the selected option using get() to avoid KeyError if the key is not present
        selected_option = FOOD_OPTIONS.get(meal, '')

        # Get the price of the selected option, defaulting to 0 if the PRICE_KEY is not found
        price = selected_option.get(PRICE_KEY, 0)

        # Get whether or not the player has free food, defaulting to False if '1' or HAVE_FREE_FOOD is not found
        has_free_food = SPECIAL_VALUES.get('1', {}).get(HAVE_FREE_FOOD, False)

        if not selected_option:
            # If the key isn't found, print an error message and return
            print(f'{HEADER} За вашу неотесанную грубость хозяин таверны вас прогнал.')
            sleep(3)
            print(f'{HEADER} Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой')
            sleep(3)

            FOOD_OPTIONS['1'][PRICE_KEY] += randint(2, 8)
            FOOD_OPTIONS['2'][PRICE_KEY] += randint(4, 10)
            return

        elif character.money < price and not has_free_food:
            # If the player doesn't have enough money and doesn't have free food, print a message
            sleep(3)
            print(f'{HEADER} Вы нищий, так как вы нищий...')

        else:
            # Subtract the price from the player's money and add its health benefit to their health
            spent_money = selected_option.get(PRICE_KEY, 0)
            got_hp = selected_option.get(HEALTH_KEY, 0)

            character.spend_money(selected_option.get(PRICE_KEY, 0))
            character.get_hp(selected_option.get(HEALTH_KEY, 0))

            SPECIAL_VALUES['1'][HAVE_FREE_FOOD] = False

            print(f'{GAME_ATTENTION} Вы потратили {spent_money} {MONEY} ')
            sleep(3)
            print(f'{GAME_ATTENTION} Вы получили {got_hp} ед {HEART}')
            sleep(3)
            print(f'{GAME_ATTENTION} Ваше {HEART} теперь: {character.show_hp()} ед')
            sleep(3)
            FOOD_OPTIONS['1'][PRICE_KEY] = 10
            FOOD_OPTIONS['2'][PRICE_KEY] = 5

        print()
        print(f'{HEADER} Хотите продолжить трапезу?')
        print()
        print(f'{TEMP_NUMERATION[1]} Да')
        print(f'{TEMP_NUMERATION[2]} Нет')
        print()

        continued = input(f'{PROMPT}')

        if continued == '1':
            pass
        elif continued == '2':
            return
        else:
            print(f"Shapilov {SHAPILOV * 3}")
            return
