from random import randint

trainings_info = {
    "1": [110, 1],
    "2": [135, 3],
    "3": [120, 4],
    "4": [200, 2]
}


def polygon(character):

    print("ЛЕВИЙ ➤ Вы оказываетесь на большом открытом пространстве, где каждый метр занят тренирующимися людьми.\n"
          "К вам подходит человек и представляется тренером, он дает вам выбор:\n"

          f"1️⃣ [Спаринг на мечах ➤ {trainings_info['1'][0]} 🪙] ➕ "
          f"{trainings_info['1'][1]} единиц 🗡️\n"

          f"2️⃣ [Тренировка подавления урона ➤ {trainings_info['2'][0]} 🪙] ➕ "
          f"{trainings_info['2'][1]} единиц 🛡️\n"

          f"3️⃣ [Контроль чакры и взаимодействие с магией ➤ {trainings_info['3'][0]} 🪙] ➕ "
          f"{trainings_info['3'][1]} единиц 💧\n"

          f"4️⃣ [Тренировка тела ➤ {trainings_info['4'][0]} 🪙] ➕ "
          f"{trainings_info['4'][1]} единиц ❤️\n")

    player_choice = input("🡆 ")

    if player_choice in trainings_info and character.money >= trainings_info[player_choice][0]:
        character.money -= trainings_info[player_choice][0]

        if player_choice == "1":
            gotten_attack = trainings_info[player_choice][1]
            character.attack += gotten_attack
            print(f"[❗] Вы потратили {trainings_info[player_choice][0]} 🪙 "
                  f"и получили {gotten_attack} единиц 🗡️\n"

                  f"[❗] Ваша 🗡️ теперь: {character.attack} единиц\n")
        elif player_choice == "2":
            gotten_defense = trainings_info[player_choice][1]
            character.defense += gotten_defense
            print(f"[❗] Вы потратили {trainings_info[player_choice][0]} 🪙 "
                  f"и получили {gotten_defense} единиц 🛡️\n"

                  f"[❗] Ваша 🛡️ теперь: {character.defense} единиц\n")
        elif player_choice == "3":
            gotten_mp = trainings_info[player_choice][1]
            character.mp += gotten_mp
            print(f"[❗] Вы потратили {trainings_info[player_choice][0]} 🪙 "
                  f"и получили {gotten_mp} атаки\n"

                  f"[❗] Ваша 💧 теперь: {character.mp} единиц\n")
        elif player_choice == "4":
            gotten_hp = trainings_info[player_choice][1]
            character.hp += gotten_hp
            print(f"[❗] Вы потратили {trainings_info[player_choice][0]} 🪙 "
                  f"и получили {gotten_hp} единиц ❤️\n"
                  f"[❗] Ваше ❤️ теперь: {character.hp} единиц")

    elif player_choice in trainings_info and character.money < trainings_info[player_choice][0]:
        print("👨‍💻 ЛЕВИЙ ➤ Вы нищий, так как вы нищий...")

    else:
        lost_hp = randint(10, 30)
        character.hp -= lost_hp
        lost_money = randint(10, character.money)
        character.money -= lost_money
        print("👨‍💻 ЛЕВИЙ ➤ Занимающимся в залах злым качкам не понравилось ваше поведение "
              "и вам прописали двойной апперкот и после вашего падения у вас выпали 🪙\n"
              f"[❗] Вы потеряли {lost_hp} единиц ❤️ и {randint(10, character.money)} 🪙\n")