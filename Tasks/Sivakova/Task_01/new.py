import datetime
d1= datetime.datetime.now()
time = d1.strftime("%H:%M")

d ={1:'один',           2:'два',           3:'три',
           4:'четыре',         5:'пять',          6:'шесть',
           7:'семь',           8:'восемь',        9:'девять', 
          10:'десять',        11:'одиннадцать',  12:'двенадцать',
          13:'тринадцать',    14:'четырнадцать', 15:'пятнадцать',
          16:'шестнадцать',   17:'семнадцать',   18:'восемнадцать',
          19:'девятнадцать',  20:'двадцать',     30:'тридцать',
          40:'сорок',         50:'пятьдесят' }

d1 = {1:'первого',           2:'второго',           3:'третьего',
           4:'четвёртого',         5:'пятого',          6:'шестого',
           7:'седьмого',           8:'восьмого',        9:'девятого', 
          10:'десятого',        11:'одиннадцатого',  12:'двенадцатого',
          13:'первого',           14:'второго',           15:'третьего',
           16:'четвёртого',         17:'пятого',          18:'шестого',
           19:'седьмого',           20:'восьмого',        21:'девятого', 
          22:'десятого',        23:'одиннадцатого',  24:'двенадцатого'}     
d2 =  {1:'одна',           2:'две',           3:'три',
           4:'четыре',         5:'пять',          6:'шесть',
           7:'семь',           8:'восемь',        9:'девять', 10:'десять',        11:'одиннадцать',  12:'двенадцать',
          13:'тринадцать',    14:'четырнадцать', 15:'пятнадцать',
          16:'шестнадцать',   17:'семнадцать',   18:'восемнадцать',
          19:'девятнадцать',  20:'двадцать',   30:'тридцать',
          40:'сорок',         50:'пятьдесят', 60:'шестьдесят' }





userstart = input ("Do you want to enter time by yersellf? Yes/No ")
if userstart == "Yes":
            while True:
                user = input("Please enter the data in the dd:mm format:\n")

                if len(user) != 5:
                    print("The data is in incorrect format, the length is wrong")
                    continue

                if user[2] != ':':
                    print("The data is in incorrect format, a dot is mnissing")
                    continue

                number = user.split(':')
                print (number)
                failed = False
                for i, num in enumerate(number):
                    if not num.isnumeric():
                        failed = True
                        break
                    
                    number[i] = int(num)

                print(number)

                if failed:
                    print("The data is in incorrect format, you must only use digits")
                    continue

                if number[0] >= 24:
                    print("The first value must be less then 24")
                    continue
                if number[1] >= 60:
                    print ("Please enter the format of minute correctly")
                    continue
            
                hh = number[0]
                mm = number [1]
                break
            yourtime = "Your time is {}:{}".format(hh,mm)
            print(yourtime)

       
if hh <= 20 and mm==00: 
       if hh in d:
          k = d.get(hh)
          print (f'{k} часов ровно')
        
       else:
        b=hh%10
        b=d.get(b)
        c=hh//10
        c=c*10
        c=d.get(c)
        res=(c+ " " + b + " час ровно")
        print(res)

if hh <= 20 and mm<=20: 
          hour = d1.get(hh+1)
          
          min = d2.get(mm)
          print(min, hour)
        
elif hh>=20 and mm<=20:
        b=hh%10
        b=d1.get(b+1)
        c=hh//10
        c=c*10
        c=d.get(c)
        min = d2.get(mm)
        res=(f"{min} минут {c} {b} часа")
        print(res)
        print(b)
elif hh <= 20 and mm>20:
        hour = d1.get(hh+1)
        e=mm%10
        e=d2.get(e)
        l=mm//10
        l=l*10
        l=d2.get(l)
        res=(f"{l} {e} минут {hour} часа")
        print(res)
           
elif hh>=20 and mm>20:
        hour = d1.get(hh+1)
        e=mm%10
        e=d2.get(e)
        l=mm//10
        l=l*10
        l=d2.get(l)
        res=(f"{l} {e} минут {hour} часа")
        print(res)
        print(hour)

             
                
    
        
if userstart == "No":
        print(time)

            