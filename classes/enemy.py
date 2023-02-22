from typing import NoReturn


class Enemy:
    def __init__(self):
        self.alive = True
        self.type = None
        self.hp = None
        self.attack = None
        self.defense = None
        self.ultimate = None

    def get_stats(self) -> NoReturn:
        print(f'Enemy Type: {self.type}')
        print(f'HP: {self.hp}')
        print(f'Attack: {self.attack}')
        print(f'Defense: {self.defense}')
        print(f'Ultimate: {self.ultimate}')

    def take_damage(self) -> bool:
        if self.hp <= 0:
            self.alive = False
        return self.alive
