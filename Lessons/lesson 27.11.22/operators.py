for i in range(20):
    if i == 10:
        break
    if i % 2 == 0:
        pass
    print(i)
else:
    print("there was no brake")


counter = 0
while True:
    counter += 1
    if counter == 10:
        break
    print(counter)

print("#"*10)

counter = 0
while True:
    if counter % 2 == 0:
        pass
    counter += 1
    if counter == 10:
        break
    print(counter)