class Enemy:
    def __init__(self, dictionary):
        self.enemy_character = dictionary["Тип"]
        self.hp = dictionary["Здоровье"]
        self.attack = dictionary["Атака"]
        self.defense = dictionary["Защита"]
        self.ultimate = dictionary["Способность"]