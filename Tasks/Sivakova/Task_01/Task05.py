import time

def check_str(string) -> int:
    title = 0
    stroka = 0
    for i in string:
        if i.istitle():
            title+=1
        elif i==" " :
            pass
        else:
            stroka+=1
    return f' It-s about {title} title letters, and {stroka} lowercase letters in your string'


   
   
def is_prime(number) -> bool:
  while number > 1:
    for i in range(2, int(number/2)+1):
         if (number % i) == 0:
            return False        
    else:
        return True
    
  else:
    return False

        
def get_ranges(number):
    lst = []
    
   
    for i in range((len(number)-1)):
    
        
        if number[i]+1 == number[i+1] and number[i]-1 != number[i-1]:
                lst.append(str(number[i])+'-')
                
        elif number[i]+1 != number[i+1] and number[i]-1 == number[i-1]:
                lst.append(str(number[i])+', ')
                
        elif number[i]+1 != number[i+1] and number[i]-1 != number[i-1]:
                lst.append(str(number[i])+', ')
        
    if number[-1]-1 == number[-2]:
            lst.append(str(number[-1]))
    else:
            len(number)
    if number[-1]-1 != number[-2]:
            lst.append(str(number[-1]))
    else:
            len(number)
    
    return (''.join(lst))
              




print("Let's conculate sone function. We'll start with counting uppercase and lowercase letters \n")
print(check_str(str(input('Please, enter some text'))))
time.sleep(1)
print('_'*100)
print("You can input your values to check this prime \n")
print(is_prime(int(input())))
time.sleep(1)
print('_'*100)
print("And finally we get the ranges \n")
print(get_ranges([0, 2, 3, 4, 7, 8, 10, 12]))
print(get_ranges([4,7,10]))  
print(get_ranges([2, 3, 8, 9]))  