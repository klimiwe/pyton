import file_work as file
import operations as do
from user_select import *

print('Добро пожаловать в базу сотрудников!')
BAZA = file.load() # Загружаем файл базы данных
user = user_sel() # Выбираем уровень доступа пользователя
x = user_options(user) # Тут варианты действий в зависимости от уровня доступа
if x == 1: do.full_print(BAZA) # Полный вывод списком
if x == 2: do.find_cont(BAZA)  # Вывод поиска по имени или фамилии списком
if x == 3:                     # Добавление контакта
    BAZA = do.add_cont(BAZA)
    file.save(BAZA)            # сохранение в файл
    print('Контакт добавлен')
if x == 4:                     # Удаление контакта
    BAZA = do.del_cont(BAZA)
    file.save(BAZA)            # сохранение в файл
    print('Контакт удален')
print('До свидания!')