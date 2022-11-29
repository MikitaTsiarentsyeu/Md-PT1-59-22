s = 'test string'
print(type(s))

print(56)
print(str(56))

print(repr(56))
print(repr(str(56)))

new_s = "test string"
print(s == new_s)

print('056' == '56')

s = "Hello, I'm Zephirka the dog"

s = """ line1
    line2
    line3"""

print(repr(s))

s = "my very long string"
print(len(s))
print(len(""))
print(len('\n'))

print(s[0], s[1], s[2], s[3], s[4])
print(s[-1], s[-2], s[-3], s[-4])

print(s[len(s)-1])
print(s[-len(s)])

# print(s[10000000]) IndexError
# s[0] = "r" TypeError

print(s[0:7])
print(s[0:len(s)])
print(s[:])
print(s[:7])
print(s[7:])

print(s[3:-3])

print(s[::3])
print(s[::-1])

print(s[3:-3:2])

print("test" in s)
print("s" in s)
print("string" in s)



print(s.upper())
print(s)

s = s.upper().lower().capitalize()
print(s)

s = s.replace(" ", "_-_").replace("_-_", "YOUR AD COULD BE HERE")
print(s)

print(s.find('!'))
print(s.find("YOUR AD COULD BE HERE"))

s = "some not so long str"
print(s.split())

print(s.split('s'))
print(s.split(' not '))

print('!!!test!!!'.join(['some', 'not', 'so', 'long', 'str']))