#number1
def check_str(s):
    d={"upper_case":0, "lower_case":0}
    for c in s:
        if c.isupper():
           d["upper_case"]+=1
        elif c.islower():
           d["lower_case"]+=1
        else:
           pass

    print (s, d["upper_case"], "upper case, ", d["lower_case"], "lower case" )
    
check_str('The quick Brown Fox ->')


          
#number2
digit = int(input("Pleas enter a number:\n"))
def is_prime(digit: int):
	for i in range(2, (digit//2)+1):
		if digit % i == 0:
			return False
	return True

print(f"is_prime({digit}) -> {is_prime(digit)}")


#number3
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
