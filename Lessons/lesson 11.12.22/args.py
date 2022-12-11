def choose_pet_name(name_1, name_2="Tishka", check=False):
    choice = input(f"Choose between {name_1} and {name_2}:\n")
    if check:
        if choice not in [name_1, name_2]:
            print("Wrong choice!")
            return
    print(f"Congrats, your pet is {choice}")
    
choose_pet_name("Zephyrka", check=True)

print(1,2,3,4,5, sep=',')