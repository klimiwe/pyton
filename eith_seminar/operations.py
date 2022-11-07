def full_print(data):
    for k, v in data.items():
        print(k, '{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}'.format(**v))

def find_name(search, data):
    temp = False
    for k, v in data.items():
        if v['Имя'] == search:
            print(k, '{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}'.format(**v))
            temp = True
    if temp == False: print('Совпадений не найдено!') 
def find_surname(search, data):
    temp = False
    for k, v in data.items():
        if v['Фамилия'] == search:
            print(k, '{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}'.format(**v))
            temp = True
    if temp == False: print('Совпадений не найдено!')
def find_cont(data):
    print('1 Поиск по фамилии\n2 Поиск по имени')
    x = int(input('Введите 1 или 2: '))
    if x == 1: 
        family = input('Введите фамилию: ')
        find_surname(family, data)
    if x == 2:
        name = input('Введите имя: ')
        find_name(name, data)

def del_cont(data):
    x = str(input('Введите номер сотрудника для удаления: '))
    data.pop(x, 'не найдено')
    return data
def add_cont(data):
    x = str(input('Введите номер для сотрудника: '))
    if x in data.keys():
        print('Такой номер уже существует')
        add_cont(data)
    else:
        temp = {}
        temp['Фамилия'] = input('Введите фамилию: ')
        temp['Имя'] = input('Введите имя: ')
        temp['Возраст'] = input('Введите возраст: ')
        y = int(input('Введите телефон: '))
        temp['Телефон'] = [y]
        data[x] = temp
    return data