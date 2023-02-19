from locations.tavern import tavern
from locations.polygon import polygon
from locations.forest import forest


def pick_location(character):
    while True:
        print('Вы появляетесь в деревне новичков, выберите, куда вы отправитесь:')
        print('[1] Таверна')
        print('[2] Полигон')
        print('[3] Лес')
        location = input('➥ ')
        if location == '1':
            tavern(character)
        if location == '2':
            polygon(character)
        if location == '3':
            forest(character)
