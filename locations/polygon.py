from random import randint

trainings = {
    '1': {'price': 110, 'damage': 1},   # Sword sparring
    '2': {'price': 135, 'defense': 3},  # Damage reduction training
    '3': {'price': 120, 'mana': 4},     # Mana control
    '4': {'price': 200, 'health': 2},   # Body fit
}


def polygon(character):
    print(f'ЛЕВИЙ ➤ Вы оказываетесь на большом открытом пространстве, где каждый метр занят тренирующимися людьми.')
    print(f'К вам подходит человек и представляется тренером, он дает вам выбор:')
    print(f'1️⃣ [Спарринг на мечах ➤ {trainings["1"]["price"]} 🪙] ➕ {trainings["1"]["damage"]} единиц 🗡️')
    print(f'2️⃣ [Тренировка подавления урона ➤ {trainings["2"]["price"]} 🪙] ➕ {trainings["2"]["defense"]} единиц 🛡️')
    print(f'3️⃣ [Контроль чакры ➤ {trainings["3"]["price"]} 🪙] ➕ {trainings["3"]["mana"]} единиц 💧')
    print(f'4️⃣ [Тренировка тела ➤ {trainings["4"]["price"]} 🪙] ➕ {trainings["4"]["health"]} единиц ❤️')
    training = input('🡆 ')

    if training in trainings.keys():
        if character.money < trainings[training]["price"]:
            print('👨‍💻 ЛЕВИЙ ➤ Вы нищий, так как вы нищий...')
        else:
            if training == '1':
                character.money -= trainings['1']['price']
                character.attack += trainings['1']['damage']
                print(f'[❗] Вы потратили {trainings["1"]["price"]} 🪙 и получили {trainings["1"]["damage"]} единиц 🗡️')
                print(f'[❗] Ваша 🗡️ теперь: {character.attack} единиц')
            if training == '2':
                character.money -= trainings['2']['price']
                character.defense += trainings['2']['defense']
                print(f'[❗] Вы потратили {trainings["2"]["price"]} 🪙 и получили {trainings["2"]["defense"]} единиц 🛡️')
                print(f'[❗] Ваша 🛡️ теперь: {character.defense} единиц')
            if training == '3':
                character.money -= trainings['3']['price']
                character.mp += trainings['3']['mana']
                print(f'[❗] Вы потратили {trainings["3"]["price"]} 🪙 и получили {trainings["3"]["mana"]} единиц 💧')
                print(f'[❗] Ваша 💧 теперь: {character.mp} единиц')
            if training == '4':
                character.money -= trainings['4']['price']
                character.hp += trainings['4']['health']
                print(f'[❗] Вы потратили {trainings["4"]["price"]} 🪙 и получили {trainings["4"]["health"]} единиц ❤️')
                print(f'[❗] Ваше ❤️ теперь: {character.hp} единиц')
    else:
        lost_hp = randint(10, 30)
        character.take_damage(lost_hp)
        lost_money = randint(10, 100)
        character.spend_money(lost_money)
        print(f'👨‍💻 ЛЕВИЙ ➤ Занимающимся в залах злым качкам не понравилось ваше поведение'
              f'и вам прописали двойной апперкот и после вашего падения у вас выпали 🪙')
        print(f'[❗] Вы потеряли {lost_hp} единиц ❤️ и {lost_money} 🪙')
        if randint(1, 1) == 1 and character.debt:
            print('👨‍💻 ЛЕВИЙ ➤ Так же тренер подал на вас в суд деревни за неправомерное поведение' 
                  f'и суд выставил на вас долг в размере {-lost_money} ')
