import os
import csv


current_dir = os.path.join("Filmbase", "Films")
ext = ".csv"

os.chdir(current_dir)


def add_film(name, x):
    with open(f'{name}{ext}', 'w', newline = '') as f:
        header = ['name', 'info', 'sits', 'data']
        val = x[name]
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        writer.writerow((val))
        spisok = f'{header[0]} : {val[0]} \n {header[1]} : {val[1]} \n  {header[2]} : {val[2]} \n {header[3]} : {val[3]}'        
        return  spisok
def add_booked_film(name, x):
    with open(f'{name}_reserve{ext}', 'w', newline = '') as f:
        header = ['name', 'info', 'sits', 'data']
        writer = csv.writer(f, delimiter=';')
        writer.writerow(header)
        writer.writerow((x))
    
def get_all_names():
    return [x.replace(ext, '') for x in os.listdir()]

def all_film (name, x):
    with open(f'{name}{ext}', 'w', newline = '') as f:
        writer = csv.writer(f, delimiter='|')
        header = ['Info', 'Genre', 'Sits']
        writer.writerow(header)
        writer.writerow(x[0])
        writer.writerow(x[1])
        writer.writerow(x[2])
        writer.writerow(x[3])
        writer.writerow(x[4])
        
def openes(name):
    with open(f'{name}{ext}', 'r') as f:
       return f.read()


Film1=['FullHD format','Horror',50, '01\\09\\23']
Film2=['3D format','Fantasy',50, '01\\15\\23']
Film3=['FullHD format','Horror',50, '01\\16\\23']
Film4=['FullHD format','Drama',50, '01\\22\\23']
Film5=['3D format','Fantasy',50, '01\\28\\23']
allfilms = [ Film1,Film2,Film3,Film4,Film5]

dict = {'Annabel': Film1, 'Avatar': Film2, 'Greanny': Film3, 'Happy end':Film4, 'Ivan Zarevich':Film5}

def search_info(term, dict):  
    if term in dict:
        val = dict[term]
        return val
    else:
        return False

def filt(value, dict): 
    l = []
    for k, v in dict.items():

        if v[1] == value:
            l.append(k)
    return l

res = []      
def favorite_film(name, res):
    
    content = os.listdir()
    name = f"{name}{ext}"
    
    if name in content:
     res.append(name.replace(ext,' '))
    return res
   
def remove_film (value, dict):
   
    content = os.listdir()
    l = []
    for k, v in dict.items():
        if v[1] == value:
            l.append(f'{k}{ext}')
    for i in l:
        if i in content:
            os.remove(i)
    return True
def choose_tickets(name, dict):
    content = os.listdir()
    name = f"{name}{ext}"
    if name in content:
        choose = name.replace(ext, '')
        info_choose = dict[choose][2]
        return info_choose
        
        



"""if __name__ == "__main__":
  print(all_film("All", allfilms))
  print(openes('All'))
  print(add_film('Annabel',dict))
print(add_film('Avatar',dict))
print(add_film('Greanny',dict))
print(add_film('Happy end',dict))
print(add_film('Ivan Zarevich',dict))

   
    
    
   
print(search_info('Annabel', dict))
print(filt('Horror', dict))
print(favorite_film('Annabel', res))
print(favorite_film('Avatar', res))

print(choose_tickets('Greanny', dict))"""
