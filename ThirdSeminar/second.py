'''Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*Пример:*

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]'''

firstNumbers = [2, 3, 4, 5, 6]
secondNumbers = [2, 3, 5, 6]

def digit (numbers):
    result =[]
    for i in range(len(numbers)//2):
        digit = numbers[i]*numbers[-1-i]
        result.append(digit)
    if len(numbers)%2!=0:
        digit = numbers[len(numbers)//2]**2
        result.append(digit)
    return result



print(digit(firstNumbers))
print(digit(secondNumbers))



