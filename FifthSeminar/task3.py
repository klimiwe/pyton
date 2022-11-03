# задача 3. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". Функции FIND и COUNT юзать нельзя.

stroka = 'абвздесь текст, абвкоторый абв не.? содержащий rабвке! этих символов'
print(stroka)

# вариант 1

# stroka = stroka.replace(" ", "*")

# def add_split2(text):
#     syntax = [' ', ',', '.', '!', '?', '*']
#     for arg in syntax:
#         text = text.replace(arg, f' {arg}')
#     return text

# def del_words(inp):
#     string = ''
#     sym = 'абв'
#     args = inp.split()
#     for arg in args:
#         if sym not in arg:
#             string += arg
#     return string

# res_stroka = del_words(add_split2(stroka))
# print(res_stroka.replace("*", " "))

# Вариант 2

list = [' ',',', '.', '!', '?', '*']

def words_with(symbols, text):
    global list
    words = []
    min_i = 0
    max_i = 0
    j = 0
    if symbols not in text: 
        return text
    else:
        for i in range(len(text)):
            if symbols in text[j:i]:
                for k in range(i-1, j-1, -1):
                    if text[k] not in list:
                        min_i = k
                    else: 
                        break
                if text[i] not in list:
                    max_i = i
                else:
                    max_i = i-1
                    j = i
                    words.append(text[min_i: max_i+1])
    words.sort(key=len, reverse=True)
    print(words)                  
    return words

res_stroka = words_with('абв', stroka)


def delete_words():
    global res_stroka
    global stroka
    for elem in res_stroka:
        stroka = stroka.replace(elem, '')

delete_words()
print(stroka)