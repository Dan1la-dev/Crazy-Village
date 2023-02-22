from time import sleep


def forest(character, enemy):
    print('👨‍💻 ЛЕВИЙ ➤ Вы стоите на опушке огромного леса, деревья шумят своими огромными кронами,'
          'тут начинается ваш путь авантюриста...')
    sleep(0.5)
    print('👨‍💻 ЛЕВИЙ ➤ О НЕТ, ВОЖДЬ! НА ВАС НАПАЛИ!!!')

    print(f"👨‍💻 ЛЕВИЙ ➤ О НЕТ,{character.name} вас атаковал {enemy.type}!\n\n"
          f"[🧑 ❤️] Ваше здоровье: {character.hp} единиц\t[👺 ❤️] Здоровье врага: {enemy.hp} единиц\n"
          f"[🧑 🗡️] Ваша атака: {character.attack} единиц  \t[👺 🗡️] Атака врага: {enemy.attack} единиц\n"
          f"[🧑 🛡️] Ваша защита: {character.defense} единиц  \t[👺 🛡️] Защита врага: {enemy.defense} единиц\n")


