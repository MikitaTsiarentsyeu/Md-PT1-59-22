import datetime

minutes = ("минута", "минут", "минуты")    
hours = ("часов", "часа")
hours = {0:'двенадцать', 1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть',
        7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 12:'двенадцать'
}
minutes = {0:'ноль', 1:'одна', 2:'две', 3:'три', 4:'четыре', 5:'пять', 6:'шесть',
           7:'семь', 8:'восемь', 9:'девять', 10:'десять', 11:'одиннадцать', 12:'двенадцать',
           13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать', 16:'шестнадцать', 17:'семнадцать',
           18:'восемнадцать', 19:'девятнадцать', 20:'двадцать', 21:'двадцать одна', 22:'двадцать две',
           23:'двадцать три', 24:'двадцать четыре', 25:'двадцать пять', 26:'двадцать шесть', 27:'двадцать семь',
           28:'двадцать восемь', 29:'двадцать девять', 30:'половина', 31:'тридцать одна', 32:'тридцать две',
           33:'тридцать три', 34:'тридцать четыре', 35:'тридцать пять', 36:'тридцать шесть', 37:'тридцать семь',
           38:'тридцать восемь', 39:'тридцать девять', 40:'сорок', 41:'сорок одна', 42:'сорок две', 43:'сорок три',
           44:'сорок четыре'
}
minutes2 = {45:'пятнадцати', 46:'четырнадцати', 47:'тринадцати', 48:'двенадцати', 49:'одиннадцати', 50:'десяти',
            51:'девяти', 52:'восьми', 53:'семи', 54:'шести', 55:'пяти', 56:'четырех', 57:'трех', 58:'двух', 59:'одной'
}

hours2 = {0:'первого', 1:'второго', 2:'третьего', 3:'четвертого', 4:'пятого', 5:'шестого', 6:'седьмого', 7:'восьмого',
          8:'девятого', 9:'десятого', 10:'одиннадцатого', 11:'двенадцатого', 12:'первого', 13:'второго', 14:'третьего',
          15:'четвертого', 16:'пятого', 17:'шестого', 18:'седьмого', 19:'восьмого', 20:'девятого', 21:'десятого', 
          22:'одиннадцатого', 23:'двенадцатого'
}

datetime.datetime.now().time()

while True:
    time_value = input("Do you want to type the time value yourself (y/n)?\n")
    if time_value == 'y':
        print("The data is in the wrong format, the colon is missing.")
        if len(time_value) != 5:
            print("Invalid format number of characters does not match")
            if time_value[2] != ':' :
                print("The data is in the wrong format, the colon is missing.")
                continue

    parts = time_value.split(':')
    failsed = False
    for i, part in enumerate(parts):
        if not part.isnumeric():
            failsed = True
            break
        parts[i] = int(part)

    print(parts)    

    if failsed:
        print("The data is in the wrong format, you must only use digits") 
        continue   

    rparts = list (time_value) 
    hh = int (parts[0])
    mm = int (parts[1])   

    if mm == 0:
        if hh == 1:
            print (f"Ваше время {hours[hh]} час ровно")
        elif hh > 1 and hh < 5:
            print (f"Ваше время {hours[hh]} часа ровно")
        elif hh > 4:
            print (f"Ваше время {hours[hh]} часов ровно")
        if mm <= 30:
            if mm == 1:
                print (f"Ваше время {minutes[mm]} минута {hours2[hh]}" )
            elif mm > 1 and mm < 5:
                print (f"Ваше время {minutes[mm]} минуты {hours2[hh]}")
            elif mm > 4 and mm < 30:
                print (f"Ваше время {minutes[mm]} минут {hours2[hh]}")
            elif mm == 30:
               print (f"Ваше время {minutes[mm]} {hours2[hh]}" )   

        if mm > 30 and mm < 45:
            if mm == 31:
                print (f"Ваше время {minutes[mm]} минута {hours[hh]}" )
            elif mm > 31 and mm < 45:
                print (f"Ваше время {minutes[mm]} минут {hours[hh]}")

        if mm > 45:
            print (f"Ваше время без {minutes2[mm]} минут {hours[hh]}" )
            break

