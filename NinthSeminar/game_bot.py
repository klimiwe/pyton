import telebot

size = 3
matrix = []
player = 'X'
step_count = 0
def hod_X(list):
    global matrix
    matrix[int(list[0])-1][int(list[1])-1] = 'X'
def hod_0(list):
    global matrix
    matrix[int(list[0])-1][int(list[1])-1] = '0'
def print_field(text):
    bot.send_message(text.chat.id, f"{'   '.join(matrix[0])}\n{'   '.join(matrix[1])}\n{'   '.join(matrix[2])}")
def res():
    count = 0
    global matrix
    for j in range(size):
        count = 0
        for i in range(size-1):
            if matrix[i][j] == matrix[i+1][j] and matrix[i][j] != '-':
                count += 1
        if count == 2:
            return True
    for i in range(size):
        if matrix[i].count(matrix[i][j]) == len(matrix[i]) and matrix[i][j] != '-':
            return True
    count = 0
    for i in range(size-1):
        if matrix[i][i] == matrix[i+1][i+1] and matrix[i][i] != '-':
            count += 1
    if count == 2:
        return True
    count = 0
    for i in range(size-1):
        if matrix[i][-1-i] == matrix[i+1][-2-i] and matrix[i][-1-i] != '-':
            count += 1
    if count == 2:
        return True

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Это игра в крестики-нолики(PvP)\nПосмотрите правила ввода, набрав команду "/help"')
    bot.send_message(message.chat.id, 'Начать игру?\n("да" или "нет")')

@bot.message_handler(commands=['help'])
def helper(message):
    bot.send_message(message.chat.id, 'Ввод координат для крестика или нолика через пробел')
    bot.send_message(message.chat.id, 'Например: для первой строки и второго столбца введите "1 2"')

@bot.message_handler(content_types='text')
def game(message):
    global matrix
    global player
    global step_count
    if 'да' in message.text:
        matrix = [["-" for j in range(size)] for i in range(size)]
        bot.send_message(message.chat.id,'Вот наше поле:')
        print_field(message)
        bot.send_message(message.chat.id,'Введите координаты для крестика')
    elif 'нет' in message.text:
        bot.send_message(message.chat.id,'До новых встреч!')
        exit()
    else:
        if player == 'X':
            hod = message.text.split()
            try:
                if matrix[int(hod[0])-1][int(hod[1])-1] != '-':
                    bot.send_message(message.chat.id, 'Эта ячейка занята')
                else:
                    hod_X(hod)
                    player = '0'
                    print_field(message)
                    step_count += 1
                    if res() == True:
                        bot.send_message(message.chat.id,'Поздравляем! Крестики выиграли')
                    elif step_count == size*size:
                        bot.send_message(message.chat.id, 'Увы, НИЧЬЯ(((\nДо новых встреч!')
                    else:
                        bot.send_message(message.chat.id,'Введите координаты для нолика')
            except:
                bot.send_message(message.chat.id, 'Неправильный ввод')
        else:
            hod = message.text.split()
            try:
                if matrix[int(hod[0])-1][int(hod[1])-1] != '-':
                    bot.send_message(message.chat.id, 'Эта ячейка занята')
                else:
                    hod_0(hod)
                    player = 'X'
                    print_field(message)
                    step_count += 1
                    if res() == True:
                        bot.send_message(message.chat.id,'Поздравляем! Нолики выиграли')
                    elif step_count == size*size:
                        bot.send_message(message.chat.id, 'Увы, НИЧЬЯ(((\nДо новых встреч!')
                    else:
                        bot.send_message(message.chat.id,'Введите координаты для крестика')
            except:
                bot.send_message(message.chat.id, 'Неправильный ввод')

bot.polling()