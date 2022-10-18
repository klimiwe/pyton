# задача 4. Задайте два числа. 
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

def simple_multiplier(num):
    list = []
    for i in range(2, num+1):
        while num%i == 0:
            list.append(i)
            num /= i
    return list

print(simple_multiplier(num1))
print(simple_multiplier(num2))

def min_total_multultiplier(a,b):
    list1 = simple_multiplier(a)
    list2 = simple_multiplier(b)
    if len(list1) > len(list2):
        list1 = simple_multiplier(b)
        list2 = simple_multiplier(a)
    temp_list = list2
    res = 1
    for i in range(len(list1)):
        if list1[i] in temp_list: 
            temp_list.remove(list1[i])
    temp_list.extend(list1)
    for item in temp_list: res *= item
    print(res)
    

min_total_multultiplier(num1, num2)