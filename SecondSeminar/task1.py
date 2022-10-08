'''Напишите программу, которая принимает на вход вещественное или целое 
число и показывает сумму его цифр. Через строку нельзя решать.
*Пример:*

- 6782 -> 23
- 0,56 -> 11'''

from curses.ascii import isdigit


number = input('введите число ')
sum = 0
for digit in number:
    if digit.isdigit():
        sum = sum +int(digit)

print (sum)