from classes.character import Character


class Archer(Character):
    battle_class = '🏹 Лучник'

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.type = 'Лучник'
        self.hp = 100
        self.attack = 50
        self.defense = 3
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 30
        self.ultimate = 'Землетряс'
