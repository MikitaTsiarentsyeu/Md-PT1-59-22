minutes = ("минут", "минуты", "минута")
hours = ("часов", "часа")

d = {
    1:("одна", "одной", "час", "первого"),
    2:("две", "двух", "два", "второго"),
    3:("три", "трёх", "три", "третьего"),
    12:("двенадцать", "двенадцати", "двенадцать", "двенадцатого"),
    13:("две", "двух"), #till 19
    20:("двадцать", "двадцати"),
    30:("тридцать", "тридцати"),
}

d[3][0]

import datetime

mode = input("Choose your mode: c/y")

if mode == 'c':
    time_value = datetime.datetime.now
    # minutes, hours
else:
    time_value = input("input your value in hh:mm format:")
    # minutes, hours


# if minutes == 0:
#     d[0][0]