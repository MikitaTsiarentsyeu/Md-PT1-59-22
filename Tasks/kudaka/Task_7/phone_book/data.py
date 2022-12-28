def file_open(type, file):
    with open("phone_book.txt", type) as phone_book:
        if type == "r":
            return phone_book.read()
        elif type == "a":
            phone_book.write(file)
            pass
        elif type == "w":
            phone_book.write(file)


def add_phone(info):
    file_open("a", info)


def remove_phone(info):
    phons = file_open("r", None)
    phons = phons.replace(info, "")
    file_open("w", phons)
    return True


def get_phone():
    phons = file_open("r", None)
    list_phone = [i + "\n" for i in phons.split("\n")]
    return list_phone


def search_phone(info):
    phons = file_open("r", None)
    list_phone = [i + "\n" for i in phons.split("\n") if info in i]
    return list_phone


def d_info():
    info = " INSTRACTION \nto search a contact,you need to enter a keyword for example: name or number" \
           "\nto see all contacts press button 'show'\nto add number press button 'add'" \
           "\nto delete number,at first search for contact that you want," \
           "\nwhen it appears on screen,press button delete "
    return info
