P = int(input("Enter the initial amount BYN:"))
I = int(input("Enter the annual percent %:"))
T = int(input("Enter the term in years:"))
K = int(365) # Number of days in a year
M = int(12) # Number of months in a year
# The general formula for calculating percent on a deposit
S1 = (P*I*T)/100
Sum1 = P+S1
print ("Your final amount", float(Sum1), "BYN")
# Formula for deposits with monthly capitalization
Sum2 = P*(1+((I/M)/100))**(M*T)
print ("Your final amount with monthly capitalization", float(Sum2), "BYN")
