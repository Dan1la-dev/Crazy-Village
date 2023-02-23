from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest
from menus.pick_enemy import pick_enemy
from typing import NoReturn


def pick_location(character: callable) -> NoReturn:
    """Sets player's location"""
    while character.alive:
        input('🧿 Нажмите Enter для продолжения...')
        print("\n" * 99999)

        print('👨‍💻 ЛЕВИЙ ➤ Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        print()
        print('1️⃣ Таверна 🏠')
        print('2️⃣ Полигон 💪')
        print('3️⃣ Лес 🌲')
        print('4️⃣ Статистика 🔆')
        print()
        location = input('>>> ')

        if location == '1':
            tavern(character)
        elif location == '2':
            if character.debt:
                print(f"👨‍💻 ЛЕВИЙ ➤ Охрана полигона не пускает вас из за вашего долга в размере {character.money} 🪙")
                print("👨‍💻 ЛЕВИЙ ➤ Сказали, что, пустят, когда вы уплатите должок...\n")
            else:
                polygon(character)
        elif location == '3':
            forest(character, pick_enemy())
        elif location == '4':
            character.get_stats()
        else:
            print("[❗] Неверный ввод. Повторите попытку...')\n")


