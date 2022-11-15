import time
import decimal

print("Welcome on our webpage!")
sum=decimal.Decimal(input("Please, enter your basic sum in BYN: "))
per=decimal.Decimal(input("For how long do you want to invest in years? "))
am=decimal.Decimal(input("Choose your percentage: "))

print("We are processing your request...")
time.sleep(2)

ans=input("Choose your capitalization?(days/week/month/year/none):")

ansy="yes"
d="days"
w="week"
m="month"
y="year"
n="none"

income=decimal.Decimal(sum*per*am)/(100)
dep=decimal.Decimal(income+sum).__round__(2)

capd=decimal.Decimal(sum*((1+am/100/365))**per).__round__(2) 
capw=decimal.Decimal(sum*((1+am/100/4))**per).__round__(2)
capm=decimal.Decimal(sum*((1+am/100/12))**per).__round__(2)  
capy=decimal.Decimal(sum*((1+am/100/1))**per).__round__(2)



if ans==d:
    print("Your deposit with capitalization: "  + str(capd) + " BYN")

if ans==w:
    print("Your deposit with capitalization: "  + str(capw) + " BYN")
  
if ans==m:
    print("Your deposit with capitalization: "  + str(capm) + " BYN" )

if ans==y:
    print("Your deposit with capitalization: " + str(capy) + " BYN")
  
if ans==n:
    print("Your deposit: " + str(dep) + " BYN")
  
  
print("Wish you a good day!")
        


    
