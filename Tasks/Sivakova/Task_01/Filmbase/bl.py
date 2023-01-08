import data
from colorama import Fore, Style
def add_film(name,x):
    return data.add_film(name,x)
def add_booked_film(name, x):
    return data.add_booked_film(name, x)
    
def get_names():
    names = data.get_all_names()
    res=""
    for i in names:
            res = f"{res}\n{i}"
    text = (Fore.GREEN + Style.BRIGHT +'The Actual list on January:')
    return f"{text}\n{Fore.WHITE +res}"

allfilms = data.allfilms
def get_all_films(name, x):
    data.all_film(name, x) 
    
def openes(name):

    return f'The full list of films: \n {data.openes(name)}'
   
        

dict = data.dict
def search_info(name, dict):
    info = data.search_info(name, dict)
    if info:
        return f'The quality is: {info[0]}, the genre is: {info[1]}'
    else:
        return 'Not found'
    
def search_sits(name, dict):
    
    info = data.search_info(name, dict)
    if info:
        return info [2]
    else:
        return 'Not found'

def filt(value, dict): 
    filt = data.filt(value, dict)
    filtr = ','.join(filt)
    if filt:
        return f' The is a film of your favorite genre: {filtr}' 
    else:
        return "Not found"
res = data.res

def favorite_film(name, res):
    favorite= data.favorite_film(name, res)
    if favorite:
        return f'My favorite film: {",".join(favorite)}'
    else:
        return 'There is not in cinema this time'

def remove_film (value, dict):
    remove = data.remove_film(value, dict)
    if remove:
        return "Menu of film was update"
    else:
        return "Film was not found"
def choose_tickets(name, dict):
    choose_sits = data.choose_tickets(name, dict)
    return choose_sits

def choose_sits(name, dict, x):
    list = []
    if name in dict:
        descr1 = dict[name][0]
        descr2 = dict[name][1]
        list.append(descr1)
        list.append(descr2)
        sitsres = dict[name][2] - x
        list.append(sitsres)
    return list


if __name__ == "__main__":
    print(get_names())
"""   add_film('Annabel',dict)
    add_film('Avatar',dict)
    add_film('Greanny',dict)
    add_film('Happy end',dict)
    add_film('Ivan Zarevich',dict)
    add_booked_film('Avatar',dict)
    print(get_names())
    print(get_all_films('All', allfilms))
    print(search_info('Avatar', dict))
    print(search_sits('Avatar', dict))
    print (filt('Fantasy', dict))
    print(favorite_film('tgt', res))
    print(favorite_film('Avatar', res))
    print(favorite_film('Greanny', res))
    print(choose_tickets("Avatar", dict))
    print(openes("All"))
    print(choose_sits('Avatar', dict, 2))
    print(remove_film('Horror', dict))"""