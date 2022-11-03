# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from filecmp import *


file = open('/Users/klimbondarenko/Desktop/Обучение/python/Hometask /FifthSeminar/task2/encode_vvod.txt','r')
startString = file.read()
print(startString)
file.close()

def encode(string):
    en_string = ''
    count = 1
    for i in range(len(string)):
        if i+1 < len(string) and string[i+1] == string[i]:
            count += 1
        else:
            en_string += str(count) + string[i]
            count = 1
    return en_string

print (encode(startString))
endFile = open('/Users/klimbondarenko/Desktop/Обучение/python/Hometask /FifthSeminar/task2/encode_vivod.txt','w')
endFile.write (encode(startString))
endFile.close()

