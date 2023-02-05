with open("test.txt", 'rb') as f:
    print(repr(f.read()))

with open("test.jpg", 'rb') as f:
    print(repr(f.read(100)))