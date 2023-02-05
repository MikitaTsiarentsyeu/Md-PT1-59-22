import os
import datetime

start_path = "forum"
dir = "themes"
current_dir = os.path.join(start_path, dir)
os.chdir(current_dir)
ext = ".txt"
date_time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def get_all_names():
    return [x.replace(ext, '') for x in os.listdir()]

def add_theme(name, descr):
    with open(f"{name}{ext}", 'w') as f:
        f.write(f"{descr}\n{date_time}\n")

def add_comment(name, comment):
    content = os.listdir()
    name = f"{name}{ext}"
    if name in content:
        with open(name, 'a') as f:
            f.write(f"{comment}\n{date_time}\n")
        return True
    else:
        return False

def read_theme(name):
    content = os.listdir()
    name = f"{name}{ext}"
    if name in content:
        with open(name, 'a+') as f:
            f.seek(0)
            content = f.read()
            return content
    return False

def remove_theme(name):
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

    add_theme("test_theme1", "test desc")
    print(add_comment("test_theme1", "test desc3"))
    print(read_theme("test_theme"))
    print(read_theme("test theme"))
    print(search("test"))
    print(search("not"))
    print(remove_theme("test_theme1"))
    print(remove_theme("test theme"))