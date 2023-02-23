from classes.enemy import Enemy


class Barbarian(Enemy):
    type = 'Варвар'

    def __init__(self):
        """Initialize inherited enemy's object with default values."""
        super().__init__()
        self.hp = 150
        self.attack = 50
        self.defense = 8
