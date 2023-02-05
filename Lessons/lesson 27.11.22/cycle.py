# while True:
#     print("to infinity and beyond!!!")

# x = 0
# while x<=10:
#     print(x)
#     x += 1

# x = True
# counter = 0
# while x:
#     if counter == 10:
#         x = False
#     print(x)
#     counter += 1

# x = 10
# while x:
#     print(x)
#     x -= 1

l = list("test string")
# i = 0
# while i < len(l):
#     print(l[i])
#     i += 1

# for letter in l:
#     print(letter)

# print(letter)

d = {1:"one", 2:"two"}
for i in d:
    print(i, d[i])

for k, v in d.items():
    print(k, v)

for i in set(l):
    print(i)

# l = [1]
# for i in l:
#     l.append(i+1)
#     print(i)

for i, e in enumerate(l):
    print(i, e)


for i in range(len(l)):
    print(i, l[i])

for i in range(2, 11, 2):
    print(i)

l = [[1,2,3], [4,5,6], [7,8,9]]
for i in l:
    print(i)
    for j in i:
        print(j)