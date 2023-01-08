import datetime

default_hours = {
    # hours with min == 0 or min >= 45
    1: 'один',
    2: 'два',
    3: 'три',
    4: 'четыре',
    5: 'пять',
    6: 'шесть',
    7: 'семь',
    8: 'восемь',
    9: 'девять',
    10: 'десять',
    11: 'одинадцать',
    12: 'двенадцать'
}

custom_hours = {
    # hours with min == 0 or min < 30 or min == 30 or min > 30 and min < 45
    1: 'первого',
    2: 'второго',
    3: 'третьего',
    4: 'четвертого',
    5: 'пятого',
    6: 'шестого',
    7: 'седьмого',
    8: 'восьмого',
    9: 'девятого',
    10: 'десятого',
    11: 'одиннадцатого',
    12: 'двеннадцаго'
}

default_minutes = {
    # minutes not min == 30 or not min >= 45
    1: 'одна минута',
    2: 'две минута',
    3: 'три минута',
    4: 'четыре минута',
    5: 'пять минут',
    6: 'шесть минут',
    7: 'семь минут',
    8: 'восем минут',
    9: 'девять минут',
    10: 'десять минут',
    11: 'одинадцать минут',
    12: 'двенадцать минут',
    13: 'тринадцать минут',
    14: 'четырнадцать минут',
    15: 'пятнадцать минут',
    16: 'шестнадцать минут',
    17: 'семнадцать минут',
    18: 'восемнадцать минут',
    19: 'деветнадцать минут',
    20: 'двадцать минут',
    21: 'двадцать одна минута',
    22: 'двадцать две минуты',
    23: 'двадцать три минуты',
    24: 'двадцать четыре минуты',
    25: 'двадцать пять минут',
    26: 'двадцать шесть минут',
    27: 'двадцать семь минут',
    28: 'двадцать восем минут',
    29: 'двадцать девять минут',
    31: 'тридцать одна минута',
    32: 'тридцать две минуты',
    33: 'тридцать три минуты',
    34: 'тридцать четыре минуты',
    35: 'тридцать пять минут',
    36: 'тридцать шесть минут',
    37: 'тридцать семь минут',
    38: 'тридцать восем минут',
    39: 'тридцать девять минут',
    40: 'сорок минут',
    41: 'сорок одна минута',
    42: 'сорок две минуты',
    43: 'сорок три минуты',
    44: 'сорок четыре минуты'
}

custom_minutes = {
    # minutes min == 30 or min >= 45
    30: 'половина',
    45: 'Без пятнадцати минут',
    46: 'Без четырнадцати минут',
    47: 'Без тринадцати минут',
    48: 'Без двенадцати минут',
    49: 'Без одинадцати минут',
    50: 'Без десяти минут',
    51: 'Без девяти минут',
    52: 'Без восьми минут',
    53: 'Без семи минут',
    54: 'Без шести минут',
    55: 'Без пяти минут',
    56: 'Без четырех минут',
    57: 'Без трех минут',
    58: 'Без двух минут',
    59: 'Без одной минуты'
}


# parser
def parser(src: list):
    # if parser break
    final_string = 'error'

    # parsing
    if src[1] == 0 and 2 <= src[0] <= 4:
        final_string = str(default_hours.get(src[0])) + 'часа ровно'
    elif src[1] == 0 and src[0] == 1:
        final_string = 'час ровно'
    elif src[1] == 0 and src[0] >= 5:
        final_string = str(default_hours.get(src[0])) + 'часов ровно'
    elif 0 < src[1] < 30:
        final_string = str(default_minutes.get(src[1])) + ' ' + str(custom_hours.get(src[0]))
    elif src[1] == 30:
        final_string = str(custom_minutes.get([src[1]])) + ' ' + str(custom_hours.get([src[0]]))
    elif 30 < src[1] < 45:
        final_string = str(default_minutes.get(src[1])) + ' ' + str(custom_hours.get([src[0]]))
    elif src[1] >= 45:
        final_string = str(custom_minutes.get(src[1])) + ' ' + str(default_hours.get(src[0] + 1))
    return final_string


# user_choise
user_choise = input('Добрый день!\nЧто необходимо ? Введите:\n'
                    'текстовый вывод текущего времени/текстовый вывод времени, введённого с консоли\n')

# 1 server time
if user_choise == 'текстовый вывод текущего времени':
    # if parser break
    source = 'error'

    if datetime.datetime.now().hour <= 12:
        source = [datetime.datetime.now().hour, datetime.datetime.now().minute]

    elif 12 < datetime.datetime.now().hour <= 24:
        source = [datetime.datetime.now().hour - 12, datetime.datetime.now().minute]

    # result
    print(parser(source))


# 2 user choise
elif user_choise == 'текстовый вывод времени, введённого с консоли':
    source_user = input('Введите, пожалуйста данные в формате:\nhh:mm\n')

    if int(source_user.split(':')[0]) <= 12:
        list_src = [int(source_user.split(':')[0]), int(source_user.split(':')[1])]
        print(parser(list_src))

    elif 12 < int(source_user.split(':')[0]) <= 24:
        list_src = [int(source_user.split(':')[0]) - 12, int(source_user.split(':')[1])]
        print(parser(list_src))
