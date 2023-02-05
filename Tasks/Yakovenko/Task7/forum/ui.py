import bl

menu = """
0. exit
1. get all themes names
2. get all themes info
3. add a new theme
4. read a theme
5. search for a theme
6. add a new comment
"""

def get_all_names():
    print(bl.get_all_names())

def get_all_info():
    print(bl.get_all())
    
def add_theme():
    name = input("Input a theme name:\n")
    descr = input("And a description:\n")
    print(bl.add_theme(name, descr))

def read_theme():
    name = input("Input a name:\n")
    print(bl.read_theme(name))

def search():
    term = input("Input a search term:\n")
    print(bl.search(term))

def add_comment():
    name = input("Input a theme name:\n")
    comment = input("Write your comment:\n")
    print(bl.add_comment(name, comment))


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
            add_theme()
        elif choice == '4':
            read_theme()
        elif choice == '5':
            search()
        elif choice == '6':
            add_comment()    
        else:
            print("Invalid menu item, please try again")


main_cycle()