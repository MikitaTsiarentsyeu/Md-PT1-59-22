from functools import reduce

print_one_object = lambda x: print(x)

print(print_one_object, type(print_one_object))
print_one_object("test")

lambda x, y="test": print(x+y)

(lambda x: print(x))("this is direct lambda call")

def apply(l, f):
    for i in l:
        f(i)

apply(range(1, 11), print)

def sq(x):
    print(x*x)

apply(range(1, 11), sq)
apply(range(1, 11), lambda x: print(x*x))

test_str = "Abc Aab aac aaa"
print(sorted(test_str.split()))
print(sorted(test_str.split(), key=lambda x: x.lower()))
print(sorted(test_str.split(), key=str.lower))

l = [("three", 3), ("two", 2), ("one", 1)]
print(sorted(l))
print(sorted(l, key=lambda x: x[1]))

d = {"three": 3, "two": 2, "one": 1}
print(sorted(d))
print(sorted(d.items(), key=lambda x: x[1]))
print(sorted(d, key=d.get))



l = list(range(1,11))
map_res = map(print, l)
print(map_res, type(map_res))

list(map(print, map(lambda x: x*x, l)))


print(list(filter(lambda x: x%2==0, l)))

print(list(map(lambda x: chr(x*10), filter(lambda x: x%2==0, l))))

print(reduce(lambda x, y: x+y, l))
print(reduce(lambda x, y: f"{x}-{y}", l))
print(reduce(lambda x, y: x if x < y else y, l))