from entities.characters.warrior import Warrior
from entities.characters.archer import Archer
from entities.characters.wizard import Wizard


def pick_character():
    """ Sets player's character """
    print("👨‍💻 ЛЕВИЙ ➤ Введите ваше имя")
    name = input('>>> ')

    battle_classes = {
        '1': Warrior(name),
        '2': Archer(name),
        '3': Wizard(name)}

    while True:
        print('Выберите класс:')
        print('1️⃣ Воин 🗡️ - мастер ближнего боя, выносит большое количество урона.')
        print('2️⃣ Лучник 🏹 - мастер дальнего боя, наносит большой урон на расстоянии.')
        print('3️⃣ Маг 🪄 - мастер магии, наносит огромный стихийный урон')
        battle_class = input('>>> ')
        if battle_class in battle_classes.keys():
            return battle_classes[battle_class]
