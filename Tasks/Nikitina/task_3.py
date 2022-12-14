import datetime
minutes = ("минут", "минуты", "минута")
hours = ("часов", "часа")
d = {
    1:("одна", "одной", "час", "первого"),
    2:("две", "двух", "два", "второго"),
    3:("три", "трёх", "три", "третьего"),
    4:("четыре","четырёх","четыре", "четвертого"),
    5:("пять","пяти","пять", "пятого"),
    6:("шесть","шести","шесть", "шестого"),
    7:("семь","семи","семь", "седьмого"),
    8:("восемь","восьми","восемь", "восьмого"),
    9:("девять","девяти","девять", "девятого"),
    10:("десять","десяти","десять", "десятого"),
    11:("одинадцать", "одинадцати", "одинадцать", "одинадцатого"),
    12:("двенадцать", "двенадцати", "двенадцать", "двенадцатого"),
    13:("тринадцать", "тринадцати", "тринадцать", "тринадцатого"),
    14:("четырнадцать", "четырнадцати", "четырнадцать", "четырнадцатого"),
    15:("пятнадцать", "пятнадцати", "пятнадцать", "пятнадцатого"),
    16:("шестнадцать", "шестнадцати", "шестнадцать", "шестнадцатого"),
    17:("семнадцать", "семнадцати", "семнадцать", "семнадцатого"),
    18:("восемнадцать", "восемнадцати", "восемнадцать", "восемнадцатого"),
    19:("девятнадцать", "девятнадцати", "девятнадцать", "девятнадцатого"),
    20:("двадцать", "двадцати"),
    21:("двадцать одна","двадцать одной"),
    22:("двадцать два ", "двадцать две "),
    23:("двадцать три", "двадцать три"),
    24:("двадцать четыре"),
    25:("двадцать пять"),
    26:("двадцать шесть"),
    27:("двадцать семь"),
    28:("двадцать восемь"),
    29:("двадцать девять"),
    30:("тридцать", "тридцати"),
    31:("тридцать одна"),
    32:("тридцать две"),
    33:("тридцать три"),
    34:("тридцать четыре"),
    35:("тридцать пять"),
    36:("тридцать шесть"),
    37:("тридцать семь"),
    38:("тридцать восемь"),
    39:("тридцать девять"),
    40:("сорок","сорока"),
    41:("сорок одна"),
    42:("сорок две "),
    43:("сорок три"),
    44:("сорок четыре"),
}
val = input("Do you want to type the time value yourself  (y/n)?\n")
if val == 'n':
    dat = datetime.datetime.now()
    dat = dat.strftime("%H:%M")
    print(dat)
    time = (dat.split(':'))
    hour, minute = int(time[0]), int(time[1])
else:
    dat = input('Please enter your value in the hh:mm format\n')

# Переводим время в список
time = (dat.split(':'))
# Проверяем правильность ввода
if time[0].isdigit() == True and time[1].isdigit() == True and 0 <= int(time[0]) < 24 and 0 <= int(time[1]) < 60:

    hour, minute = int(time[0]), int(time[1])
    if minute == 0:
        if hour >= 2 and hour <=4 and hour >= 22 and hour <=23 and hour >= 12 and hour <=14 :
            print(d[hour][0], hours[1] , "ровно", end='.')
        else:
            print(d[hour][0], hours[0] , "ровно", end='.')
        
    elif 0 < minute < 30:
        if 1 < minute < 5 and 11 < minute < 15 and 21 < minute < 25:
            print('Ваше время', d[minute][0], minutes[1], d[(hour+1)][3] , end='.')
        elif minute == 11 and minute == 21:
            print('Ваше время', d[minute][0], minutes[2], d[(hour+1)][3] , end='.')
        else:
            print('Ваше время', d[minute][0], minutes[0], d[(hour+1)][3] , end='.')
    elif minute == 30:
        print('Ваше время половина', d[(hour+1)][3] , end='.')
    elif 30 < minute < 45:
        if 31 < minute < 35:
            print('Ваше время', d[minute][0], minutes[1], d[(hour+1)][3] , end='.')
        elif minute == 31 and minute == 41:
            print('Ваше время', d[minute][0], minutes[2], d[(hour+1)][3] , end='.')
        else:
            print('Ваше время', d[minute][0], minutes[0], d[(hour+1)][3] , end='.')

    elif minute >= 45:
        if hour >= 12:
            # перевод часов в p.m.
            print('Ваше время без', d[(60-minute)][1],minutes[0], d[((hour-12)+1)][3], end='.')
        else:
            print('Ваше время без', d[(60-minute)][1],minutes[0], d[hour+1][3], end='.')
else:
    print('Пожалуйста, проверьте правильность введенных данных.')


