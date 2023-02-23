from classes.character import Character


class Wizard(Character):
    battle_class = '🪄 Маг'

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 110
        self.attack = 30
        self.defense = 0
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 50
        self.ultimate = 'Землетряс'
