import b_logic

menu = """
1. Show all contacts
2. Find a number by surname
3. Find a number by name
4. Search by phone number
5. Add a contact
6. Edit a contact
7. Delete a contact


8. Exit
"""


def get_all_contacts():
    print(b_logic.get_all_contacts())


def add_contacts():
    surname = input("Enter the last name:\n").title()
    name = input("Enter a name:\n").title()
    number = input("Enter the phone number(format 375XXXXXXXXX):\n")
    print(b_logic.add_contact(surname, name, number))


def edit():
    value = input('Enter the name, surname, or phone number of the contact you want to change:\n').title()
    info = [input('What do you want to change?(Surname, Name or Number)\n').title(), input('Enter a new value\n')]
    print(b_logic.edit(value, info))


def search():
    request = input().title()
    print(b_logic.search(request))


def search_number():
    request = input("Enter the contact number with the code (example: 375291234567):\n")
    print(b_logic.search_number(request))


def remove():
    value = input('Enter the name, surname, or phone number of the contact you want to delete:\n').title()
    print(b_logic.remove(value))


def main_cycle():
    while True:
        print("Menu:")
        print(menu)
        choice = input()
        if choice == '1':
            get_all_contacts()
        elif choice == '2':
            print("Enter the contact's last name:\n")
            search()
        elif choice == '3':
            print("Enter the name of the contact:\n")
            search()
        elif choice == '4':
            search_number()
        elif choice == '5':
            add_contacts()
        elif choice == '6':
            edit()
        elif choice == '7':
            remove()
        elif choice == '8':
            break
        else:
            print("not valida menu point, try again")


main_cycle()
