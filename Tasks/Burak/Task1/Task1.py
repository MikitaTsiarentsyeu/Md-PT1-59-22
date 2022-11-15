#This program is designed to calculate the amount in the account for deposits with monthly capitalization.
deposit, term, percentage = int(input('Please,enter the deposit ammount in BYN:')),\
                            int(input('Please,enter the deposit term in years:')),\
                            int(input('Please,enter the deposit percentage:'))
result = deposit * ((1+percentage/100/12))**(term*12)
rubles = int(result // 1)
kopecks = int((result % 1)*100)

if kopecks == 0:
    print('The total amount of the deposit at the end of the period will be', rubles,
          'belarusian rubles.')
elif kopecks == 1:
    print('The total amount of the deposit at the end of the period will be', rubles,
          'belarusian rubles', kopecks,
          'kopeck.')
else:
    print('The total amount of the deposit at the end of the period will be', rubles,
          'belarusian rubles', kopecks,
          'kopecks.')







