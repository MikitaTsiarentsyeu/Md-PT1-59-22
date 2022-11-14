import decimal as dec
while True:
    try:
        print("Enter amount of money that you want to deposit")
        money_amoun = dec.Decimal(input("Enter value: "))
    except Exception:
        print("YOU MUST ENTER A NUMBER, NOT A STRING!\nPlease try again")
    else:
        break
while True:
    try:
        print("For how many years do you want to deposit?")
        year_dep = dec.Decimal(input("Enter year/s: "))
    except Exception:
        print("YOU MUST ENTER A NUMBER, NOT A STRING!\nPlease try again")
    else:
        break
while True:
    try:
        print("Yearly percentage")
        year_per = dec.Decimal(input("Enter value: "))
    except Exception:
        print("YOU MUST ENTER A NUMBER, NOT A STRING!\nPlease try again")
    else:
        break
while True:
    print("Do you wish monthly capitalization?")
    month_cap = str(input("Enter yes/no "))
    if month_cap == "yes":
        count = money_amoun
        for i in range(int(year_dep*12)):
            calculation_yes = ((count * (dec.Decimal(1/12)) * year_per) / 100).__round__(2)
            count += calculation_yes
            print("Profit of the " + str(i+1) + " Month: "+str(calculation_yes))
        print("Total Profit is: "+str(count-money_amoun))
        print("Total money at the end of deposit is: "+str(count))
        break
    elif month_cap == "no":
        calculation_no = ((money_amoun * year_per * year_dep) / 100).__round__(2)
        total = calculation_no + money_amoun
        monthly_profit = (calculation_no / 12).__round__(2)
        print("Monthly profit: "+str(monthly_profit))
        print("Total profit: "+str(total-money_amoun))
        print("Total money at the end of deposit: "+str(total))
        break
    else:
        print("YOU MUST ENTER ONLY YES OR NO!\nPlease try again")





