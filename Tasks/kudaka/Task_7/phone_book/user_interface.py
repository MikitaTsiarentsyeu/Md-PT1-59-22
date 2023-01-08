from tkinter import Tk, Toplevel, Button, Label, messagebox, Entry, scrolledtext, Frame, END
import business_logic


class gui(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Phone book")
        self.geometry("600x400")
        self.frame = Frame(height=200)
        self.label = Label(self.frame, text="enter a keyword:", font="Verdana,15")
        self.label.grid(column=0, row=0, padx=10, pady=10)
        self.entry = Entry(self.frame, width=40)
        self.entry.grid(column=1, row=0)
        self.search = Button(self.frame, text="Search", command=self.entry_get)
        self.search.grid(column=3, row=0, padx=10)
        self.label_1 = Label(self.frame, text="show all phones number:", font="Verdana,15")
        self.label_1.grid(columnspan=2, row=1, padx=10)
        self.show = Button(self.frame, text="show", command=self.show_all)
        self.show.grid(column=3, row=1, padx=10)
        self.label_2 = Label(self.frame, text="add a new number:", font="Verdana,15")
        self.label_2.grid(columnspan=2, row=2, padx=10, pady=10)
        self.add = Button(self.frame, text="add", command=self.c_win)
        self.add.grid(column=3, row=2)
        self.label_3 = Label(self.frame, text="delete number:", font="Verdana,15")
        self.label_3.grid(columnspan=2, row=3)
        self.delete = Button(self.frame, text="delete", command=self.del_but)
        self.delete.grid(column=3, row=3)
        self.frame.pack()
        self.sck = scrolledtext.ScrolledText(width=70)
        self.sck.pack(padx=10, pady=10)
        self.info()
        self.mainloop()

    def c_win(self):
        self.root = Toplevel(self)
        self.root.title("add new number")
        self.root.geometry("500x300")
        Label(self.root, text="enter name", font="Verdana,15").grid(column=0, row=0, pady=10, padx=10)
        self.name_ent = Entry(self.root, width=30)
        Label(self.root, text="enter last_name", font="Verdana,15").grid(column=0, row=1, pady=10, padx=10)
        self.last_name_ent = Entry(self.root, width=30)
        Label(self.root, text="address", font="Verdana,15").grid(column=0, row=2, pady=10, padx=10)
        self.addr_ent = Entry(self.root, width=30)
        Label(self.root, text="name of your company", font="Verdana,15").grid(column=0, row=3, pady=10, padx=10)
        self.comp_ent = Entry(self.root, width=30)
        Label(self.root, text="phone number", font="Verdana,15").grid(column=0, row=4, pady=10, padx=10)
        self.phone_ent = Entry(self.root, width=30)
        Button(self.root, text="save", command=self.data_chi_window).grid(column=1, row=5, padx=100)

        self.name_ent.grid(column=1, row=0)
        self.last_name_ent.grid(column=1, row=1)
        self.addr_ent.grid(column=1, row=2)
        self.comp_ent.grid(column=1, row=3)
        self.phone_ent.grid(column=1, row=4)

        self.focus()

    def focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()

    def entry_get(self):
        self.sck.delete(1.0, END)
        f = self.entry.get()
        st = business_logic.search_ph(f)
        self.sck.insert(1.0, st)

    def show_all(self):
        self.sck.delete(1.0, END)
        st = business_logic.get_all_phons()
        self.sck.insert(1.0, st)

    def del_but(self):
        info = self.sck.get(1.0, END)
        business_logic.remove_ph(info)

    def data_chi_window(self):
        name = self.name_ent.get()
        last_name = self.last_name_ent.get()
        address = self.addr_ent.get()
        company = self.comp_ent.get()
        phone = self.phone_ent.get()
        f = messagebox.askyesno("INFO", "DO YOU WANT TO SAVE")
        if f:
            business_logic.add_ph(name, last_name, address, company, phone)

    def info(self):
        self.sck.insert(1.0, business_logic.info_b())


gui()
