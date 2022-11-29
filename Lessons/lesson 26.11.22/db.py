d = {9103976271:[("Reina", "Meinhard"), ("Memphis", "Tennessee")],
4199392609:[("Stephanie", "Bruce"), ("Greensboro", "North Carolina")],
9099459979:[("Ermes", "Angela"), ("Dallas", "Texas")],
6123479367:[("Lorenza", "Takuya"), ("Indianapolis", "Indiana")],
7548993768:[("Margarete", "Quintin"), ("Raleigh", "North Carolina")]}

number = int(input())

if number in d:
    res = d[number]
    print(f"{res[0][0]} {res[0][1]} from {res[1][0]}, {res[1][0]}")
else:
    print("nothing was found")

res = d.get(number)
if res:
    print(f"{res[0][0]} {res[0][1]} from {res[1][0]}, {res[1][0]}")
else:
    print("nothing was found")

