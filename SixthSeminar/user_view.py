def get_string():
    return input('Введите выражение: ')

def result_view(res, text):
    print(f'{text} = {res}')

def error():
    print('Ошибка ввода!')