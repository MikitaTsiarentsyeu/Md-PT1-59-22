filename = "test.txt"

with open(filename, 'r') as f:
    content = f.readlines()

name = filename.split('.')
name[0] += "_copy"
filename = '.'.join(name)

with open(filename, 'w') as f:
    f.writelines(content)