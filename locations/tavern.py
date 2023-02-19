from random import randint

food_info = {
    '1': {'price': 10, 'health': 5},  # Meat stew
    '2': {'price': 2, 'health': 2},   # Kvass mug
}


def tavern(player):
    print(f'ЛЕВИЙ ➤ Вы входите в большой дом, около барной стойки стоит хозяин таверны, который предлагает вам обед:')
    print(f'1️⃣ [Мясное рагу] ➤ {food_info["1"]["price"]} 🪙 ➕ {food_info["1"]["health"]} единиц ❤️')
    print(f'2️⃣ [Кружка кваса] ➤ {food_info["2"]["price"]} 🪙 ➕ {food_info["2"]["health"]} единиц ❤')
    meal = input('🡆 ')

    if meal in food_info.keys():
        if player.money < food_info[meal]['price']:
            print('ЛЕВИЙ ➤ Вы нищий, так как вы нищий...')
        else:
            player.money -= food_info[meal]['price']
            player.hp += food_info[meal]['health']
            print(f'[❗] Вы потратили {food_info[meal]["price"]} 🪙 и получили {food_info[meal]["health"]} единиц ❤️')
    else:
        print(f'ЛЕВИЙ ➤ За вашу неотесанную грубость хозяин таверны вас прогнал.')
        print(f'ЛЕВИЙ ➤ Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой')
        food_info['1']['price'] += randint(2, 8)
        food_info['2']['price'] += randint(4, 10)
