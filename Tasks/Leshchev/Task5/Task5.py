line = "The quick Brown Fox"
def check_str (up = [] , low = []):
	up = [i for i in line if i.isupper()]
	low = [i  for i in line if i.islower()]	
	print(f"{len(up)} upper case, {len(low)} lower case")
check_str()


def is_prime (x = 1, y = True):
	x = int(input("Enter your number > 0: "))
	if x > 1:
		for i in range(2, (x//2)+1):
			if  x%i == 0 :
				y = False
		print(f"number is {y}") 
	else:
		print("You have done mistakes, please try again")
		is_prime()

is_prime()	

x = [0, 1, 2, 3, 4, 7, 8, 10]
y = [4,7,10]
z = [2, 3, 8, 9]
k = [1,20, 21,22]
		
def get_ranges(x):
	big_list = [[x.pop(0)]]
	for i, n in enumerate(x) :
			if big_list[-1][-1]+1 == x[i] :
				big_list[-1].append(x[i])
			elif big_list[-1][-1]+1 != x[i] :		
				big_list.append(list())
				big_list[-1].append(x[i])
	x = ""
	for i, v in enumerate(big_list) :
		if len(v) == 1 and i != len(big_list)-1:
			x = x + str(v[0]) + ","
		elif  len(v) == 1 :
			x = x + str(v[0]) 
		elif len(v) > 1 and i != len(big_list)-1:
			x = x + str(v[0]) + "-" + str(v[-1]) + ","
		elif len(v) > 1 :
			x = x + str(v[0]) + "-" + str(v[-1])
	print(x)

get_ranges(x)		
get_ranges(y)
get_ranges(z)		
get_ranges(k)			