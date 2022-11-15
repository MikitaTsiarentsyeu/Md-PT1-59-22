import decimal

# Hello user
input_parametrs = input("Hello!\nMy name finbot.Let's calculate your profit."
                        "Provide plesase,initial amount (for example, 20000),"
                        " term in years (for example, 5)),"
                        " annual percentage (for example, 15). Example:\n20000,5,15.4\n").split(',')

# calculations
amount, date_range, fee_year = decimal.Decimal(input_parametrs[0]), \
                               decimal.Decimal(input_parametrs[1]), \
                               decimal.Decimal(input_parametrs[2])
index = 1

import decimal as dec
while True:
    try:
        print("Enter amount of money that you want to deposit")
        print("Enter amount of money that you want to deposit in BYN")
        money_amoun = dec.Decimal(input("Enter value: "))
    except Exception:
        print("YOU MUST ENTER A NUMBER, NOT A STRING!\nPlease try again")

        for i in range(int(year_dep*12)):
            calculation_yes = ((count * (dec.Decimal(1/12)) * year_per) / 100).__round__(2)
            count += calculation_yes
            print("Profit of the " + str(i+1) + " Month: "+str(calculation_yes))
        print("Total Profit is: "+str(count-money_amoun))
        print("Total money at the end of deposit is: "+str(count))
        print("Profit of the " + str(i+1) + " Month: "+str(calculation_yes) + " BYN")
        print("Total Profit is: "+str(count-money_amoun) + " BYN")
        print("Total money at the end of deposit is: "+str(count) + " BYN")
        break
    elif month_cap == "no":
    calculation_no = ((money_amoun * year_per * year_dep) / 100).__round__(2)
    total = calculation_no + money_amoun
    monthly_profit = (calculation_no / 12).__round__(2)
    print("Monthly profit: "+str(monthly_profit))
    print("Total profit: "+str(total-money_amoun))
    print("Total money at the end of deposit: "+str(total))
    print("Monthly profit: "+str(monthly_profit) + " BYN")
    print("Total profit: "+str(total-money_amoun) + " BYN")
    print("Total money at the end of deposit: "+str(total) + " BYN")
    break
else:
    print("YOU MUST ENTER ONLY YES OR NO!\nPlease try again")