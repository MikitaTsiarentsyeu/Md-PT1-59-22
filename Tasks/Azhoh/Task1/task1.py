import decimal
print("Hello dear friend! Please enter the amount of the attachment")
sum=int(input())
print("Please enter the term in years")
term=int(input())
print("Please enter the interest rate")
percent=int(input())
Total=int(sum*percent*term*365/365)/100
capitalization= decimal.Decimal(sum*((1+percent/100/1))**term)
print("The total amount of the deposit:" , int(Total+sum))
print("The total amount of the deposit with capitalization:", "%.2f" % capitalization)
