from entities.characters.warrior import Warrior
from entities.characters.archer import Archer
from entities.characters.wizard import Wizard
from misc.consts import CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, PRESS_ENTER
from menus.pick_character_name import pick_character_name


# A list of available character classes with their respective descriptions
AVAILABLE_CLASSES = [
    {'class': Warrior, 'description': 'персонаж ближнего боя, выносит большое количество урона.'},
    {'class': Archer, 'description': 'персонаж дальнего боя, наносит большой урон на расстоянии.'},
    {'class': Wizard, 'description': 'персонаж мастер-магии, наносит огромный стихийный урон.'},
]


def display_classes():
    """Displays the available character classes"""
    # Clear the screen and print the header
    print(f'{HEADER} Выберите персонажа: ')
    print()
    # Print the available character classes with their descriptions
    for i, battle_class in enumerate(AVAILABLE_CLASSES):
        print(f"{i+1}️⃣ {battle_class['class'].battle_class} - {battle_class['description']}")
    print()


def get_class_choice():
    """Gets the user's class choice"""
    while True:
        # Display the available character classes
        display_classes()
        # Get the user's input for the character class index
        battle_class_index = input(PROMPT)
        print()
        try:
            # Convert the input to an integer index and check if it's valid
            index = int(battle_class_index)
            if index <= 0 or index > len(AVAILABLE_CLASSES):
                raise ValueError
            # Get the chosen character class based on the index entered
            battle_class = AVAILABLE_CLASSES[index - 1]['class']
        except (ValueError, IndexError):
            # If an error occurs, notify the user and prompt them to try again
            print(f'{ATTENTION} Неверное значение. Повторите попытку...')
            print()
            input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
            print(CLEAR_SCREEN)
        else:
            # If the input is valid, return the chosen character class
            return battle_class


def pick_character():
    """Sets player's character"""
    battle_class = get_class_choice()
    name = pick_character_name()

    # Create a new instance of the chosen character class with the user's name and return it
    return battle_class(name)
