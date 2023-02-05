import os

start_path = "book_store"
dir = "books"
current_dir = os.path.join(start_path, dir)
os.chdir(current_dir)

ext = ".txt"

def get_all_names():
    return [x.replace(ext, '') for x in os.listdir()]

def add_book(name, descr):
    with open(f"{name}{ext}", 'w') as f:
        f.write(descr)

def get_book(name):
    content = os.listdir()
    name = f"{name}{ext}"
    if name in content:
        with open(name, 'a+') as f:
            f.seek(0)
            content = f.read()
            return content
    return False

def remove_book(name):
    content = os.listdir()
    name = f"{name}{ext}"
    if name in content:
        os.remove(name)
        return True
    else:
        return False

def search(term):
    content = os.listdir()
    result = []
    for c in content:
        if term in c:
            result.append(c.replace(ext, ""))
    return result

if __name__ == "__main__":

    add_book("test_book", "test description")
    print(get_book("test_book"))
    print(get_book("test book"))
    print(search("test"))
    print(search("not"))
    print(remove_book("test_book"))
    print(remove_book("test book"))