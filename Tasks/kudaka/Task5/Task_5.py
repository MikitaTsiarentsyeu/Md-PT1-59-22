str_up_low = "The quick Brown Fox"
def check_str(string:str) -> "n upper case, n lower case":
   "taking a string, and return count of upper letters and count of lower letters "
   count = "".join(["1" if i.isupper() else "2" for i in string.replace(" ","")])
   return f"{count.count('1')} upper case {count.count('2')} lower case"
print(check_str(str_up_low))

def is_prime(number:int) -> "return true or false":
   "taking a number, and return True if number is a prime,return False if it's not prime "
   n_calcul = [i for i in range(1,number+1) if number % i == 0]
   if len(n_calcul) == 2:
      return True
   else:return False
print(is_prime(787))


num_list = [0,1,3,5,7,8,10,11,12,13,17,19,20]
def get_ranges(list_n:list) -> "1-4,5-7,9":
   "this function taking sorted list without dublication of items, and return line segment of items"
   new_list = []
   new_list_2 = []
   count = 0
   for i in range(len(list_n)-1):
      if list_n[i] + 1 == list_n[i+1] or list_n[i]+1 == list_n[-1]:
         count+= 1
         new_list_2.append(list_n[i])
      elif list_n[i] - 1 == list_n[i-1] and count > 0:
         new_list_2.append(list_n[i])
         new_list.append(tuple(new_list_2))
         new_list_2.clear()
         count = 0
      elif count == 0:
         new_list.append(tuple([list_n[i]]))
   if count > 0:
      new_list_2.append(list_n[-1])
      new_list.append(tuple(new_list_2))
   elif count == 0:
      new_list.append(tuple([list_n[-1]]))
   new_list_2 = [f"{i[0]}-{i[-1]}" if len(i) > 1 else f"{i[0]}" for i in new_list]
   return ('"'+('{}, '*len(new_list)).strip(", ")+'"').format(*new_list_2)
print(get_ranges(num_list))