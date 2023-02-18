from random import randint

food_info = {
    "1": [10, 5],
    "2": [2, 2]
}


def tavern(player):
    print(
        f"ЛЕВИЙ ➤ Вы входите в большой дом, "
        f"около барной стойки стоит хозяин таверны, "
        f"который предлагает вам обед: \n"

        f"1️⃣ [Мясное рагу] ➤ {food_info['1'][0]} 🪙 ➕ {food_info['1'][1]} единиц ❤️\n"
        f"2️⃣ [Кружка кваса] ➤ {food_info['2'][0]} 🪙 ➕ {food_info['2'][1]} единиц ❤️\n")
    player_choice = input("🡆 ")

    if player_choice in food_info and player.money >= food_info[player_choice][0]:
        player.money -= food_info[player_choice][0]
        gotten_hp = food_info[player_choice][1]
        player.hp += gotten_hp
        print(f"[❗] Вы потратили {food_info[player_choice][0]} 🪙 и получили {gotten_hp} единиц ❤️\n")

    elif player_choice in food_info and player.money < food_info[player_choice][0]:
        print("ЛЕВИЙ ➤ Вы нищий, так как вы нищий...")

    else:
        print("ЛЕВИЙ ➤ За вашу неотесанную грубость хозяин таверны вас прогнал.\n"
              f"ЛЕВИЙ ➤Похоже, хозяин таверны теперь будет торговать с вами с большей.... наценкой\n")
        food_info['1'][0] += randint(2, 8)
        food_info['2'][0] += randint(4, 10)
