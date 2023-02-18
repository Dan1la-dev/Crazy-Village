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
        print('\n⬇️ Ваша статистика ⬇️\n'
              f'🧑 Имя: {self.character_name}\n'
              f'🥋 Персонаж: {self.character.character}\n'
              f'✨ Текущий опыт: {self.character.xp}\n'
              f'🥇 Текущий уровень: {self.character.lvl}\n'
              f'❤️ Здоровье: {self.character.hp}\n'
              f'🗡️ Атака: {self.character.attack}\n'
              f'🛡️ Защита: {self.character.defense}\n'
              f'🎒 Инвентарь: {self.character.inventory}\n'
              f'💧 Мана: {self.character.mp}\n'
              f'🪙 Деньги: {self.character.money}\n'
              f'🔥 Способность: {self.character.ultimate}\n')
