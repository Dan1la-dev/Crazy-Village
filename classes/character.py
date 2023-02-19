class Character:
    def __init__(self, dictionary):
        self.character_name = ""
        self.character = dictionary["Тип"]
        self.hp = dictionary["Здоровье"]
        self.attack = dictionary["Атака"]
        self.lvl = dictionary["Уровень"]
        self.defense = dictionary["Защита"]
        self.inventory = dictionary["Инвентарь"]
        self.mp = dictionary["Мана"]
        self.xp = dictionary["Опыт"]
        self.money = dictionary["Деньги"]
        self.ultimate = dictionary["Способность"]

    def get_info(self):
        print(f'⬇️ Ваша статистика ⬇️')
        print(f'🧑 Имя: {self.character_name}')
        print(f'🥋 Персонаж: {self.character.character}')
        print(f'✨ Текущий опыт: {self.character.xp}')
        print(f'🥇 Текущий уровень: {self.character.lvl}')
        print(f'❤️ Здоровье: {self.character.hp}')
        print(f'🗡️ Атака: {self.character.attack}')
        print(f'🛡️ Защита: {self.character.defense}')
        print(f'🎒 Инвентарь: {self.character.inventory}')
        print(f'💧 Мана: {self.character.mp}')
        print(f'🪙 Деньги: {self.character.money}')
        print(f'🔥 Способность: {self.character.ultimate}')
