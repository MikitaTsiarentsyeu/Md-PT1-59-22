import os, csv


headline = ["Name", "Surname", "Number"]
ext = ".csv"


name = {"Name": "Sergey","Surname": "lesh4ev", "Number": "511"}

def add_book(name_book):
    content = os.listdir()
    veriable = name_book + ext
    if veriable not in content:
        with open(name_book + ext , "w", newline='') as f:
            writer = csv.DictWriter(f, headline)
            writer.writeheader() 
            return True
    else:
        return False   

def add_person(person, name_book):
    content = os.listdir()
    veriable = name_book + ext
    if veriable not in content:
        add_book(name_book)
    with open(name_book + ext , "a+", newline="") as f:
        writer = csv.DictWriter(f, headline)
        writer.writerow(person)
        return True 

def view_persons(name_book):
    content = os.listdir()
    veriable = name_book + ext
    if veriable in content:
        elements = []
        is_first = True
        with open(name_book + ext, 'r') as f:
            reader = csv.DictReader(f, headline)
            for e in reader:
                if is_first:
                    is_first = False
                    continue
                elements.append(e)
            return elements
    else:
        return False
    

def search(theme):
    content = os.listdir()
    result = []
    for i in content:
        m,k = os.path.splitext(i)
        if k == ".csv":
            with open(i, 'r') as f:
                reader = csv.DictReader(f, headline)
                is_first = True
                for v in reader:
                    if is_first:
                        is_first = False
                        continue
                    for d,f in v.items():    
                        if theme in f:
                            p = [i, v]
                            result.append(p)
    return result

def delete_person(name_book, theme):
    content = os.listdir()
    veriable = name_book + ext
    ver = False
    if veriable in content:
        with open(name_book + ext, 'r') as f:
            reader = csv.DictReader(f, headline)
            with open(name_book +"123" + ext , "w", newline='') as f:
                writer = csv.DictWriter(f, headline)
                for i in reader:
                    if theme not in i["Name"] and theme not in i["Surname"] and theme not in i["Number"]:  
                        writer.writerow(i)
                    else:
                        ver = True               
        os.remove(name_book + ext)
        os.rename(name_book +"123" + ext, name_book + ext)
        return ver
    return 1       
                
def delete_book(name_book):
    content = os.listdir()
    variable = name_book + ext
    if variable in content:
        os.remove(variable)
        return True
    else:
        return False

if __name__ == "__main__":
    #add_book("phone_book")
    #print(add_person(name, "book"))
    #print(add_person(name, "phone_book"))
    print(view_persons("N"))
    #search("Sergey")
    #delete_book("phone_book_2")
    #delete_person("phone_book_2", "Ser")