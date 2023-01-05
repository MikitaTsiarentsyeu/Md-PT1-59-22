import bl
import os

from colorama import Fore, Style
frr = Fore.RED
frg = Fore.GREEN
frb = Fore.BLUE
frw=Fore.WHITE

print(frg + Style.BRIGHT +"Choose operation: \n\
      1. Get list of the film on January\n\
      2. Get all information about the film\n\
      3. Get information about film\n\
      4. Viev a count of sits\n\
      5. Add a film to a favorite list\n\
      6. Remove special genre of films\n\
      7. Choose tickets\n\
      8. Return to the profile"+frw)


dict= bl.dict
def add_film(name, x): #добавить все фильмы
    bl.add_film(name, x)
    
def get_names():#получить все имена
    content = os.listdir()
    i = 'All.csv'
    if i in content:
        os.remove(i)
    return print (bl.get_names())
    
def get_all_films():
    allfims = bl.allfilms
    file = 'All'
    bl.get_all_films(file,allfims)
    return print(Fore.BLUE +bl.openes(file))

def search_info():
    name = input(frg+'Please, enter the filmname to get additional information '+frw)
    print(bl.search_info(name, dict))
sits = []
def search_sits(sits):
    name = input(frg +'Please, enter the filmname to get additional information '+frw)
    dict = bl.dict
    reserve= int(input(frg +'How much sits do you want to reserve?'+frw))
    res = (bl.search_sits(name,dict) - reserve)
    sits.append(res)
    return sits
def filt():
    kind_of_film = input(frg +'What kind of film do you intrested in? '+frw)
    print(frb +bl.filt(kind_of_film, dict))

def favorites():
    favorite = input(frg +'Please, enter the name of your favorite film to add it on group of favorites: '+frw)
    print(frb +bl.favorite_film(favorite, res))
def remove_film():
    genre_to_remove = input(frg +"What genre you don't wanna to watch in? "+frw)
    print(frr+ bl.remove_film(genre_to_remove, dict)+frw)
res = bl.res
def choose_tickets():
    name = input(frg+'Please, enter the filmname to get additional information '+frw)
    dict = bl.dict
    reserve= int(input(frg+'How much sits do you want to reserve?'+frw))
    getsits = bl.choose_tickets(name,dict)
    res = (getsits - reserve)
    sits.append(res)
    descr = bl.choose_sits(name,dict,reserve)
    bl.add_booked_film(name, descr)
    return print(f'{frw}You have been reserve {frr} {reserve} {frw} tickets for {frr} {name} {frw}film. Add info: \n\
        {frr} {descr[0]}{frw}, genre {frr} {descr[1]}{frw}, {frr} {descr[2]}{frw} sits left')
    
def count_of_sits():
    name = input(frg+'}Please, enter the filmname to get additional information '+frw)
    dict = bl.dict
    sits = dict[name][2]
    return print(f'{frr}{sits}{frw} left')



add_film('Annabel',dict)
add_film('Avatar',dict)
add_film('Greanny',dict)
add_film('Happy end',dict)
add_film('Ivan Zarevich',dict)




while True:
    user = input()
    if user=='1':
        get_names()
        
    if user=='2':
        get_all_films()
        
    if user=='3':
        search_info()
    if user=='4':
        count_of_sits()        
    if user=='5':
        favorites()
        while True:
            user1 = input(Fore.GREEN +'Do you want add film again? Yes/No '+Fore.WHITE )
            if user1=="Yes":
                favorites()
            
            if user1=='No':
                 print('Done')
                 break
    if user=='6':
        remove_film()
        
    if user=='7':
        choose_tickets()
  
        
    if user=='8':
        print('See you next time!')
        break
       



