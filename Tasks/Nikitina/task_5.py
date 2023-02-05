# . Реализовать функцию check_str которая получает на вход непустую строку и выдаёт информацию
# о количестве букв в верхнем и нижнем регистре.
# check_str('The quick Brown Fox') -> '3 upper case, 13 lower case'
string = input("Please enter a line\n")
if string == (""):
   print("The string is empty")
if string != (""):
  def check_str (uppercase = [] , lowercase = []):
    uppercase = [i for i in string if i.isupper()]
    lowercase = [i  for i in string if i.islower()]	
    print(f" {len(uppercase)} upper case, {len(lowercase)} lower case")
check_str()

# part2 
#Реализовать функцию is_prime которая получает на вход любое число больше нуля и выдаёт True, 
# если число является простым, и False, если нет.
#is_prime(787) -> True
#is_prime(777) -> False

def is_prime(n):
    for i in range(2, (n//2)+1):
        if n%i == 0:
            return False
        else:
            return True
n = int(input("Please enter a number:\n"))   
if n <=0:
    print("Is not correct input")
else:
    print(is_prime(n)) 

# part3
# Реализовать функцию get_ranges которая получает на вход непустой список неповторяющихся целых чисел, 
# отсортированных по возрастанию, и которая этот список “сворачивает” в набор отрезков.

# get_ranges([0, 1, 2, 3, 4, 7, 8, 10])  ->  "0-4, 7-8, 10"
# get_ranges([4,7,10])  -> "4, 7, 10"
# get_ranges([2, 3, 8, 9])  -> "2-3, 8-9"

list = [2,3,4,5,8,9,10,15,18,19,20,22,23,24,25]
def get_ranges(l):
    another_list = []
    counter = 0
    for i in range(len(list)):
        if i != len(list)-1 and list[i+1]-list[i] == 1:
            counter += 1
        elif counter == 0:
                another_list.append(str(list[i]))
        else:
            another_list.append(f'{list[i-counter]}-{list[i]}')
            counter = 0
    return f'{",".join(another_list)}'
print (get_ranges(list))