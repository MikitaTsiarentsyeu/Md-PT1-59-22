import bl

menu = """
0. exit
1. get all book names
2. get all books info
3. add a new book
4. get a book info
5. search for a book
"""

def get_all_names():
    print(bl.get_all_names())

def get_all_info():
    print(bl.get_all())
    
def add_book():
    name = input("Input a new name:\n")
    descr = input("And a description:\n")
    print(bl.add_book(name, descr))

def get_book():
    name = input("Input a name:\n")
    print(bl.get_book(name))

def search():
    term = input("Input a search term:\n")
    print(bl.search(term))

def main_cycle():
    while True:
        print("choose a point from the menu:")
        print(menu)
        choice = input()
        if choice == '0':
            break
        elif choice == '1':
            get_all_names()
        elif choice == '2':
            get_all_info()
        elif choice == '3':
            add_book()
        elif choice == '4':
            get_book()
        elif choice == '5':
            search()
        else:
            print("not valida menu point, try again")


main_cycle()