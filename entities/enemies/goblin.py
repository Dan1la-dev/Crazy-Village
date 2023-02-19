from classes.enemy import Enemy


class Goblin(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Гоблин'
        self.hp = 100
        self.attack = 40
        self.defense = 20
