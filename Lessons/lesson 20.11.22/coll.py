l = []
print(type(l))
print(l)

l = [1,2,3,4,5,"test"]
print(l)

print(list("my test string"))

print([1,2,3]+[4,5,6])
print([0]*10)

print(len(l))
print(l[0], l[1])
print(l[::-1])

l[0] = 1.0
print(l)

l[5:] = [6,7,8,9,"ten"]
print(l)

# l[10000000] IndexError
# l[len(l)] = 11

l.append("NEW ELEM")
print(l)

l.extend([333,444])
l.extend("test")
print(l)

l.insert(0, "new first element")
print(l)

l.remove('ten')
print(l)

x = l.pop()
print(x, l)

x = l.pop(0)
print(x, l)

l.pop(3)
print(l)

del l[0]
print(l)

del l[0:8]
print(l)

# del l
# print(l)
l.clear()
print(l)


l, m = [1,2,3], [1,2,3,4]
l == m
print(l == m)

print(2 in m)

l = ["first", "second", "third"]
l[0], l[2] = l[2], l[0]
print(l)

l = [[], [], []]