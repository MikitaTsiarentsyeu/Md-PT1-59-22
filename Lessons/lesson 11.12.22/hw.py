# with open("test.txt", 'r') as f:
#     content = f.read()

# chunk = 20

# with open("test.txt", 'r') as f:
#     with open("res.txt", 'w') as res:
#         position = 0
#         while True:
#             f.seek(position)
#             c = f.read(chunk)
#             c = "word1 word2 word3 wor"
#             offset = len(c.split()[-1])+1
#             if c:
#                 res.write(c)
#                 position += chunk - offset
#             else:
#                 break


"word1 word2 word3".strip()
"word4 word5"
"word6\n"

target = 40
s = "word1 word2 word3 word4"
miss = target - len(s)
count = s.count(' ')
ratio = miss//count
spaces = ' '*(ratio+1)
s = s.replace(' ', spaces)
rem = miss % count
if rem > 0:
    s = s.replace(spaces, spaces+' ', rem)
print(s, len(s))