
import datetime

list_time = []


dict_min ={0 : ["ровно" , "одна минута" , "две минуты" , "три минуты" , "четыре минуты" , "пять минут" , "шесть минут" , "семь минут" , "восемь минут" , "девять минуты"] , 
					1 : [ "десять минут" , "одинадцать минут" , "двенадцать минут" , "тринадцать минут" , "четырнадцать минут" , "пятнадцать минут" , "шестнадцать минут" , "семнадцать минут" , "восемнаднать минут" , "девятнадцать минут"], 
					2: ["двадцать " , "двадцать минут" , "одна минута" , "две минуты" , "три минуты" , "четыре минуты" , "пять минут" , "шесть минут" , "семь минут" , "восемь минут" , "девять минут"],
					3 : ["тридцать ", "тридцать минут", "одна минута" , "две минуты" , "три минуты" , "четыре минуты" , "пять минут" , "шесть минут" , "семь минут" , "восемь минут" , "девять минут"], 
					4 : ["сорок ","сорок минут", "одна минута" , "две минуты" , "три минуты" , "четыре минуты" , "пять минут" , "шесть минут" , "семь минут" , "восемь минут" , "девять минут"], 
					5 : ["пятьдесят ", "пятьдесят минут" , "одна минута" , "две минуты" , "три минуты" , "четыре минуты" , "пять минут" , "шесть минут" , "семь минут" , "восемь минут" , "девять минут"]}
 																
dict_hour ={ 0 : ["ноль часов", "один час", "два часа", "три часа", "четыре часа", "пять часов", "шесть часов", "семь часов", "восемь часов", "девять часов"] , 
					   1 : [ "десять часов" , "одинадцать часов" , "двенадцать часов" , "тринадцать часов" , "четырнадцать часов" , "пятнадцать часов" , "шестнадцать часов" , "семнадцать часов" , "восемнаднать часов" , "девятнадцать часов"] , 
					   2 : ["двадцать ", "двадцать часов" , "один час", "два часа", "три часа", "четыре часа", "пять часов", "шесть часов", "семь часов", "восемь часов", "девять часов"]}
 
hours = ["0","первого","второго","третьего","четвертого","пятого","шестого","седьмого", "восьмого","девятого","десятого","одинадцатого","двенадцатого" , "первого", "второго", "третьего","четвертого", "пятого", "шестого", "седьмого", "восьмого", "девятого", "десятого", "одинадцатого", "двенадцатого", "первого"]

min = ["0", "одной", "двух", "трех", "четырех", "пяти", "шести", "семи", "восьми", "девяти", "десяти", "одинадцати", "двенадцати", "тринадцати", "четырнадцати", "пятнадцати"]

num = ["0", "час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "двенадцать","час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одинадцать", "двенадцать" ]



def enter_user ():
	enter_value = input("Do you want to use your time y/n : ").lower()
	if enter_value == "y" :
		enter_time = input("Enter your time in format hh:mm")
		if len(enter_time) == 5 and enter_time[2] == ":" :
			enter_time = enter_time.split(":")
			if enter_time[0].isdigit() == True and enter_time[1].isdigit() == True and  -1 < int(enter_time[0]) < 24 and   -1 < int(enter_time[1]) < 60 :
				hour = list(enter_time[0])                
				minutes = list(enter_time[1])
				output(hour, dict_hour, list_time)
				output(minutes , dict_min, list_time)
				last(enter_time, list_time, hours, min, num)
				print(f"Второй вариант вывода времени :  {list_time[0]}  {list_time[1]}")		
			else:
				print(f"You have done mistakes, try again")
				enter_user()	
		else:
			print(f"You have done mistakes, try again")
			enter_user()		
	elif enter_value == "n":
			enter_time = datetime.datetime.now().strftime("%H:%M")
			enter_time = enter_time.split(":")
			hour = list(enter_time[0])                
			minutes = list(enter_time[1])
			output(hour, dict_hour, list_time)
			output(minutes , dict_min, list_time)
			last(enter_time, list_time, hours, min, num)
			print(f"Второй вариант вывода времени :  {list_time[0]}  {list_time[1]}")	
	else:
		print(f"You have done mistakes, try again")
		enter_user()
			
def output(a, b, c):
	for v, k in b.items():
		if v == int(a[0]) :
			if v < 2:
				for m, p in enumerate(k) :
					if m == int(a[1]) : 
						list_time.append(p)
			if v > 1 :
				for m, p in enumerate(k) :
					if int(a[1]) == 0 and int(a[1]) == m : 
						list_time.append(k[1])
					elif int(a[1]) == m:	
						list_time.append(k[0] + k[m+1])
				
def last(a , b , c , d, e):
	if int(a[1]) == 00 :
		print(1)
		print(f"Первый вариант. Ваше время:  {b[0]} ровно ")
	elif int(a[1]) < 30 :
		print(2)
		print(f"Первый вариант. Ваше время:  {b[1]}  {c [ int(a[0] )+1] } ")		
	elif int(a[1]) == 30 :
		print(3)
		print(f"Первый вариант. Ваше время:  половина  {c [ int(a[0] )] } ")		
	elif int(a[1]) > 30 and int(a[1]) < 45 :
		print(4)
		print(f"Первый вариант. Ваше время:  {b[1]}  {c [ int(a[0] )+1] } ")	
	elif int(a[1]) >= 45 :
		print(5)
		print(f"Первый вариант. Ваше время:  без {d[ 60-int(a[1]) ]} минут {e[int(a[0])+1] }")			
			

enter_user()
