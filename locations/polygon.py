from random import randint
from misc.consts import *
from time import sleep

TRAININGS = {
    '1': {PRICE_KEY: 110, DAMAGE_KEY: 1, NAME: 'Спарринг на мечах'},
    '2': {PRICE_KEY: 135, DEFENSE_KEY: 3, NAME: 'Подавление урона'},
    '3': {PRICE_KEY: 120, MANA_KEY: 4, NAME: 'Контроль маны'},
    '4': {PRICE_KEY: 200, HEALTH_KEY: 2, NAME: 'Тренировка тела'}
}


def polygon(character: callable):
    """One of three locations
    :param character: It used to transmit character's params"""
    while True:
        input(f'{PRESS_ENTER} Нажмите Enter для продолжения...')
        print(CLEAR_SCREEN)

        print(f'{HEADER} Вы оказываетесь на большом открытом пространстве, где каждый метр занят тренирующимися людьми.')
        sleep(3)
        print(f'{HEADER} К вам подходит человек и представляется тренером, он дает вам выбор:')
        sleep(3)
        print()

        print(f'{TEMP_NUMERATION[0]} Выход из локации')
        sleep(0.35)
        for key, value in TRAININGS.items():
            print(f"{TEMP_NUMERATION[int(key)]} "
                  f"{value.get(NAME)} >>> "
                  f"{value.get(PRICE_KEY, 0)} {MONEY} "
                  f"(➕ {value.get(DAMAGE_KEY, 0)} {ATTACK}|"
                  f"➕ {value.get(DEFENSE_KEY, 0)} {DEFENSE}|"
                  f"➕ {value.get(MANA_KEY, 0)} {MANA}|"
                  f"➕ {value.get(HEALTH_KEY, 0)} {HEART})")
            sleep(0.35)

        print()

        training = input(PROMPT)
        print()

        if training == '0':
            return

        elif training in TRAININGS.keys():
            cost = TRAININGS[training][PRICE_KEY]
            if character.money < cost:
                print(f'{HEADER} Вы нищий, так как вы нищий...')
                sleep(3)
            else:
                if training == '1':
                    character.spend_money(cost)
                    got_attack = TRAININGS.get('1').get(DAMAGE_KEY)
                    character.get_attack(got_attack)

                    print(f'{GAME_ATTENTION} Вы потратили {cost} {MONEY} и получили {got_attack} {ATTACK}')
                    sleep(3)
                    print(f'{GAME_ATTENTION} Ваша {ATTACK} теперь: {character.attack}')
                    sleep(3)
                elif training == '2':
                    character.spend_money(cost)
                    got_defense = TRAININGS.get('2').get(DEFENSE_KEY)
                    character.get_defense(got_defense)

                    print(f'{GAME_ATTENTION} Вы потратили {cost} {MONEY} и получили {got_defense} {DEFENSE}')
                    sleep(3)
                    print(f'{GAME_ATTENTION} Ваша {DEFENSE} теперь: {character.defense}')
                    sleep(3)
                elif training == '3':
                    character.spend_money(cost)
                    got_mp = TRAININGS.get('3').get(MANA_KEY)
                    character.get_mp(got_mp)

                    print(f'{GAME_ATTENTION} Вы потратили {cost} {MONEY} и получили {got_mp} {MANA}')
                    sleep(3)
                    print(f'{GAME_ATTENTION} Ваша {MANA} теперь: {character.mp}')
                    sleep(3)
                elif training == '4':
                    character.spend_money(cost)
                    got_hp = TRAININGS.get('4').get(HEALTH_KEY)
                    character.get_hp(got_hp)

                    print(f'{GAME_ATTENTION} Вы потратили {cost} {MONEY} и получили {got_hp} {HEART}')
                    sleep(3)
                    print(f'{GAME_ATTENTION} Ваше {HEART} теперь: {character.hp} ')
                    sleep(3)
        else:
            lost_hp = randint(10, 30)
            character.get_damage(lost_hp)

            print(f'{HEADER} Занимающимся в залах злым качкам не понравилось ваше поведение...')
            print()
            sleep(3)
            print(f'{HEADER} Вам прописали двойной апперкот и дали по печени')
            sleep(3)
            print(f'{GAME_ATTENTION} Вы потеряли {lost_hp} {HEART}')
            sleep(3)
            if randint(1, 3) == 1 and character.show_money() < 0:
                lost_money = randint(10, 100)
                character.spend_money(lost_money)

                print(f'{HEADER} Так же тренер подал на вас в суд деревни за неправомерное поведение')
                sleep(3)
                print(f'{HEADER} Суд выставил на вас долг в размере {-lost_money} ')
                sleep(3)
        if not character.show_money() < 0:
            print(f'{HEADER} Хотите продолжить тренироваться?')
            print()
            print(f'{TEMP_NUMERATION[1]} Да')
            print(f'{TEMP_NUMERATION[2]} Нет')
            print()

            continued = input(f'{PROMPT}')

            if continued == '1':
                pass
            elif continued == '2':
                return
            else:
                print(f"Shapilov {SHAPILOV * 3}")
                return
