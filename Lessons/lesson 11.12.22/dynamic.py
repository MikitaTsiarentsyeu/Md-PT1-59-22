def sum(a, b):
    return a+b

print(id(sum))

def sum(a, b, c):
    return sum(sum(a,b), c)

print(id(sum))

x = 10
x = "10"

# sum(2, 3, 4) error

def times(a:object, b:object) -> object:
    return a*b

print(times(2, 3))
print(times([2], 3))
print(times('[2]', 3))


def times_for_int(a:int, b:int) -> int:
    """this function
    will multiply only 
    int values, will return None
    in all other cases"""
    if isinstance(a, int) and isinstance(b, int):
        return a*b

print(times_for_int(2, 3))
print(times_for_int([2], 3))
print(times_for_int('[2]', 3))

print([1, 2, 3] == [3, 2, 1])
def eq(l1, l2):
    for i in l1:
        if i not in l2:
            return False
    for i in l2:
        if i not in l1:
            return False
    return True

print(eq([1,2,3,4,4,4,4], (4,2,3,1)))
print(eq("1234", ("4","2","3","1")))


# while True:
#     i = input("Enter:\n")
#     try:
#         int(i)
#         break
#     except:
#         print("The value was wrong! Try again")
