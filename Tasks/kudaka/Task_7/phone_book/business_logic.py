import data
from tkinter import messagebox


def print_f(files):
    strin = ""
    for file in files:
        for i in file.split(","):
            i += "\n"
            strin += i
    return strin


def search_exist(info):
    phons = data.file_open("r", None)
    if info in phons:
        return True
    elif info not in phons:
        return False


def get_all_phons():
    dat = data.get_phone()
    return print_f(dat)


def add_cont(*args):
    error = ["!", "£", "$", "%", "=", "?", "^", "*", "°", "  "]
    for i in args:
        if i == "":
            messagebox.showerror("ERROR", "some simbols is not allowed or missing")
            return False
        for g in error:
            if g in args:
                messagebox.showerror("ERROR", "some simbols is not allowed or missing")
                return False
    return True


def add_ph(*args):
    if add_cont(*args):
        file = f"Name:{args[0]},Last_name:{args[1]},Address:{args[2]},Company:{args[3]},Phone:{args[4]}\n"
        value = search_exist(file)
        if value:
            messagebox.showinfo("INFO", "such file already exist")
        elif value != True:
            data.add_phone(file)
            messagebox.showinfo("INFO", "data was saved successfully")


def remove_ph(info: str):
    phone_remove = info.replace("\n", ",").strip(",")
    if phone_remove.count(":") == 5:
        mes_an = messagebox.askyesno("INFO", "do you want to cancel contact")
        if mes_an:
            if search_exist(phone_remove):
                an = data.remove_phone(phone_remove + "\n")
                if an:
                    if search_exist(phone_remove) == False:
                        messagebox.showinfo("INFO", "contact was successfully deleted")
            else:
                messagebox.showerror("ERROR", "contact dose not exist")
    else:
        messagebox.showerror("ERROR", "missing some elements,please select contact")


def search_ph(info):
    if info == "" or " " in info:
        messagebox.showinfo("INFO", "please enter any key")
        return ""
    else:
        dat = data.search_phone(info)
        return print_f(dat)


def info_b():
    return data.d_info()

# if __name__ == "__main__":
#     remove_ph()