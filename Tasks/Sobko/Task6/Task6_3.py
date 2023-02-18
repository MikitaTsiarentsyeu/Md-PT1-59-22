def reverse(string: str) -> str:
    if len(string) == 0:
        return string
    else:
        return reverse(string[1:]) + string[0]


string = 'hello'
print(f'reverse("hello") => {reverse(string)}')