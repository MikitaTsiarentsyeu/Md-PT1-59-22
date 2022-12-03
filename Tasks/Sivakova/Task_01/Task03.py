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
d2 =  {1:'одна минута',           2:'две минуты',           3:'три минуты',
           4:'четыре минуты',         5:'пять минут',          6:'шесть минут',
           7:'семь минут',           8:'восемь минут',        9:'девять  минут', 10:'десять минут' ,  
           11:'одиннадцать минут',  12:'двенадцать минут',
          13:'тринадцать минут',    14:'четырнадцать минут', 15:'пятнадцать минут',
          16:'шестнадцать минут',   17:'семнадцать минут',   18:'восемнадцать минут',
          19:'девятнадцать минут',  20:'двадцать',     30:'тридцать',
          40:'сорок',         50:'пятьдесят'}
d3 = {13:'один час',           14:'два часа',           15:'три часа',
           16:'четыре часа',         17:'пять часов',          18:'шесть часов',
           19:'семь часов',           20:'восемь часов',        21:'девять часов', 
          22:'десять часов',        23:'одиннадцать часов',  24:'двенадцать часов'}
          
def texttime (a,b):
    if mm==00: 
       if hh in d:
          k = d.get(hh)
          print (f'{k} часов ровно') 
       elif hh>20:
            hour = d3.get
            print (f'{hour}  ровно')         
          
    if hh==00 and mm==00:
        print  (f'Полночь')   
    if hh<=23 and 0<mm<=20:
          hour = d1.get(hh+1)
          
          min = d2.get(mm)
          print(f'{min}  {hour}')                
    elif hh<=23  and 20<mm<30:
        hour = d1.get(hh+1)
        e=mm%10
        e=d2.get(e)
        l=mm//10
        l=l*10
        l=d2.get(l)
        res=(f"{l} {e}  {hour} часа")
        print(res)
    elif hh<=23  and 30<mm<60:
        hour = d1.get(hh+1)
        e=mm%10
        e=d2.get(e)
        l=mm//10
        l=l*10
        l=d2.get(l)
        res=(f"{l} {e} {hour} часа")
        print(res)                    
    elif hh<=23 and mm==30:
         hour = d1.get(hh+1)
         print(f'половина {hour}')


    return(a,b)   




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
                failed = False
                for i, num in enumerate(number):
                    if not num.isnumeric():
                        failed = True
                        break
                    
                    number[i] = int(num)    

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
            
           
            texttime (hh,mm)           
            yourtime = "Your time is {}:{}".format(hh,mm)
            print(yourtime)

             
                
    
        
if userstart == "No":
    
    number = time.split(':')
    number1 = list(number)
    hh = int(number1[0])
    mm = int(number1[1])
  
   
    if hh in d:
                 texttime (hh,mm)
                 yourtime = "Your time is {}:{}".format(hh,mm)
                 print(yourtime)
