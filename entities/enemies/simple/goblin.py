from classes.enemy import Enemy


class Goblin(Enemy):
    type = 'Гоблин'

    def __init__(self):
        """Initialize inherited enemy's object with default values."""
        super().__init__()
        self.hp = 100
        self.attack = 40
        self.defense = 20
