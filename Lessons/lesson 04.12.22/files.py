# f = open("test.txt", 'r')
# print(f, type(f))

# f.close()

with open("test.txt", 'w') as f:
    f.write(f"4+5={4+5}")
    f.writelines(["test line 1\n", "test line 2\n", "test line 3\n"])
    # f.read() error

with open("test.txt", 'r') as f:
    for l in f:
        print(l)
    # print(f.readlines())

    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))
    # print(repr(f.readline()))

    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))
    # print(repr(f.read(10)))

    # print(f.read())
    # f.seek(0)
    # f.seek(18)
    # print(f.read())

with open("test.txt", 'a') as f:
    f.write("new content from append\n")
    f.seek(0)
    f.write("prepended content\n")

with open("test.txt", 'a+') as f:
    f.seek(0)
    print(repr(f.read()))
    f.write("new content from append plus\n")
    f.seek(0)
    f.write("a plus prepended content\n")
    print(repr(f.read()))

with open("test.txt", 'r+') as f:
    f.write("r+ prepended content\n")
    print(repr(f.read()))


with open("test.txt", 'w+') as f:
    f.write("totally new and cool file content\n")
    f.seek(0)
    f.write("test")