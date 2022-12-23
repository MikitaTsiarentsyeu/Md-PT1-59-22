number_fibonacci = int(input("Enter fibonacci number:\n"))
def fib(n: int) -> list:
   if n == 1:
      return [0]
   elif n == 2:
      return [0, 1]
   list_fib = fib(n-1)
   list_fib.append(list_fib[-1] + list_fib[-2])
   return list_fib 
print("List of fibonacci numbers:\n")
print(fib(number_fibonacci))   
