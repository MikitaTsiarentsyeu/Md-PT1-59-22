import data
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
            content = data.read_theme(name)
            if not content:
                continue
            res = f"{res}\n{name}:\n{content}"
    return res

def add_theme(name, descr):
    data.add_theme(name, descr)
    return "The theme was added"

def remove_theme(name):
    res = data.remove_theme(name)
    if res:
        return "The theme was deleted"
    else:
        return "The theme was not found"

def read_theme(name):
    descr = data.read_theme(name)
    if descr:
        return f"{name}\n{descr}"
    else:
        return "The theme was not found"


def search(term):
    content = data.search(term)
    res = ""
    if len(content) > 0:
        for i in range(1, len(content)+1):
            res = f"{res}\n{i}.{content[i-1]}"
    return res if res else "Nothing was found"

def add_comment(name,comment):
    res = data.add_comment(name,comment)
    if res:
        return "The comment was added"
    else:
        return "The theme was not found"
    


if __name__ == "__main__":
    print(add_theme("test_theme", "some descr"))
    print(get_all_names())
    print(get_all())
    print(search("test"))
    print(add_comment("test_theme","descr1"))
    print(add_comment("test theme","descr1"))


