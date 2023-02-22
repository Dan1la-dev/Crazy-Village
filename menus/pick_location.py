from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest


def pick_location(character):
    while character.alive:
        print('Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        print('[1] Таверна')
        print('[2] Полигон')
        print('[3] Лес')
        location = input('➥ ')
        if location == '1':
            tavern(character)
        if location == '2':
            if character.debt:
                print(f"👨‍💻 ЛЕВИЙ ➤ Охрана полигона не пускает вас из за вашего долга в размере {character.money} 🪙")
                print("👨‍💻 ЛЕВИЙ ➤ Сказали, что, пустят, когда вы уплатите должок...\n")
            else:
                polygon(character)
        if location == '3':
            forest(character)
