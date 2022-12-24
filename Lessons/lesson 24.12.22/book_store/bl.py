import data

cart = []

def get_all_names(): 
    names = data.get_all_names()
    res = ""
    if len(names) > 0:
        for i in range(1, len(names)+1):
            res = f"{res}\n{i}.{names[i-1]}"
    return res

def get_all():
    names = data.get_all_names()
    res = ""
    if len(names) > 0:
        for name in names:
            content = data.get_book(name)
            if not content:
                continue
            res = f"{res}\n{name}:\n{content}"
    return res

def add_book(name, descr):
    data.add_book(name, descr)
    return "The book was added"

def get_book(name):
    descr = data.get_book(name)
    if descr:
        return f"{name}\n{descr}"
    else:
        return "The book was not found"

def remove_book(name):
    res = data.remove_book(name)
    if res:
        return "The book was deleted"
    else:
        return "The book was not found"

def search(term):
    content = data.search(term)
    res = ""
    if len(content) > 0:
        for i in range(1, len(content)+1):
            res = f"{res}\n{i}.{content[i-1]}"
    return res if res else "Nothing was found"

def add_to_cart(name): pass

def remove_from_cart(name): pass

def show_cart(): pass

if __name__ == "__main__":
    print(add_book("test_book", "some descr"))
    print(get_all_names())
    print(get_all())
    print(search("test"))





