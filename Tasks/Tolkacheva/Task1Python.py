from decimal import Decimal

#По-хоршему надо задать формат ввода значений для пользователя, не знаю пока, особенно с булевыми ясно что-то умнее можно

Amount, Years, Percentage, Cap = Decimal(input("Enter the value of the initial amount of your deposit (BYN):")), Decimal(input("Enter the term of your deposit (in years):")), Decimal(input("Enter the value of the annual percentage of your deposit (%):")), (input("Do you want to enable monthly capitalization? (Please type [yes] if you want to enable capitalization, otherwise capitalization will not be performed:")) 



if Cap.upper()=="YES": 
   Sum=Decimal(round(Amount*(pow(1+Percentage/100/12,12*Years)),2))
   print("The amount on the account in ", Years," years",Sum,"/ - With capitalization")
   

else: 
   Sum=Decimal(round(Amount*Percentage/100*Years+Amount,2))
   print("The amount on the account in ", Years," years",Sum,"/ - No capitalization")
   
