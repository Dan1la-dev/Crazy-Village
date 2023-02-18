from classes.character import Character
from misc.null import NULL
from classes.enemy import Enemy
from random import randint
from entities.characters import *
from entities.enemies import *


class Menu:
    character = Character(NULL)
    enemy = Enemy(NULL)

    def get_character(self):
        print("👨‍💻 ЛЕВИЙ ➤ Добро пожаловать в игру 'Безумный посёлок'"
              "\n\n👨‍💻 ЛЕВИЙ ➤ Введите ваше имя...\n")
        self.character.player_name = input("🡆 ")

        print('Выберите персонажа:\n'
              '1️⃣ Воин 🗡️ - мастер ближнего боя, выносит большое количество урона.\n'
              '2️⃣ Лучник 🏹 - мастер дальнего боя, наносит большой урон на расстоянии.\n'
              '3️⃣ Маг 🪄 - мастер магии, наносит огромный стихийный урон\n')

        player_choice = ""

        characters = {
            "1": Character(WARRIOR),
            "2": Character(ARCHER),
            "3": Character(WIZARD),
        }

        while player_choice not in characters:
            player_choice = input("🡆 ")
            if player_choice in characters:
                self.character = characters[player_choice]
            else:
                print("[❗] Данного персонажа нет в списке, повторите попытку\n")

    def get_enemy(self):
        enemies = {
            1: Enemy(GOBLIN),
            2: Enemy(BARBARIAN),
            3: Enemy(GHOST),
            4: Enemy(BOSS_PIG)
        }
        enemy_choice = randint(1, 4)
        self.enemy = enemies[enemy_choice]
