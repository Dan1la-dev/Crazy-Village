from classes.enemy import Enemy


class Barbarian(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Варвар'
        self.hp = 150
        self.attack = 50
        self.defense = 8
