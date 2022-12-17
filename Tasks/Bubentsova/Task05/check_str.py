import sys

def check_str(s):
    l_upper = []
    l_lower = []
    for i in s:
        if str.isupper(i):
            l_upper.append(i)
        else:
            str.isupper(i) == False
            l_lower.append(i)
    return print(f"{len(l_upper)} upper case, {len(l_lower)} lower case")


while True:
    some_text = input("Please enter some text:\n")
    if some_text:
        text = some_text.replace(" ", "")
        check_str(text)
    else:
        break
    sys.exit()