def full_print(data):
    for k, v in data.items():
        print(k, '{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}'.format(**v))
def del_cont(inp, data):
    if inp[0] not in data.keys():
        raise KeyboardInterrupt
    else:
        data.pop(inp[0], 'не найдено')
    return data
def add_cont(list, data):
    x = str(list[0])
    if x in data.keys():
        raise KeyboardInterrupt
    else:
        temp = {}
        numb = []
        temp['Фамилия'] = list[1]
        temp['Имя'] = list[2]
        temp['Возраст'] = int(list[3])
        for i in list[4:]:
            numb.append(int(i))
        temp['Телефон'] = numb
        data[x] = temp
    return data