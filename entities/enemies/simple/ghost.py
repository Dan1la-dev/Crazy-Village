from classes.enemy import Enemy


class Ghost(Enemy):
    type = 'Призрак'

    def __init__(self):
        """Initialize inherited enemy's object with default values."""
        super().__init__()
        self.hp = 100
        self.attack = 100
        self.defense = 0
