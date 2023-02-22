from entities.characters.warrior import Warrior
from entities.characters.archer import Archer
from entities.characters.wizard import Wizard


def pick_character():
    """ Sets player's character """
    print("👨‍💻 ЛЕВИЙ ➤ Введите ваше имя")
    name = input('>>> ')

    available_classes = [
        {'class': Warrior, 'description': 'маг ближнего боя, выносит большое количество урона.'},
        {'class': Archer, 'description': 'маг дальнего боя, наносит большой урон на расстоянии.'},
        {'class': Wizard, 'description': 'мастер магии, наносит огромный стихийный урон.'},
    ]

    while True:
        print('Выберите класс:')

        for i, battle_class in enumerate(available_classes):
            print(f'{i+1}️⃣ {battle_class["class"].__name__} 🗡️ - {battle_class["description"]}')

        battle_class_index = input('>>> ')
        battle_class = available_classes[int(battle_class_index)-1]['class']

        return battle_class(name)
