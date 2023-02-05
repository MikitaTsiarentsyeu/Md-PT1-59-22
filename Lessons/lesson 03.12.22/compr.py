l = [x for x in range(1, 11)]
print(l)

l = [x*x for x in range(1, 11)]
print(l)

l = [str(x) for x in range(1, 100) if x%5 == 0 if x%2 == 0]
print(l)


l = []
for x in range(1, 100):
    if x%5 == 0:
        if x%2 == 0:
            l.append(str(x))
print(l)


d = {x:str(x) for x in range(1,11)}
print(d)

l = [v*k for k, v in d.items()]
print(l)

l1 = [1,2,3,4,5]
l2 = [0,1,2]
l = [x**y for x in l1 for y in l2]
print(l)
# for x in l1:
#     for y in l2:
#         x**y

l = [[1,2,3], [4,5,6], [7,8,9]]
l = [y for x in l for y in x]
print(l)