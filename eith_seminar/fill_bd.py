import random
import json

f_list = ['Иванов', 'Петров', 'Львов', 'Маркс', 'Федоров', 
        'Ильин', 'Светлов', 'Захаров', 'Григорьев', 'Куц', 'Сидоров', 'Малышев']
n_list = ['Василий', 'Петр', 'Алексей', 'Руслан', 'Григорий', 'Илья', 'Максим', 'Артем']
slov = {}
def fill_slov():
    for i in range(1,31):
        temp = {}
        temp['Фамилия'] = random.choice(f_list)
        temp['Имя'] = random.choice(n_list)
        temp['Возраст'] = random.randint(19, 42)
        x = random.randint(200000, 900000)
        temp['Телефон'] = [x]
        slov[i] = temp
fill_slov()