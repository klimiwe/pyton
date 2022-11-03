# задача 1. Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
#                 Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
#                 Все конфеты оппонента достаются сделавшему последний ход. 
#                 Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint


konf = 2021
print(f'На столе лежат {konf} конфета. За один раз вы можете взять не более 28 конфет.')
print('Выиграет тот, кто сделает последний ход')

def input_pl():
    while True:
        try:
            num = int(input('введите количество конфет: '))
            if num<1 or num>28:
                print('Число должно быть от 1 до 28')
                continue
        except ValueError:
            print('Это не число!')
        else:
            return num
def game_PvP():
    global konf
    player_num = 1
    while konf > 28:
        if player_num == 1:
            print('Игрок1')
            konf -= input_pl()
            print(f'Остальсь {konf} конфет')
            player_num = 2
        elif player_num == 2:
            print('Игрок2')
            konf -= input_pl()
            print(f'Осталось {konf} конфет')
            player_num = 1
    print(f'Игрок {player_num} выиграл. Поздравляем!')
def game_PvС():
    global konf
    player_num = 1
    while konf > 28:
        if player_num == 1:
            print('Игрок1')
            konf -= input_pl()
            print(f'Остальсь {konf} конфет')
            player_num = 2
        elif player_num == 2:
            rand = randint(1, 29)
            print(f'Бот забирает {rand} конфет')
            konf -= rand
            print(f'Осталось {konf} конфет')
            player_num = 1
    if player_num == 1:
        print(f'Вы выиграли. Поздравляем!')
    else:
        print('Выиграл Бот, вы проиграли(')
game_PvP()
# game_PvС()