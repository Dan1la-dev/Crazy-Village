from classes.enemy import Enemy


class Necron(Enemy):
    type = 'Некрон'
    
    def __init__(self):
        """Initialize inherited enemy's object with default values."""
        super().__init__()
        self.hp = 300
        self.attack = 5
        self.defense = 50
        self.ultimate = {
            'skill': 'Тотальная защита',
            'duration': 5,
        }
