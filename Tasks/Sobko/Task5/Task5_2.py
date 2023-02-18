def is_prime(number: int):
	for i in range(2, (number//2)+1):
		if number % i == 0:
			return False
	return True

number = int(input('Enter a number greater than 1:\n'))
if number <=0:  
    print("Error")
elif number == 1:
    print("Error")
elif number > 1:
    print(f"is_prime({number}) -> {is_prime(number)}")
    