class Enemy:
    def __init__(self):
        self.alive = True
        self.type = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.ultimate = None
    def take_damage(self):
        if self.hp <= 0:
            self.alive = False
