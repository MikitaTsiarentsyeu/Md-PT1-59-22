s = "five two eleven"
s = [{"five":5, "two":2, "eleven":11}[s] for s in s.split()]
print(s)

s = sorted(list(set(s)))
s += [True, 0, 0]

while True:
    if s[s[-1]] % 2 != 0:
        s[-2] += s[s[-1]]
    if isinstance(s[s[-1]+1], bool):
        break
    if s[-3]:
        print(s[s[-1]]+s[s[-1]+1])
    else:
        print(s[s[-1]]*s[s[-1]+1])
    s[-3] = not s[-3]
    # print(s[s[-1]])
    s[-1] += 1

print(s)