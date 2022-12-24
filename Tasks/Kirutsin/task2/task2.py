import decimal

source = input('Hello!\nPlease input your value here. Example:\ny = kx + b\n')


# validator of start value
# src == data
def validation(src: str):
    spaces = src.replace(' ', '').replace('(', '').replace(')', '')
    count_1, count_2 = spaces.count('='), spaces.count('x')
    frod1 = '=' * count_1
    frod2 = 'x' * count_2

    final_src = spaces.replace(frod2, 'x').replace(frod1, '=')

    k = final_src[final_src.find('=') + 1:final_src.find('x')]
    if k[0] != '+' and k[0] != str('-'):
        k = '+' + k
    if k == '':
        k = '+1'
    b = final_src[final_src.find('x') + 2:]
    return k, b


# result of value
print(f'Your value:\n'
      f'k == {validation(source)[0]}\n'
      f'b == {validation(source)[1]}\n\n'
      f'Want to Calculate the expression ?\n y/n')

# user_choise
user_choise = input().lower()

if user_choise == 'y':
    x = (input('Provide please value of x. Example:\nx=-13\n').replace(' ', '').split('=')[1])
    k = validation(source)[0].replace('-', '').replace('+', '')
    b = validation(source)[1].replace('-', '').replace('+', '')

    # calculation
    if validation(source)[0][0] == '+' and validation(source)[1][0] == '+' and x[0] == '+':
        y = decimal.Decimal(k) * decimal.Decimal(x.replace('-', '').replace('+', '')) + decimal.Decimal(b)

    elif validation(source)[0][0] == '+' and validation(source)[1][0] == '-' and x[0] == '+':
        y = decimal.Decimal(k) * decimal.Decimal(x.replace('-', '').replace('+', '')) + (decimal.Decimal(b) * -1)

    elif validation(source)[0][0] == '-' and validation(source)[1][0] == '+' and x[0] == '+':
        y = (decimal.Decimal(k) * -1) * decimal.Decimal(x.replace('-', '').replace('+', '')) + decimal.Decimal(b)

    elif validation(source)[0][0] == '-' and validation(source)[1][0] == '-' and x[0] == '+':
        y = (decimal.Decimal(k) * -1) * decimal.Decimal(x.replace('-', '').replace('+', '')) + (decimal.Decimal(b) * -1)

    # x have -
    elif validation(source)[0][0] == '+' and validation(source)[1][0] == '+' and x[0] == '-':
        y = decimal.Decimal(k) * (decimal.Decimal(x.replace('-', '').replace('+', '')) * -1) + decimal.Decimal(b)

    elif validation(source)[0][0] == '+' and validation(source)[1][0] == '-' and x[0] == '-':
        y = decimal.Decimal(k) * (decimal.Decimal(x.replace('-', '').replace('+', '')) * -1) + (decimal.Decimal(b) * -1)

    elif validation(source)[0][0] == '-' and validation(source)[1][0] == '+' and x[0] == '-':
        y = (decimal.Decimal(k) * -1) * (decimal.Decimal(x.replace('-', '').replace('+', '')) * -1) + decimal.Decimal(b)

    elif validation(source)[0][0] == '-' and validation(source)[1][0] == '-' and x[0] == '-':
        y = (decimal.Decimal(k) * -1) * (decimal.Decimal(x.replace('-', '').replace('+', '')) * -1) + (
                decimal.Decimal(b) * -1)

    print(f'Result:\ny = {y}')

elif user_choise == 'n':
    print('Good day!')
