user_string = input("Please enter your string:\n")
def reverse_string(any_string):
    if any_string == "":
        return any_string
    else:
        return reverse_string(any_string[1:]) + any_string[:1]
print(reverse_string(user_string))