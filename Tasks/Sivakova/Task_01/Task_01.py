import time

print("Welcome on our webpage!")
sum=int(input("Please, enter your basic sum in BYN: "))
per=int(input("For how long do you want to invest in years? "))
am=int(input("Choose your percentage: "))

print("We are processing your request...")
time.sleep(2)

ans=input("Choose your capitalization?(days/week/month/year/none):")

ansy="yes"
d="days"
w="week"
m="month"
y="year"
n="none"

income=int(sum*per*am)/(100)
dep=int(income+sum)

capd=int(sum*((1+am/100/365))**per) 
capw=int(sum*((1+am/100/4))**per)
capm=int(sum*((1+am/100/12))**per)  
capy=int(sum*((1+am/100/1))**per)



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
        


    
