
# D=b**-4*a*c

# if D >0 
#     x1 = (-*b - d**0.5) / (2*a)
#     x2 = (-*b + d**0.5) / (2*a)
#     print(x1,x2)
#  elif D ==0   
#     x2 = (-*b ) / (2*a)

#  else:

#     print() 

import decimal
# x = decimal.Decimal(0.1)
x = decimal.Decimal('0.3')
print(type(x))
print(x)
print(x*3)

print(float('0.1')+float('0.1')+float('0.1'))
print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')) 



from decimal import Decimal

Amount, Years, Percentage, Cap = Decimal(input("Enter the value of the initial amount of your deposit (BYN):")), Decimal(input("Enter the term of your deposit (in years):")), Decimal(input("Enter the value of the annual percentage of your deposit (%):")), (input("Do you want to enable monthly capitalization? (Please type [yes] if you want to enable capitalization, otherwise capitalization will not be performed:")) 

if (Cap=="yes" or Cap=="Yes"):
   Sum=Decimal(round(Amount*(pow(1+Percentage/100/12,12*Years)),2))
   print("The amount on the account in ", Years," years",Sum,"/ - With capitalization")
   print("типо да")

else: 
   Sum=Decimal(round(Amount*Percentage/100*Years+Amount,2))
   print("The amount on the account in ", Years," years",Sum,"/ - No capitalization")
   print("типо не понял")


print(type (Amount),Amount)
print(type (Percentage/100), Percentage/100)
print(type (Years), Years)

print("The amount on the account in ", Years," years", Sum,type(Sum),Cap)