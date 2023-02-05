import bl

def show_products():
    print("-------------------------------------------------------------------------------")
    print(f"{bl.get_products()}")
    print("-------------------------------------------------------------------------------")
    while True:
        choise = input ("""Choose a point from the menu:
        0.Exit
        1.Show Motor oil
        2.Show Transmission oil
        3.Show Hydraulic oil
        4.Show Antireeze
        5.Show Lubricants
        6.Show all products""")

        if choise == '0':
            break
        elif choise == '1':
            show_motor_oil() 
        elif  choise == '2':
            show_transmission_oil()
        elif choise == '3':
            show_hydraulic_oil()
        elif choise == '4':
            show_antireeze()
        elif choise == '5':
            show_lubricants()        
        elif choise == '6':
            show_all_products() 
            break


def show_motor_oil():
    print("--------------------------------------------------------------")
    print(f"{bl.get_motor_oil()}")
    print("--------------------------------------------------------------") 

def show_transmission_oil():
    print("--------------------------------------------------------------")
    print(f"{bl.get_transmission_oil()}")
    print("--------------------------------------------------------------") 

def show_hydraulic_oil():
    print("--------------------------------------------------------------")
    print(f"{bl.get_hydraulic_oil()}")
    print("--------------------------------------------------------------") 

def show_antireeze():
    print("--------------------------------------------------------------")
    print(f"{bl.get_antireeze()}")
    print("--------------------------------------------------------------") 

def show_lubricants():
    print("--------------------------------------------------------------")
    print(f"{bl.get_lubricants()}")
    print("--------------------------------------------------------------") 

def show_all_products():
    print("--------------------------------------------------------------")
    print(f"{bl.get_all()}")
    print("--------------------------------------------------------------") 

def show_basket(name):
    print("--------------------------------------------------------------")
    return bl.add_to_basket(name)


def make_an_order():
    while True: 
        item_for_order = input("Please, enter name of the product you have chosen:\n")
        print (f'{show_basket(item_for_order)}')
        break   

def show_total_amount():
    print("--------------------------------------------------------------")
    return bl.total_amount()


while True:
    chosen = input("""Choose a point from the menu:
    0.Exit
    1.Show catalog
    2.Make an order
    """)

    if chosen == '0':
        break

    elif chosen == '1':
        show_products()
        choise = input("Do you want to continue? Please, enter 'Yes' or 'No'\n")
        if choise == "Yes":
                continue
        else:
            print("Thank you! See you soon!")
            break 


    elif chosen == '2':
        make_an_order()
        while True:
            o = input("Do you want to order something else? Please, enter 'Yes' or 'No'\n") 
            if o == "Yes":
                make_an_order()      
            elif o == "No":
                print(f"The total price is {show_total_amount()}. Thank you for your order :)")   
                print("--------------------------------------------------------------") 
                break 

    break     