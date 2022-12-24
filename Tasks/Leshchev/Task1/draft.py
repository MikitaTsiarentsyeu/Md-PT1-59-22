
start_sum = int(input("Enter the sum: "))
annual_percentage = int (input("Enter the percent: "))

def calculation(a, b):
    answer = input("Do you want to add monthly capitalization (yes/no)")
    if answer == "yes":
        mounth = int(input("Enter the number of months: "))
        All_sum = freeValue = 0
        while mounth != 0:
            All_sum = (freeValue + start_sum)*(annual_percentage/100/12) 
            freeValue = All_sum + freeValue
            mounth -= 1	
        return(print("You will have" , "%.2f" % (freeValue+start_sum))) 
    elif answer == "no":
        term_in_years = int(input("Enter the term in year: "))
        All_sum = start_sum*(1+annual_percentage/100)**term_in_years
        return(print("You will have " "%.2f" % All_sum))
    else:
        print("You have done mistake, please try again")
        calculation(start_sum, annual_percentage)

calculation(start_sum, annual_percentage)


