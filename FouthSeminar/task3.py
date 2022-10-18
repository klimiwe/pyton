# задача 3. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint


k = int(input('Введите натуральную степень k: '))
def rando():
    num = randint(0,3)
    return num

def mnogochlen(diff):
    result = ''
    if diff == 1: result += f'{randint(1,100)}*x'
    if diff <=0: 
        result = 'Степень должна быть больше нуля'
        print(result)
        return       
    if diff > 1: 
        result = f'{randint(1,100)}*x^{diff}'
        diff -= 1
        while diff > 1:
            rand = rando()
            if rand == 0: diff -= 1
            else:
                result += f' + {rand}*x^{diff}'
                diff -= 1
        if diff == 1: 
            rand = rando()
            if rand == 0: diff -= 1
            else:
                result += f' + {randint(1,100)}*x'
    rand = rando()
    if rand == 0: result = result + ' = 0'
    else: result = result + f' + {rand} = 0'
    print(result)

mnogochlen(k)