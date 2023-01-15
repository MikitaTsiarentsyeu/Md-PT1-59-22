import bl

menu = """
Menu:
1. Add book
2. Add contact
3. View all contact in the book
4. Find contact
5. delete contakt
6. delete book
7. Exit
Enter :
"""
def add_book():
    name_book = input("Enter name book\n")
    print(bl.add_book(name_book))

def add_person():
    name = input("Enter a name:\n").title()
    surname = input("Enter the last name:\n").title()
    number = input("Enter the phone number:\n")
    name_book = input("Enter the name book\n")
    print(bl.add_person(surname, name, number, name_book))

def view_persons():
    name_book = input("Enter name book\n")
    for i in bl.view_persons(name_book):
        if isinstance(i, dict):
            print(i["Name"], i["Surname"], i["Number"]) 
        else:
            print(i)

def search():
    value = input("Enter value for search\n")
    result = bl.search(value)
    if isinstance(result, list):
        for i in result:
            print("In", i[0]," : ", i[1]["Name"], i[1]["Surname"], i[1]["Number"])
                
    else:
        print(result)

def delete_person():
    name_book = input('Enter name book for delete contact\n')
    theme = input("Enter value for delete contact\n")
    print(bl.delete_person(name_book, theme))

def delete_book():
    name_book = input("Enter name book\n")
    print(bl.delete_book(name_book))

def main_cycle():
    while True:
        print(menu)
        choice = input()
        if choice == '1':
            add_book()
        elif choice == '2':
            add_person()
        elif choice == '3':
            view_persons()
        elif choice == '4':
            search()
        elif choice == '5':
            delete_person()
        elif choice == '6':
            delete_book()
        elif choice == '7':
            print("Stop")
            break
        else:
            print("not valida menu point, try again")


main_cycle()
