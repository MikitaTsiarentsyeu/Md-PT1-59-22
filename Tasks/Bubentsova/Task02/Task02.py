# Task2> Calculate "y" value using the formula "y = kx + b" entered by user via one input

# Note1: The following cases are covered (operators can be +/-):
# 1. y = x
# 2. y = kx
# 3. y = kx + b
# 4. y = x + b
# 5. y = b + x
# 6. y = b + kx
# Note2: The following cases are not covered:
# 1. several x, k or b values, e.g.: "y = 3x + 4 + 3x + 5"
# 2. positive value with + operator (if there is just mistake during equation input), e.g.: "y = +2x + 4"
# 3. b value is not specified, e.g.: "y = 3x + ", "y = 3x - ", "y = + 2x"

import sys

# Variables
symbols_to_check1 = ["y", "x", "="] # mandatory symbols
symbols_to_check2 = ["*", "/", "//", "**", "%"] # not allowed symbols
message1 = "The entered equation is not correct."
message2 = "The entered equation contains not allowed symbols: *, /, //, **, %. Please rewrite your equation."

while True:
    equation_all = input("Please enter your equation in the following format: y = kx + b. For example: y = 2x + 3:\n")
    # Process initial equation
    # 1. Remove spaces if any
    if " " in equation_all:
        equation_wo_spaces = equation_all.replace(' ','')
        equation = equation_wo_spaces
    else:
        equation = equation_all
        
     # 2. Convert to lower case if required
    if "Y" or "X" in equation: # if Y and X in the upper case
        equation_final = equation.lower()
    else:
        equation_final = equation
        
    # 3. Create list from string
    equation_elements = list(equation_final)

    # 4. Validation 1: equation contains mandatory symbols "y", "x" and "="
    if all([s in equation_elements for s in symbols_to_check1]):
        print("Validation 1 passed")
    else:
        print(message1)
        continue
    
    # 5. Validation 2: equation is not in the format kx + b = y
    if equation_elements[-1] == "y":
        print(message1)
        continue
    else:
        print("Validation 2 passed")

    # 6. Validation 3: equation does not contain not allowed symbols: "*", "/", "//", "**", "%"
    if any([s in equation_elements for s in symbols_to_check2]):
        print(message2)
        continue
    else:
        print("Validation 3 passed")

    # Algorithm to find k and b values
    equation_len = len(equation_elements)

    if equation_len == 3:
        k = 1.0
        b = 0.0
    elif equation_len == 4 and equation_elements[2] == "-":
        k = -1.0
        b = 0.0
    else:
        equation_final_splitted = equation_final.split("x")
        equation_elements_0 = equation_final_splitted[0]
        equation_elements_1 = equation_final_splitted[1]
        equation_elements_0_list = list(equation_elements_0)
        equation_elements_1_list = list(equation_elements_1)
        if equation_elements_1_list != []: # e.g.: y = 3x + 2
            k_string = equation_elements_0.replace('y=','')
            if k_string =="":
                k = 1.0
            elif k_string == "-":
                k = -1.0
            else:
                k = float(k_string)
            b_string = equation_elements_1
            if "+" in equation_elements_1_list:
                b_string = equation_elements_1.replace('+','')
                b = float(b_string)
            else:
                b = float(b_string)
        else:
            equation_elements_1_list == [] # e.g.: y = 3x or y = 2 + 3x
            if "+" in equation_elements_0_list:
                plus_index = equation_elements_0_list.index("+")
                b_list = equation_elements_0_list[2:plus_index]
                b_string = ('').join(b_list)
                b = float(b_string)
                if equation_elements_0_list[-1] == "+":
                    k = 1.0
                else:
                    k_list = equation_elements_0_list[plus_index:]
                    k_list.remove("+")
                    k_string = ('').join(k_list)
                    k = float(k_string)      
            elif "-" in equation_elements_0_list:
                if equation_elements_0_list.count("-") == 1:
                    minus_index = equation_elements_0_list.index("-")
                    b_list = equation_elements_0_list[2:minus_index]
                    b_string = ('').join(b_list)
                    b = float(b_string)
                    if equation_elements_0_list[-1] == "-":
                        k = -1.0
                    else:
                        k_list = equation_elements_0_list[minus_index:]
                        k_string = ('').join(k_list)
                        k = float(k_string)
                else:
                    equation_elements_0_list.count("-") == 2
                    list_to_check = equation_elements_0_list
                    item = "-"
                    indexes = [i for i in range(len(list_to_check)) if list_to_check[i] == item]
                    minus_index1 = indexes[0]
                    minus_index2 = indexes[1]
                    b_list = equation_elements_0_list[2:minus_index2]
                    b_string = ('').join(b_list)
                    b = float(b_string)
                    if equation_elements_0_list[-1] == "-":
                        k = -1.0
                    else:
                        k_list = equation_elements_0_list[minus_index2:]
                        k_string = ('').join(k_list)
                        k = float(k_string)
            else: # "+" and "-" not in equation_elements_0_list:
                k_string = equation_elements_0.replace('y=','')
                k = float(k_string)
                b = 0.0
                    
    # 9. Request x value
    while True:
        try:
            x = float(input("Please enter the x value:\n"))
        except:
          print("Entered value is not valid. Please enter correct value which should be number.")
          continue
        break
        
    # 10. Calculate y value
    y = k*x + b
        
    # 11. Show result
    print(f"y value is {round(y, 2)}")
            
    # 12. Ask to repeat or not
    to_repeat = input("Would you like to repeat (Yes/No)?\n")
    if to_repeat == "No":
        print("Thank you for your participation.")
        sys.exit()