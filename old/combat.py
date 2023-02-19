from random import randint


def choosing_enemy(self):
    self.enemy = enemies[randint(1, 4)]


def player_hp_info(self, player_hp):
    print(f"[❗] Ваше ❤️: {self.player.hp} единиц\n")


def battle_process(self):
    print(f"👨‍💻 ЛЕВИЙ ➤ О НЕТ,{self.player.player_name} вас атаковал {self.enemy.enemy_character}!\n\n"
          f"[🧑 ❤️] Ваше здоровье: {self.player.hp} единиц\t[👺 ❤️] Здоровье врага: {self.enemy.hp} единиц\n"
          f"[🧑 🗡️] Ваша атака: {self.player.attack} единиц \t[👺 🗡️] Атака врага: {self.enemy.attack} единиц\n"
          f"[🧑 🛡️] Ваша защита: {self.player.defense} единиц\t[👺 🛡️] Защита врага: {self.enemy.defense} единиц\n")
    while True:
        self.player.player_battle_move(self.player, self.enemy)
        if self.enemy.hp <= 0:
            self.battle_result(True)
            break

        self.enemy.enemy_battle_move(self.enemy, self.player)
        self.player_hp_info(self.player.hp)
        if self.player.hp <= 0:
            self.battle_result(False)
            break


def battle_result(self, result):
    if result:
        received_money = randint(1, 10)
        received_xp = randint(5, 15)
        self.player.money += received_money
        self.player.xp += received_xp
        print("👨‍💻 ЛЕВИЙ ➤ Это победа!!! Поздравляем!!!\n"
              f"[❗] Вы получаете: {received_money} 🪙 и {received_xp} ✨")
        self.choosing_location()
    else:
        print(f"[❗] Вас уничтожили... Что вы хотите?\n\n"
              f"1️⃣ Сыграть еще разик ✅\n"
              f"2️⃣ Выйти из игры ❌\n")
        player_choice = input("🡆 ")
        self.player_bad_battle_result(player_choice)


def player_bad_battle_result(self, player_choice):
    if player_choice == "1":
        self.start()
    else:
        exit(0)
