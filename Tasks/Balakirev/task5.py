# Task 1
# Option 1. For Russian and English
def check_str(string: str) -> 'n upper case, m lower case':
	count_upper = 0
	count_lower = 0
	for i in range(len(string)):
		if ord(string[i]) >= 65 and ord(string[i]) <= 90:
			count_upper += 1
		elif ord(string[i]) >= 97 and ord(string[i]) <= 122:
			count_lower += 1
		if (ord(string[i]) >= 1040 and ord(string[i]) <= 1071) or ord(string[i]) == 1025:
			count_upper += 1
		elif (ord(string[i]) >= 1072 and ord(string[i]) <= 1103) or ord(string[i]) == 1105:
			count_lower += 1
	return count_upper, count_lower


string = input('Enter text:\n')
upper_reg, lower_reg = check_str(string)
print(f"{upper_reg} upper case, {lower_reg} lower case")


# Option 2.
def check(string: str) -> 'n upper case, m lower case':
	count_upper = 0
	count_lower = 0
	char = ' -:;,?!@#$%^&*()+×÷=/_<>[]€£¥~{}1234567890'
	string = string.translate(str.maketrans('', '', char))
	for i in string:
		if i.isupper():
			count_upper += 1
		elif i.islower():
			count_lower += 1
	return count_upper, count_lower


string = input('Enter text:\n')
upper_reg, lower_reg = check(string)
print(f"{upper_reg} upper case, {lower_reg} lower case")


# Task 2
def is_prime(numbers: int) -> 'return False or True':
	for i in range(2, (numbers//2)+1):
		if numbers % i == 0:
			return False
	return True


numbers = int(input('Enter a number greater than 0:\n'))
print(f"is_prime({numbers}) -> {is_prime(numbers)}")


# Task 3
def get_ranges(mylist: list) -> '1-4, 7-8, 10':
	new_list = []
	nest_list = []
	num = mylist[0]
	nest_list.append(num)
	for i in range(1, len(mylist)):
		if num == mylist[i]-1:
			num = mylist[i]
			nest_list.append(num)
		else:
			num = mylist[i]
			new_list.append(nest_list)
			nest_list = []
			nest_list.append(num)
	new_list.append(nest_list)
	for i in range(len(new_list)):
		if len(new_list[i]) == 1:
			new_list[i] = str(new_list[i][0])
		else:
			new_list[i] = f"{min(new_list[i])}-{max(new_list[i])}"
	return ', '.join(new_list)


mylist = list(map(int, input('Enter non-repeating integers in ascending order separated by commas:\n').split(',')))
print(get_ranges(mylist))
