from time import sleep
from random import randint


def battle_info(character, enemy: callable):
    print()
    print(f"[🧑 ❤️] Ваше здоровье: {character.hp}\t[👺 ❤️] Здоровье врага: {enemy.hp} ")
    print(f"[🧑 🗡️] Ваша атака: {character.attack}   \t[👺 🗡️] Атака врага: {enemy.attack} ")
    print(f"[🧑 🛡️] Ваша защита: {character.defense}   \t[👺 🛡️] Защита врага: {enemy.defense}")
    print()


def forest(character: callable, enemy: callable):
    input('🧿 Нажмите Enter для продолжения...')
    print("\n" * 99999)

    print('👨‍💻 ЛЕВИЙ ➤ Вы стоите на опушке огромного леса, деревья шумят своими огромными кронами,'
          'тут начинается ваш путь авантюриста...')
    sleep(0.5)
    print(f"👨‍💻 ЛЕВИЙ ➤ О НЕТ,{character.name} вас атаковал {enemy.type}!")

    while True:
        battle_info(character, enemy)
        print("[🧑] Ваш ход: ")
        print()
        for move in range(len(character.battle_moves)):
            print(f'{move + 1}️⃣  {character.battle_moves[move]}')
        print()

        character_move = input(">>> ")
        print()

        if character_move == '1':
            enemy.take_damage(character.attack)
            print(f"[🧑] Вы уменьшили 👺 ❤️ с {enemy.hp} >>> {enemy.take_damage(character.attack)}")

            print(f"[👺 ❤️ ❗] Здоровье врага: {enemy.hp}")
            print()
        elif character_move == '2':
            print(f"[🧑🛡️🛡️] Вы повысили свою 🛡️🛡️🛡️ c {character.defense} >>> {character.get_defense()}")

            print(f"[🧑🛡️❗] Ваша защита: {character.defense}")
            print()
        if not enemy.alive:
            print("👨‍💻 ЛЕВИЙ ➤ Вы победили!!! Вы - настоящий боец")

            earned_money = randint(10, 100)
            character.earn_money(earned_money)

            earned_xp = randint(13, 50)
            character.earn_xp(earned_xp)

            print(f"💎 НАГРАДЫ 💎  ")
            print(f"➡️ {earned_money} 🪙")
            print(f"➡️ {earned_xp} ✨")
            break

        sleep(5)
        print("\n" * 99999)
        print("[👺] Ход врага: \n")
        sleep(0.3)

        enemy_move = randint(1, 2)

        if enemy_move == 1:
            print(f"[👺] Враг уменьшил ваше ❤️❤️❤️ с {character.hp} >>> {character.take_damage(enemy.attack)}")
            print(f"[🧑❤️❗] Ваше здоровье: {character.hp}")
        elif enemy_move == 2:
            print(f"[👺] Враг повысил свою 🛡️🛡️🛡️ с {enemy.defense} >>> {enemy.get_defense()}")
            print(f"[👺🛡️❗] Защита врага: {enemy.defense}")

        if not character.alive:
            break

        sleep(5)
        print("\n" * 99999)












