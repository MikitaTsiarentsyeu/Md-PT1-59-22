list = [1, 2, [2, 4, [[7, 8], 4, 6]]]
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print("The sum of the elements is:", sum1(list))