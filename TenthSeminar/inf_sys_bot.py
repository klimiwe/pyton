import telebot
import file_work as f
import operations as do

BD = {}
API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)
def find_name(search, data,mes):
    temp = False
    for k, v in data.items():
        if v['Имя'] == search[0]:
            bot.send_message(mes.chat.id, f'{k} {"{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}".format(**v)}')
            temp = True
    if temp == False:
        bot.send_message(mes.chat.id,'Совпадений не найдено')
def find_surname(search, data,mes):
    temp = False
    for k, v in data.items():
        if v['Фамилия'] == search[0]:
            bot.send_message(mes.chat.id, f'{k} {"{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}".format(**v)}')
            temp = True
    if temp == False:
        bot.send_message(mes.chat.id,'Совпадений не найдено')
def find_age(search, data,mes):
    temp = False
    for k, v in data.items():
        if v['Возраст'] >= int(search[0]) and v['Возраст'] <= int(search[1]):
            bot.send_message(mes.chat.id, f'{k} {"{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}".format(**v)}')
            temp = True
    if temp == False:
        bot.send_message(mes.chat.id,'Совпадений не найдено')

@bot.message_handler(commands=['start'])
def start(message):
    global BD
    try:
        BD = f.load()
        bot.send_message(message.chat.id, 'База данных работников офиса успешно загружена')
        bot.send_message(message.chat.id, 'Список операций через "/help"')
    except:
        bot.send_message(message.chat.id, 'База данных не найдена')
@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'Список команд для работы с базой данных(в кавычках примеры):')
    bot.send_message(message.chat.id,'"/all" - показать всю базу')
    bot.send_message(message.chat.id,'"/findName Александр" - поиск по имени')
    bot.send_message(message.chat.id,'"/findSurname Иванов" - поиск по фамилии')
    bot.send_message(message.chat.id,'"/findAge 20 30" - поиск по возрасту (от 20 до 30 лет)')
    bot.send_message(message.chat.id,'"/findID 10" - поиск по номеру(10) учетной записи')
    bot.send_message(message.chat.id,'"/del 10 - удаление учетной записи номер 10')
    bot.send_message(message.chat.id,'"/add 1 Илья Сидоров 47 456734 368794 - добавление записи\nгде 47 - возраст, далее номера телефонов')
@bot.message_handler(commands=['all'])
def print_all(message):
    for i,j in BD.items():
        bot.send_message(message.chat.id, f'{i} {"{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}".format(**j)}')
@bot.message_handler(commands=['findName'])
def find_N(message):
    name = message.text.split()[1:]
    find_name(name, BD, message)
@bot.message_handler(commands=['findSurname'])
def find_S(message):
    surname = message.text.split()[1:]
    find_surname(surname, BD, message)
@bot.message_handler(commands=['findAge'])
def find_A(message):
    age = message.text.split()[1:]
    find_age(age, BD, message)
@bot.message_handler(commands=['findID'])
def find_ID(message):
    ID = message.text.split()[1]
    try:
        bot.send_message(message.chat.id, f'{"{Фамилия} {Имя} Возраст {Возраст} Телефон {Телефон}".format(**BD[ID])}')
    except:
        bot.send_message(message.chat.id, 'Совпадений не найдено')
@bot.message_handler(commands=['add'])
def add_C(message):
    global BD
    cont = message.text.split()[1:]
    try:
        BD = do.add_cont(cont, BD)
        f.save(BD)
        bot.send_message(message.chat.id, 'Контакт успешно добавлен в базу')
    except:
        bot.send_message(message.chat.id, 'Такой ID уже существует')
@bot.message_handler(commands=['del'])
def del_C(message):
    global BD
    ID = message.text.split()[1:]
    try:
        BD = do.del_cont(ID, BD)
        f.save(BD)
        bot.send_message(message.chat.id, 'Контакт успешно удалён из базы')
    except:
        bot.send_message(message.chat.id, 'Такого ID не существует')

bot.polling()