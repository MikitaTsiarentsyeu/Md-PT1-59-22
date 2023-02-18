import os, csv


headline = ["Time", "Item"]
ext = ".csv"


name = {"Item": "Go to the shop", "Time": "12.00"}

def add_schedule(name_schedule):
    content = os.listdir()
    veriable = name_schedule + ext
    if veriable not in content:
        with open(name_schedule + ext , "w", newline='') as f:
            writer = csv.DictWriter(f, headline)
            writer.writeheader() 
            return True
    else:
        return False   

def add_item(item, name_schedule):
    content = os.listdir()
    veriable = name_schedule + ext
    if veriable not in content:
        add_schedule(name_schedule)
    with open(name_schedule + ext , "a+", newline="") as f:
        writer = csv.DictWriter(f, headline)
        writer.writerow(item)
        return True 

def view_schedule(name_schedule):
    content = os.listdir()
    veriable = name_schedule + ext
    if veriable in content:
        elements = []
        is_first = True
        with open(name_schedule + ext, 'r') as f:
            reader = csv.DictReader(f, headline)
            for e in reader:
                if is_first:
                    is_first = False
                    continue
                elements.append(e)
            return elements
    else:
        return False

def delete_item(name_schedule, theme):
    content = os.listdir()
    veriable = name_schedule + ext
    ver = False
    if veriable in content:
        with open(name_schedule + ext, 'r') as f:
            reader = csv.DictReader(f, headline)
            with open(name_schedule +"123" + ext , "w", newline='') as f:
                writer = csv.DictWriter(f, headline)
                for i in reader:
                    if theme not in i["Item"] and theme not in i["Time"]:  
                        writer.writerow(i)
                    else:
                        ver = True               
        os.remove(name_schedule + ext)
        os.rename(name_schedule +"123" + ext, name_schedule + ext)
        return ver
    return 1       
                
def delete_schedule(name_schedule):
    content = os.listdir()
    variable = name_schedule + ext
    if variable in content:
        os.remove(variable)
        return True
    else:
        return False

if __name__ == "__main__":
   
    print(view_schedule("N"))
   