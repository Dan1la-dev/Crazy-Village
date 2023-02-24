from random import randint
from misc.consts import *

TRAININGS = {
    '1': {PRICE_KEY: 110, DAMAGE_KEY: 1},   # Sword sparring
    '2': {PRICE_KEY: 135, DEFENSE_KEY: 3},  # Damage reduction training
    '3': {PRICE_KEY: 120, MANA_KEY: 4},     # Mana control
    '4': {PRICE_KEY: 200, HEALTH_KEY: 2},   # Body fit
}


def polygon(character: callable):
    """One of three locations
    :param character: It used to transmit character's params"""
    input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
    print(CLEAR_SCREEN)

    print(f'{HEADER} Вы оказываетесь на большом открытом пространстве, где каждый метр занят тренирующимися людьми.')
    print(f'{HEADER} ➤ К вам подходит человек и представляется тренером, он дает вам выбор:')
    print()

    print(f'{NUMERATION[1]} [Спарринг на мечах ➤ {TRAININGS["1"][PRICE_KEY]} 🪙] ➕ {TRAININGS["1"][DAMAGE_KEY]} единиц 🗡️')
    print(f'{NUMERATION[2]} [Тренировка подавления урона ➤ {TRAININGS["2"][PRICE_KEY]} 🪙] ➕ {TRAININGS["2"][DEFENSE_KEY]} единиц 🛡️')
    print(f'{NUMERATION[3]} [Контроль чакры ➤ {TRAININGS["3"][PRICE_KEY]} 🪙] ➕ {TRAININGS["3"][MANA_KEY]} единиц 💧')
    print(f'{NUMERATION[4]} [Тренировка тела ➤ {TRAININGS["4"][PRICE_KEY]} 🪙] ➕ {TRAININGS["4"][HEALTH_KEY]} единиц ❤️')
    print()

    training = input(PROMPT)
    print()

    if training in TRAININGS.keys():
        cost = TRAININGS[training][PRICE_KEY]
        if character.money < cost:
            print(f'{HEADER} Вы нищий, так как вы нищий...')
        else:
            if training == '1':
                character.spend_money(cost)
                character.attack += TRAININGS['1'][DAMAGE_KEY]

                print(f'{ATTENTION} Вы потратили {cost} 🪙 и получили {TRAININGS["1"][DAMAGE_KEY]} единиц 🗡️')
                print(f'{ATTENTION} Ваша 🗡️ теперь: {character.attack} единиц')
            elif training == '2':
                character.spend_money(cost)
                character.defense += TRAININGS['2'][DEFENSE_KEY]

                print(f'{ATTENTION} Вы потратили {cost} 🪙 и получили {TRAININGS["2"][DEFENSE_KEY]} единиц 🛡️')
                print(f'{ATTENTION} Ваша 🛡️ теперь: {character.defense} единиц')
            elif training == '3':
                character.spend_money(cost)
                character.mp += TRAININGS['3'][MANA_KEY]

                print(f'{ATTENTION} Вы потратили {cost} 🪙 и получили {TRAININGS["3"][MANA_KEY]} единиц 💧')
                print(f'{ATTENTION} Ваша 💧 теперь: {character.mp} единиц')
            elif training == '4':
                character.spend_money(cost)
                character.hp += TRAININGS['4'][HEALTH_KEY]

                print(f'{ATTENTION} Вы потратили {cost} 🪙 и получили {TRAININGS["4"][HEALTH_KEY]} единиц ❤️')
                print(f'{ATTENTION} Ваше ❤️ теперь: {character.hp} единиц')
    else:
        lost_hp = randint(10, 30)
        character.take_damage(lost_hp)

        lost_money = randint(10, 100)
        character.spend_money(lost_money)

        print(f'{HEADER} Занимающимся в залах злым качкам не понравилось ваше поведение'
              f'и вам прописали двойной апперкот и после вашего падения у вас выпали 🪙')
        print(f'[❗] Вы потеряли {lost_hp} единиц ❤️ и {lost_money} 🪙')

        if randint(1, 1) == 1 and character.money < 0:
            print(f'{HEADER} Так же тренер подал на вас в суд деревни за неправомерное поведение' 
                  f'и суд выставил на вас долг в размере {-lost_money} ')
