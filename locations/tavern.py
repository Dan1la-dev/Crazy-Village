from random import randint
from misc.consts import *
from time import sleep

FOOD_OPTIONS = {
    '1': {'name': 'Мясное рагу', PRICE_KEY: 10, HEALTH_KEY: 5},
    '2': {'name': 'Кружка кваса', PRICE_KEY: 2, HEALTH_KEY: 2},
}

SPECIALS_VALUES = {
    '0': {FREE_COUNT_FOOD: 1},
    '1': {HAVE_FREE_FOOD: False},
}


def tavern(character: callable):
    """One of three locations
    :param character: It used to transmit character's params"""

    if character.money < 0 and SPECIALS_VALUES['0'][FREE_COUNT_FOOD] == 1:
        SPECIALS_VALUES['1'][HAVE_FREE_FOOD] = True
        print(f'{HEADER} Обобранный и побитый вы приходите в таверну...:')
        sleep(0.3)
        print(f'{HEADER} Хозяин таверны, увидев вас в таком лице, решил бесплатно вас накормить')
        FOOD_OPTIONS['1'][PRICE_KEY] = 0
        FOOD_OPTIONS['2'][PRICE_KEY] = 0
        SPECIALS_VALUES['0'][FREE_COUNT_FOOD] -= 1

    input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
    print(CLEAR_SCREEN)
    print(f'{HEADER} Вы входите в большой дом, около барной стойки стоит хозяин таверны, он предлагает вам обед:')

    for key, option in FOOD_OPTIONS.items():
        print(f"{key}️⃣ [{option['name']}] ➤ {option[PRICE_KEY]} 🪙 ➕ {option[HEALTH_KEY]} единиц ❤️")
    print()

    meal = input(PROMPT)
    print()

    try:
        # Attempt to look up the selected option by key
        selected_option = FOOD_OPTIONS[meal]
    except KeyError:
        # If the key isn't found, print an error message and return
        print(f'{HEADER} За вашу неотесанную грубость хозяин таверны вас прогнал.')
        print(f'{HEADER} Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой')
        FOOD_OPTIONS['1'][PRICE_KEY] += randint(2, 8)
        FOOD_OPTIONS['2'][PRICE_KEY] += randint(4, 10)

        return

    if character.money < selected_option[PRICE_KEY] and not SPECIALS_VALUES['1'][HAVE_FREE_FOOD]:
        # If the player doesn't have enough money, print an error message
        print(f'{HEADER} Вы нищий, так как вы нищий...')

    else:
        # Subtract the price of the selected option from the player's money and add its health benefit to their health
        character.money -= selected_option[PRICE_KEY]
        character.hp += selected_option[HEALTH_KEY]
        SPECIALS_VALUES['1'][HAVE_FREE_FOOD] = False

        print(f'{ATTENTION} Вы потратили {selected_option[PRICE_KEY]} 🪙 и получили {selected_option[HEALTH_KEY]} единиц ❤️')
        print(f'{ATTENTION} Ваше ❤️ теперь: {character.hp} единиц')
