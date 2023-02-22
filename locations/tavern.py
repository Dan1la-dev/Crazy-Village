from random import randint

PRICE_KEY = 'price'
HEALTH_KEY = 'health'


FOOD_OPTIONS = {
    '1️⃣': {PRICE_KEY: 10, HEALTH_KEY: 5},  # Meat stew
    '2️⃣': {PRICE_KEY: 2, HEALTH_KEY: 2},   # Kvass mug
}


def tavern(character: callable):
    print(f'ЛЕВИЙ ➤ Вы входите в большой дом, около барной стойки стоит хозяин таверны, который предлагает вам обед:')

    for key, option in FOOD_OPTIONS.items():
        print(f'{key}️⃣ [{option["name"]}] ➤ {option["price"]} 🪙 ➕ {option["health"]} единиц ❤️')

    meal = input('🡆 ')
    selected_option = FOOD_OPTIONS[meal]

    if meal in FOOD_OPTIONS.keys():
        if character.money < selected_option[PRICE_KEY]:
            print('ЛЕВИЙ ➤ Вы нищий, так как вы нищий...')
        else:
            character.spend_money(selected_option[PRICE_KEY])
            character.hp += selected_option[HEALTH_KEY]
            print(f'[❗] Вы потратили {selected_option[PRICE_KEY]} 🪙 и получили {selected_option[HEALTH_KEY]} единиц ❤️')
    else:
        print(f'ЛЕВИЙ ➤ За вашу неотесанную грубость хозяин таверны вас прогнал.')
        print(f'ЛЕВИЙ ➤ Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой')
        selected_option[PRICE_KEY] += randint(2, 8)
        selected_option[PRICE_KEY] += randint(4, 10)
