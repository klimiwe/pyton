#Напишите программу для. проверки истинности утверждения 
#¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int (input('введите число x'))
y = int (input('введите число y'))
z = int (input('введите число z'))

if -(x  or y or z) == -x or -y or -z:
    print ('выражение истинно')
else:
    print ('выражение ложно')