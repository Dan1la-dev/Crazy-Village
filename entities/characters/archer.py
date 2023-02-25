from classes.character import Character


class Archer(Character):
    battle_class = '🏹 Лучник'

    def __init__(self, name):
        """Initialize inherited character's object with default values.
        :param name: It used to initialize player's name"""

        super().__init__()
        self.name = name
        self.hp = 120
        self.attack = 30
        self.defense = 3
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 30
        self.ultimate = 'Землетряс'

