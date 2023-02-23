from random import randint

PRICE_KEY = 'price'
HEALTH_KEY = 'health'


FOOD_OPTIONS = {
    '1': {'name': 'Мясное рагу', PRICE_KEY: 10, HEALTH_KEY: 5},
    '2': {'name': 'Кружка кваса', PRICE_KEY: 2, HEALTH_KEY: 2},
}


def tavern(character: callable):
    input('🧿 Нажмите Enter для продолжения...')
    print("\n" * 99999)
    print(f'👨‍💻 ЛЕВИЙ ➤ Вы входите в большой дом, около барной стойки стоит хозяин таверны, который предлагает вам обед:')

    for key, option in FOOD_OPTIONS.items():
        print(f'{key}️⃣ [{option["name"]}] ➤ {option[PRICE_KEY]} 🪙 ➕ {option[HEALTH_KEY]} единиц ❤️')
    print()

    meal = input('>>> ')
    print()

    try:
        # Attempt to look up the selected option by key
        selected_option = FOOD_OPTIONS[meal]
    except KeyError:
        # If the key isn't found, print an error message and return
        print('👨‍💻 ЛЕВИЙ ➤ За вашу неотесанную грубость хозяин таверны вас прогнал.')
        print('👨‍💻 ЛЕВИЙ ➤ Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой')
        FOOD_OPTIONS['1'][PRICE_KEY] += randint(2, 8)
        FOOD_OPTIONS['2'][PRICE_KEY] += randint(4, 10)

        return

    if character.money < selected_option['price']:
        # If the player doesn't have enough money, print an error message
        print('👨‍💻 ЛЕВИЙ ➤ Вы нищий, так как вы нищий...')

    else:
        # Subtract the price of the selected option from the player's money and add its health benefit to their health
        character.money -= selected_option[PRICE_KEY]
        character.hp += selected_option[HEALTH_KEY]

        print(f'[❗] Вы потратили {selected_option[PRICE_KEY]} 🪙 и получили {selected_option[HEALTH_KEY]} единиц ❤️')
        print(f'[❗] Ваше ❤️ теперь: {character.hp} единиц')