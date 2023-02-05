sum = 0
def listofobjects(l):
    global sum
    for i in l:
        if type(i) == int:
            sum += i
        elif type(i) == list:
            listofobjects(i)
    return sum


def reversestring(s):
    if len(s) == 1:
        return s
    return s[-1] + reversestring(s[:-1])

def fibonacci(number):
    if number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    fiblist = fibonacci(number - 1)
    fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist


def quicksort(n):
    if not len(n):
        return []
    else:
        middle = n[0]
        left = quicksort([i for i in n[1:] if i < n[0]])
        right = quicksort([i for i in n[1:] if i >= n[0]])
    return left + [middle] + right

print(listofobjects([1,2,[[52], 7, 33],5]))
print(quicksort([1, -32, 5, 10, 0, 33, 7, 5]))
print(fibonacci(10))
print(reversestring('Hello dear user.'))





