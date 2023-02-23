from entities.characters.warrior import Warrior
from entities.characters.archer import Archer
from entities.characters.wizard import Wizard


def pick_character():
    """ Sets player's character """
    print("\n" * 99999)
    print("👨‍💻 ЛЕВИЙ ➤ Введите ваше имя")
    print()
    name = input('>>> ')

    available_classes = [
        {'class': Warrior, 'description': 'персонаж ближнего боя, выносит большое количество урона.'},
        {'class': Archer, 'description': 'персонаж дальнего боя, наносит большой урон на расстоянии.'},
        {'class': Wizard, 'description': 'персонаж мастер-магии, наносит огромный стихийный урон.'},
    ]

    while True:
        print('👨‍💻 ЛЕВИЙ ➤ Выберите класс')
        print()

        for i, battle_class in enumerate(available_classes):
            print(f'{i+1}️⃣ {battle_class["class"].battle_class} - {battle_class["description"]}')
        print()
        battle_class_index = input('>>> ')
        print()

        try:
            battle_class = available_classes[int(battle_class_index) - 1]['class']
        except (ValueError, IndexError):
            print('[❗] Неверное значение. Повторите попытку...')
        else:
            return battle_class(name)

        input('🧿 Нажмите Enter для продолжения...')
        print("\n" * 99999)

