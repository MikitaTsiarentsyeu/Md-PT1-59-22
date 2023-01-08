import data

def add_book(name_book):
    value = data.add_book(name_book)
    if value:
        return f"The book has been added"
    else:
        return f"The book was in list books"


def add_person(name, surname, number, name_book):
    person = {"Name": name,"Surname": surname, "Number": number}
    value = data.add_person(person, name_book)
    if value:
        return f"The contact has been added"

def view_persons(name_book):
    value = data.view_persons(name_book)
    if value != False:
        return value
    else:
        return ["The book has not been found"]

def search(theme):
    value = data.search(theme)
    if value != []:
        return value
    else:
        return f"The value has not been found"

def delete_person(name_book, theme):
    value = data.delete_person(name_book, theme)
    if isinstance(value, bool):
        if value == True:
            return f"The contact has been removed "
        elif value == False:
            return f"The value has not been found"
    else:
        return f"The book has not been found"

def delete_book(name_book):
    value = data.delete_book(name_book)
    if value :
        return f"The book has been removed"
    else:
        return f"The book has not been found"

#if __name__ == "__main__":
    #print(add_books("phone_book_2"))
    #print(add_person("Kate","lesh4eva", "+37533", "phone_book_2"))
    #print(view_persons("phone_book_2"))
    #print(search("lesh"))
    #print(delete_person("phone_book_2", "K"))
    #print(delete_book("phone_book_2"))