def is_prime():
    num = int(input('Hi, enter your value:\n'))
    if num <= 0:
        return "Something went wrong. Please, enter the value higher than 0."
    elif num == 1:
        return True
    elif num >= 1:
        for i in range(2, num):
            if num % i == 0:
                return False
            return True

def check_str():
    list = []
    list.extend(input("I'm waiting for you to enter the string:\n"))
    uppercounter = 0
    lowercounter = 0
    for i in list:
        if i == i.upper():
            uppercounter += 1
        elif i == i.lower():
            lowercounter += 1
    return f'{uppercounter} upper case, {lowercounter} lower case'

def get_ranges(checklist):
    decision = []
    for i in range(len(checklist) - 1):
        if checklist[i] + 1 == checklist[i + 1] and checklist[i] - 1 != checklist[i - 1]:
            decision.append(str(checklist[i]) + '-')
        elif checklist[i] - 1 == checklist[i - 1] and checklist[i] + 1 != checklist[i + 1]\
                and checklist[i] != checklist[-1]:
            decision.append(str(checklist[i]) + ', ')
        elif checklist[i] - 1 != checklist[i - 1] and checklist[i] + 1 != checklist[i + 1]\
                and checklist[i] != checklist[-1]:
            decision.append(str(checklist[i]) + ', ')
    decision.append(str(checklist[-1]))
    return f"So the result is {''.join(decision)}"

print(is_prime())
print(check_str())
print(get_ranges([1,23,45,46,47,48]))

