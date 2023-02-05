t = (1,2,3,4,5,"test",)
print(t, type(t))

t = 1,2,3,4,5
print(t, type(t))

t = (1,) #1,
print(t, type(t))

x, y = 2, 3

t = tuple("string")
print(t)

print(t[0], t[-1], t[2:5])

print(len(t))

print(((1,2,3)+(4,5,6))*10)

# t[0] = "test" error

print(t.index("i"))
print(t.count("i"))

t = list(t)
t.append("test")
t = tuple(t)

print(t)

# del t

print("########################################################")


d = {}
print(d, type(d))

d = {"one":1, 2:"two", "three":3.0}
print(d)
# d[0] KeyError

print(d["one"])
print(d[2])

d = {"one": 1, "one": 1.0}
print(d)

d["two"] = 2.0
print(d)

d["two"] = "two"
print(d)

print(d["two"])

print(len(d))
print("two" in d)
print(2.0 in d)

print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

print(d.get("twooo", "not found"))

del d["two"]
print(d)



print("########################################################")

s = {1,2,3}
print(s, type(s))

s = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1}
print(s)

s = set()
print(s, type(s))


l = [1,2,3,4,4,4,4,4,4,4,5,6,7]
print(set(l))

s = set("a very long test string")
print(s)

l = [1,2,3,4,4,4,4,4,4,4,5,6,7]
l = list(set(l))
print(l)

s = ''.join(list((set("a very long test string"))))
print(s)

l1 = [1,2,3]
l2 = [3,2,1]
print(l1 == l2, set(l1) == set(l2))

print({1,2,3,(4,)})

s = {1,2,3,4,5}
s.add(1)
s.add(7)
s.add('a')
print(s)

s.update([3,4,5,6,7])
print(s)
s.update("test string")
print(s)

s.remove(7)
print(s)

# s.remove(7) error
s.discard(7)
print(s)

print(s.pop())
print(s.pop())
print(s.pop())

s.clear()
print(s)


print({1,2,3,4,5}.union({3,4,5,6,7,8}))
print({1,2,3,4,5}.intersection({3,4,5,6,7,8}))

print({3,4,5}.issubset({3,4,5,6,7,8}))


print("########################################################")


l = [[1,2,3],(4,5,6),{7,8,9}]
l = [[1,2,3],[4,5,6],[7,8,9]]

print(l[0])
print(l[1])
print(l[2])

print(l[0][0], l[0][1], l[0][2])
print(l[1][0], l[1][1], l[1][2])
print(l[2][0], l[2][1], l[2][2])

t = (l, "test")
print(t)

t[0][0][0] = "1.0"
print(t)

d = {(1,2,3):"one two three"}
print(d)

d[t] = "tuple"