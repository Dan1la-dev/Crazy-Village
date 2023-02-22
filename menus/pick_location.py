from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest
from menus.pick_enemy import pick_enemy


def pick_location(character):
    """Sets player's location"""
    while character.alive:
        print('Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        print('[1] Таверна')
        print('[2] Полигон')
        print('[3] Лес')

        location = input('➥ ')

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
        else:
            print("Неверный ввод. Пожалуйста, выберите 1, 2 или 3.\n")
