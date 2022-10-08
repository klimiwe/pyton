'''Реализуйте алгоритм перемешивания списка. Список размерностью 
10 задается случайными целыми числами, выводится на экран, затем перемешивается, 
опять выводится на экран. SHUFFLE нельзя юзать!'''

import random
def get_rand_list(num, min, max):
    list = [num]
    for i in range(num - 1):
        number = random.randint(min, max)
        list.append(number)
    return list
OrigList = get_rand_list(10, 0, 10)
print(OrigList)

def shuffle_list(input_list):
    shuf_list = []
    for i in range(len(input_list)):
        num = random.choice(input_list)
        shuf_list.append(num)
        input_list.remove(num)
    return shuf_list

print(shuffle_list(OrigList))