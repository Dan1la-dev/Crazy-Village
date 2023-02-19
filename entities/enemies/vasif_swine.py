from classes.enemy import Enemy


class VasifSwine(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Васифсвин'
        self.hp = 300
        self.attack = 5
        self.defense = 50
        self.ultimate = {
            'skill': 'Тотальная защита',
            'duration': 5,
        }
