from classes.character import Character


class Warrior(Character):
    battle_class = '⚔️ Воин'

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hp = 10
        self.attack = 10
        self.defense = 10
        self.inventory = ['Карта', 'Зелье здоровья', 'Соль']
        self.mp = 10
        self.ultimate = 'Землетряс'
