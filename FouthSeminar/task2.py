'''Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
элементов исходной последовательности.
'''

list = [1, 4, 6, 10, 45, 1, 4, 52, 6, 7, 74, 10, 1, 354, 52, 10, 74]
def ChoiceNumber(list):
    for i in range(len(list)-2, -1, -1):
        if list[i] in list[i+1:]: list.pop(i)
    print (list)

ChoiceNumber(list)

