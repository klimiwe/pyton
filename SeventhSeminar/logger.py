from datetime import datetime as dtnow

def log_true(string, res):
    with open('log.txt', 'a') as data:
        time = dtnow.now().strftime('%d.%m.%y %H:%M')
        data.write(f'{time}: {string} = {res}\n')

def log_error(string):
    time = dtnow.now().strftime('%d.%m.%y %H:%M')
    with open('log.txt', 'a') as data:
        data.write(f'{time}: {string} Error\n')