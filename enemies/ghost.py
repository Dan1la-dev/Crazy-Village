from classes.enemy import Enemy


class Ghost(Enemy):
    def __init__(self):
        super().__init__()
        self.type = 'Призрак'
        self.hp = 100
        self.attack = 100
        self.defense = 0
