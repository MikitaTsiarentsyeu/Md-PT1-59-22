import sys

def get_ranges(some_list):
    segments = [[some_list[0]]]
    for i in range(1, len(some_list)):
        if some_list[i - 1] - some_list[i] == -1:
            segments[len(segments) - 1].append(some_list[i])
        else:
            segments.append([some_list[i]])

    list_new = []
    for s in segments:
        del s[1:-1]
        if len(s) > 1:
            s.insert(1, "-")
        s_string = "".join(map(str,s))
        list_new.append(s_string)
        set_of_segments = ", ".join(list_new)
    
    return set_of_segments


while True:
    option = input("Hello, would you like to type the values by yourself (yes/no)?\n")
    if option == "yes":
    # First option. Values are entered by user but without validation: user enters expected values via space
    # and there are no space at the end
        l = input()
        l = l.split(" ")
        l = [int(i) for i in l]
        l = sorted(list(set(l)))

        print(get_ranges(l))
    else:
    # Second option with predefined list, just to check function faster
        l = [0, 1, 2, 3, 4, 7, 8, 10, 14, 15, 16, 40, 45, 46, 888, 889]

        print(get_ranges(l))
    sys.exit()