from classes.character import Character


class Warrior(Character):
    battle_class = 'Воин'

    def __init__(self, name: str):
        """Initialize inherited character's object with default values.
        :param name: It used to initialize player's name"""

        super().__init__()
        self.name = name
        self.hp = 150
        self.attack = 10
        self.defense = 10
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 10
        self.ultimate = 'Землетряс'
