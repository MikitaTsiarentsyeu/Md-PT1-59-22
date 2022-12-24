import csv

laptop = ["4534562", "hp", "omen", "i7", "rtx1080", "16"]

# with open("test.csv", 'a') as f:
#     f.write(','.join(laptop) + '\n')

# is_first = True
# with open("test.csv", 'r') as f:
#     for line in f:
#         if is_first:
#             is_first = False
#             continue
#         print(line.split(','))


# with open("test.csv", 'r') as f:
#     reader = csv.reader(f)
#     for elements in reader:
#         print(elements)

headline = ["product code","make","model","cpu","gpu","memory"]

elements = []
is_first = True
with open("test.csv", 'r') as f:
    reader = csv.DictReader(f, headline)
    for e in reader:
        if is_first:
            is_first = False
            continue
        elements.append(e)

print(elements)

with open("test-copy.csv", 'w', newline='') as f:
    writer = csv.DictWriter(f, headline)
    writer.writeheader()
    writer.writerows(elements)
    