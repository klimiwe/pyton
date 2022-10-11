'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
*Пример:*

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

list1 = [1.1, 1.2, 3.1, 5, 10.01]

def ne_znat_kak_nazvat(list):
    res = 0
    max_double = list[0]%1
    min_double = list[0]%1
    for i in range(len(list)):
        if list[i]%1 > max_double:
            max_double = list[i]%1
        if list[i]%1< min_double:
            min_double = list[i]%1
    res = max_double - min_double
    return res
   


print(ne_znat_kak_nazvat(list1))