from random import randint

PRICE_KEY = 'price'
DAMAGE_KEY = 'damage'
DEFENSE_KEY = 'defense'
MANA_KEY = 'mana'
HEALTH_KEY = 'health'

trainings = {
    '1': {PRICE_KEY: 110, DAMAGE_KEY: 1},   # Sword sparring
    '2': {PRICE_KEY: 135, DEFENSE_KEY: 3},  # Damage reduction training
    '3': {PRICE_KEY: 120, MANA_KEY: 4},     # Mana control
    '4': {PRICE_KEY: 200, HEALTH_KEY: 2},   # Body fit
}


def polygon(character: callable):
    input('🧿 Нажмите Enter для продолжения...')
    print("\n" * 99999)

    print(f'👨‍💻 ЛЕВИЙ ➤ Вы оказываетесь на большом открытом пространстве, где каждый метр занят тренирующимися людьми.')
    print(f'‍👨‍💻 ЛЕВИЙ ➤ К вам подходит человек и представляется тренером, он дает вам выбор:')
    print()

    print(f'1️⃣ [Спарринг на мечах ➤ {trainings["1"][PRICE_KEY]} 🪙] ➕ {trainings["1"][DAMAGE_KEY]} единиц 🗡️')
    print(f'2️⃣ [Тренировка подавления урона ➤ {trainings["2"][PRICE_KEY]} 🪙] ➕ {trainings["2"][DEFENSE_KEY]} единиц 🛡️')
    print(f'3️⃣ [Контроль чакры ➤ {trainings["3"][PRICE_KEY]} 🪙] ➕ {trainings["3"][MANA_KEY]} единиц 💧')
    print(f'4️⃣ [Тренировка тела ➤ {trainings["4"][PRICE_KEY]} 🪙] ➕ {trainings["4"][HEALTH_KEY]} единиц ❤️')
    print()

    training = input('>>> ')
    print()

    if training in trainings.keys():
        cost = trainings[training][PRICE_KEY]
        if character.money < cost:
            print('👨‍💻 ЛЕВИЙ ➤ Вы нищий, так как вы нищий...')
        else:
            if training == '1':
                character.spend_money(cost)
                character.attack += trainings['1'][DAMAGE_KEY]

                print(f'[❗] Вы потратили {cost} 🪙 и получили {trainings["1"][DAMAGE_KEY]} единиц 🗡️')
                print(f'[❗] Ваша 🗡️ теперь: {character.attack} единиц')
            elif training == '2':
                character.spend_money(cost)
                character.defense += trainings['2'][DEFENSE_KEY]

                print(f'[❗] Вы потратили {cost} 🪙 и получили {trainings["2"][DEFENSE_KEY]} единиц 🛡️')
                print(f'[❗] Ваша 🛡️ теперь: {character.defense} единиц')
            elif training == '3':
                character.spend_money(cost)
                character.mp += trainings['3'][MANA_KEY]

                print(f'[❗] Вы потратили {cost} 🪙 и получили {trainings["3"][MANA_KEY]} единиц 💧')
                print(f'[❗] Ваша 💧 теперь: {character.mp} единиц')
            elif training == '4':
                character.spend_money(cost)
                character.hp += trainings['4'][HEALTH_KEY]

                print(f'[❗] Вы потратили {cost} 🪙 и получили {trainings["4"][HEALTH_KEY]} единиц ❤️')
                print(f'[❗] Ваше ❤️ теперь: {character.hp} единиц')
    else:
        lost_hp = randint(10, 30)
        character.take_damage(lost_hp)

        lost_money = randint(10, 100)
        character.spend_money(lost_money)

        print(f'👨‍💻 ЛЕВИЙ ➤ Занимающимся в залах злым качкам не понравилось ваше поведение'
              f'и вам прописали двойной апперкот и после вашего падения у вас выпали 🪙')
        print(f'[❗] Вы потеряли {lost_hp} единиц ❤️ и {lost_money} 🪙')

        if randint(1, 10) == 1 and character.debt:
            print('👨‍💻 ЛЕВИЙ ➤ Так же тренер подал на вас в суд деревни за неправомерное поведение' 
                  f'и суд выставил на вас долг в размере {-lost_money} ')
