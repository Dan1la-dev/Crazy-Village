from entities.characters.warrior import Warrior
from entities.characters.archer import Archer
from entities.characters.wizard import Wizard
from misc.consts import CLEAR_SCREEN, HEADER, PROMPT, ATTENTION, NUMERATION, PRESS_ENTER
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
    print(CLEAR_SCREEN)
    print(f'{HEADER} Выберите класс')
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
            # Get the chosen character class based on the index entered
            battle_class = AVAILABLE_CLASSES[int(battle_class_index) - 1]['class']
        except (ValueError, IndexError):
            # If an error occurs, notify the user and prompt them to try again
            print(f'{ATTENTION} Неверное значение. Повторите попытку...')
        else:
            # If the input is valid, return the chosen character class
            return battle_class


def pick_character():
    """Sets player's character"""
    # Get the user's chosen character class
    battle_class = get_class_choice()
    # Create a new instance of the chosen character class with the user's name and return it
    return battle_class(pick_character_name())
