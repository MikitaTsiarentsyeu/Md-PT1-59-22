from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M")
time_value = input("Do you want to type the time valueyourself, y/n?\n").lower()
if  time_value == 'y':
    enter_time = input("Please enter your time value in the format hh:mm\n")
else:
    print("Current Time =", current_time)
if  len(enter_time) == 5 and enter_time[2] == ":":
	time = enter_time.split(":")
else:	
    print("The data is in incorrect format")
if  time[0].isdigit() == True and time[1].isdigit() == True and  -1 < int(time[0]) < 24 and   -1 < int(time[1]) < 60 :
	hours = int(time[0])              
	minutes = int(time[1])
else:
    print("The data is in incorrect format")

d = {1:'один', 2:'два', 3:'три', 4:'четыре', 5:'пять', 6:'шесть', 7:'семь', 8:'восемь', 9:'девять', 
     10:'десять', 11:'одиннадцать', 12:'двенадцать', 13:'тринадцать', 14:'четырнадцать', 15:'пятнадцать',
     16:'шестнадцать', 17:'семнадцать', 18:'восемнадцать', 19:'девятнадцать', 20:'двадцать', 30:'тридцать', 40:'сорок', 50:'пятьдесят' }

d1 = {1:'первого', 2:'второго', 3:'третьего', 4:'четвёртого', 5:'пятого', 6:'шестого', 7:'седьмого', 8:'восьмого', 9:'девятого', 
      10:'десятого', 11:'одиннадцатого', 12:'двенадцатого', 13:'первого', 14:'второго',  15:'третьего', 16:'четвёртого', 17:'пятого', 18:'шестого',
      19:'седьмого', 20:'восьмого', 21:'девятого', 22:'десятого', 23:'одиннадцатого', 24:'двенадцатого'}     
d2 = {1:'одна минута', 2:'две минуты', 3:'три минуты', 4:'четыре минуты', 5:'пять минут', 6:'шесть минут',
      7:'семь минут', 8:'восемь минут', 9:'девять  минут', 10:'десять минут' , 11:'одиннадцать минут',  12:'двенадцать минут',
      13:'тринадцать минут', 14:'четырнадцать минут', 15:'пятнадцать минут', 16:'шестнадцать минут',  17:'семнадцать минут',  18:'восемнадцать минут',
      19:'девятнадцать минут', 20:'двадцать', 30:'тридцать', 40:'сорок', 45: 'пятнадцати', 46: 'четырнадцати', 47: 'тринадцати', 48: 'двенадцати', 49: 'одиннадцати',
      50:'десяти', 51: 'девяти', 52: 'восьми', 53:'семи', 54: 'шести',  55: 'пяти', 56: 'четырёх', 57: 'трёх', 58: 'двух', 59: 'одной'}
d3 = {13:'один час', 14:'два часа', 15:'три часа', 16:'четыре часа', 17:'пять часов', 18:'шесть часов',
      19:'семь часов', 20:'восемь часов', 21:'девять часов', 22:'десять часов', 23:'одиннадцать часов',  24:'двенадцать часов'}
your_time = (f'Ваше время: {hours}:{minutes}')
print(your_time)
def outputtime (hours, minutes):
    if minutes == 00: 
        if hours in d:
          k = d.get(hours)
          res = (f'{k} часов ровно')
          print (res) 
        elif hours > 20:
             hour = d3.get(hours)
             res = (f'{hour}  ровно')
             print (res)         
    if  hours == 00 and minutes == 00:
        res = (f'Полночь')  
        print(res) 
    if hours <= 23 and 0 < minutes <= 20:
          hour = d1.get(hours+1)
          min = d2.get(minutes)
          res = (f'{min}  {hour}')
          print(res) 
    elif hours <= 23  and 20 < minutes < 45:
        hour = d1.get(hours+1)
        e = minutes%10
        e = d2.get(e)
        l = minutes//10
        l = l*10
        l = d2.get(l)
        res = (f'{l} {e} {hour}')
        print(res)
    elif hours <= 23 and minutes == 30:
         hour = d1.get(hours+1)
         res = (f'половина {hour}')
         print(res)
    elif hours <= 23 and minutes >= 45: 
         hour = d1.get(hours+1)
         min = d2.get(minutes)
         res = (f'без {min} минут {hour}')
         print(res) 
outputtime (hours, minutes)           


