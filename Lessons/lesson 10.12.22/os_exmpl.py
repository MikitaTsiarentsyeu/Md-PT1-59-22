import os

print(os.name)

print(os.sep)

print(os.sep.join(["level 1", "level 3"]))

x = os.path.join("level 1", "level 2", "level 3")
print(x)

# os.makedirs(x)

# print(os.getcwd())
# os.chdir(x)
# print(os.getcwd())

# open("test.txt", 'w')

print(os.listdir())

for l in os.walk(os.getcwd()):
    print(l)