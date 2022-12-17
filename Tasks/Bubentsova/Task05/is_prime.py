def is_prime(number):
    number_is_prime = True
    if number > 1:
        for d in range(2, number):
            if (number % d) == 0:
                number_is_prime = False
                break
        return number_is_prime
    else:
        return False


number = int(input("Plese enter some number > 0\n"))
print(is_prime(number))