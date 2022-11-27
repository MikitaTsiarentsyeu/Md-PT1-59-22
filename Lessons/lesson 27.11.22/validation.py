while True:
    user_input = input("Please enter the data in the dd.mm.yyyy format:\n")

    if len(user_input) != 10:
        print("The data is in incorrect format, the length is wrong")
        continue

    if user_input[2] != '.' or  user_input[5] != '.':
        print("The data is in incorrect format, a dot is mnissing")
        continue

    parts = user_input.split('.')
    failed = False
    for i, part in enumerate(parts):
        if not part.isnumeric():
            failed = True
            break
        parts[i] = int(part)

    print(parts)

    if failed:
        print("The data is in incorrect format, you must only use digits")
        continue

    if parts[0] > 31:
        print("The day value myst be less then 31")
        continue

    break


print("the main logic goes here")