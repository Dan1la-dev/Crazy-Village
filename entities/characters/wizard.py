from classes.character import Character


class Wizard(Character):
    battle_class = '🪄 Маг'

    def __init__(self, name):
        """Initialize inherited character's object with default values.
        :param name: It used to initialize player's name"""

        super().__init__()
        self.name = name
        self.hp = 100
        self.attack = 70
        self.defense = 0
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 90
        self.ultimate = 'Землетряс'
