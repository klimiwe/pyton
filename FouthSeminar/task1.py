'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.'''

N = int (input('введите число'))

def factor(N):
    List= []
    for i in range (2, N+1):
        if N%i==0:
            List.append(i)
            N /= i
    return List

print (factor(N))