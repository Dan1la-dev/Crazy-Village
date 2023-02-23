from time import sleep
from random import randint


def battle_info(character, enemy: callable):
    print(f"[🧑 ❤️] Ваше здоровье: {character.hp} единиц\t[👺 ❤️] Здоровье врага: {enemy.hp} единиц")
    print(f"[🧑 🗡️] Ваша атака: {character.attack} единиц  \t[👺 🗡️] Атака врага: {enemy.attack} единиц")
    print(f"[🧑 🛡️] Ваша защита: {character.defense} единиц  \t[👺 🛡️] Защита врага: {enemy.defense} единиц\n")


def forest(character: callable, enemy: callable):
    print('👨‍💻 ЛЕВИЙ ➤ Вы стоите на опушке огромного леса, деревья шумят своими огромными кронами,'
          'тут начинается ваш путь авантюриста...')
    sleep(0.5)
    print('👨‍💻 ЛЕВИЙ ➤ О НЕТ, ВОЖДЬ! НА ВАС НАПАЛИ!!!')
    print(f"👨‍💻 ЛЕВИЙ ➤ О НЕТ,{character.name} вас атаковал {enemy.type}!")
    battle_info(character, enemy)
    print("🧑 Ваш ход: ")

    for move in range(len(character.battle_moves)):
        print(f'{move + 1}️⃣  {character.battle_moves[move]}')

    while True:
        battle_choice = input("🡆 ")

        if battle_choice == '1':
            enemy.take_damage(character.attack)
        elif battle_choice == '2':
            print(f"🛡️🛡️🛡️ Вы повысили свою защиту в размере {character.get_defense()} ед")

        if not enemy.check_hp():
            battle_info(character, enemy)
            print("👨‍💻 ЛЕВИЙ ➤ Вы победили!!! Вы - настоящий боец")

            earned_money = randint(10, 100)
            character.earn_money(earned_money)

            earned_xp = randint(13, 50)
            character.earn_xp(earned_xp)

            print(f"💎 НАГРАДЫ: "
                  f"➡️ {earned_money} 🪙"
                  f"➡️ {earned_xp} ✨")
            break

        battle_info(character, enemy)

        print("👺 Ход врага: \n")
        sleep(0.3)

        if randint(1, 2) == 1:
            character.take_damage(enemy.attack)
        elif randint(1, 2) == 2:
            enemy.get_defense()

        if not character.check_hp():
            battle_info(character, enemy)
            break

        battle_info(character, enemy)









