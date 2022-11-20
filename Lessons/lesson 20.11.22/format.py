s = "test " + "str"
print(s)
print("test", "str")

s = "a"+"b"+"c"+"1"+"2"+"3"
print(s)

s = "test"*8
print(s)

c, d, p = "cat", "dog", "parrot"

"a cat, a dog and a parrot"
print("a " + c + ", a " + d + " and a " + p)

"a cat"
"a cat, a "
"a cat, a dog"
"a cat, a dog and a "
"a cat, a dog and a parrot" 

pattern = "a {}, a {} and a {}"
print(pattern.format(c, d, p))

f"a {c}, a {d} and a {p}"

x = 25
print(f"the answer is {x/5}")
print(f"the answer is {x/4.8:.10f}")

# print("the string %s and the number %d" % ("test", 25/5)) OLD WAY, DO NOT USE!!!