"""
Реализовать:
1.текстовый вывод текущего времени
2.текстовый вывод времени, введённого с консоли (пользователь должен вводить данные в формате hh:mm).
Дать пользователю возможность выбрать режим работы программы, время выводить числительными на русском языке.

Для получения текущего времени использовать модуль datetime.

min == 0: такое-то значение часа ровно (15:00 - три часа ровно)
min < 30: столько-то минут следующего часа (19:12 - двенадцать минут восьмого)
min == 30: половина такого-то (15:30 - половина четвёртого)
min > 30 and min < 45 столько-то минут следующего часа (12:38 - тридцать восемь минут первого)
min >= 45 без min такого-то (08:54 - без шести минут девять)
"""
import datetime


value = input("Do you want to type the time value yourself (y/n)? ")
if value == 'y' or value == 'Y':
    while True:
        str_time = input("Please enter your value in the hh:mm format\n")
        if len(str_time) != 5 or str_time[2] != ':': 
            print("The data is incorrect format!")
            continue

        hh = str_time[0:2]
        mm = str_time[3:]

        if hh.isnumeric() == False: 
            print("Entered hours must be numebrs!")
            continue

        if mm.isnumeric() == False: 
            print("Entered hours must be numbers!")
            continue

        hh = int(hh)
        mm = int(mm)

        if hh < 0 or hh > 23: #if 0 > hh > 23: почему это не сработало?
            print("Entered hours out of range!")
            continue
            
        if mm < 0 or mm > 59: #if 0 > mm > 59: тоже почему-то не сработало
            print("Entered minutes out of range!")
            continue

        break
else:
    now = datetime.datetime.now()
    hh = now.hour
    mm = now.minute


if hh > 12:
    hh = hh - 12 # нормализуем часы во второй половине суток

hour = {}
hour[0] = ['ноль','первого']
hour[1] = ['один','второго']
hour[2] = ['два','третьего']
hour[3] = ['три','четвёртого']
hour[4] = ['четыре','пятого']
hour[5] = ['пять','шестого']
hour[6] = ['шесть','седьмого']
hour[7] = ['семь','восьмого']
hour[8] = ['восемь','девятого']
hour[9] = ['девять','десятого']
hour[10] = ['десять','одиннадцатого']
hour[11] = ['одиннадцать','двенадцатого']
hour[12] = ['двенадцать','первого']

minut = {}
minut[1] = ['одна','одной']
minut[2] = ['две','двух']
minut[3] = ['три','трёх']
minut[4] = ['четыре','четырёх']
minut[5] = ['пять','пяти']
minut[6] = ['шесть','шести']
minut[7] = ['семь','семи']
minut[8] = ['восемь','восьми']
minut[9] = ['девять','девяти']
minut[10] = ['десять','десяти']
minut[11] = ['одиннадцать','одиннадцати']
minut[12] = ['двенадцать','двенадцати']
minut[13] = ['тринадцать','тринадцати']
minut[14] = ['четырнадцать','четырнадцати']
minut[15] = ['пятнадцать','пятнадцати']
minut[16] = ['шестнадцать']
minut[17] = ['семнадцать']
minut[18] = ['восемнадцать']
minut[19] = ['девятнадцать']
minut[20] = ['двадцать']

chasov = ''
if hh == 1:
    chasov = 'час'
elif 1 < hh < 5:
    chasov = 'часа'
else:
    chasov = 'часов'

minutes = ''
if mm < 20:
    correct_mm = mm
else:
    correct_mm = mm % 10  # для минут больше 19, там работает правило первого десятка

if correct_mm == 1:
    minutes = 'минута'
elif 1 < correct_mm < 5:
    minutes = 'минуты'
else:
    minutes = 'минут'


if mm == 0:
    print(f"{hour[hh][0]} {chasov} ровно")
elif mm < 30:
    if mm < 21:
        print(f"{minut[mm][0]} {minutes} {hour[hh][1]}")
    else:
        print(f"двадцать {minut[mm-20][0]} {minutes} {hour[hh][1]}")
elif mm == 30:
    print(f"половина {hour[hh][1]}")
elif 30 < mm < 45:
    if mm < 40:
        print(f"тридцать {minut[mm-30][0]} {minutes} {hour[hh][1]}")
    elif mm == 40:
        print(f"сорок минут {hour[hh][1]}")
    else:
        print(f"сорок {minut[mm-40][0]} {minutes} {hour[hh][1]}")
else:
    print(f"без {minut[60-mm][1]} {'минуты' if (60-mm)==1 else 'минут'} {hour[hh+1][0]}")
