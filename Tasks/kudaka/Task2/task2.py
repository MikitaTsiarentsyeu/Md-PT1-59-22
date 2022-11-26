errors = ["!", "'", '"', "£", "$", "%", "&", " ", "?", "^", "°", "_", ",", ";", ":"]
while True:
    try:
        user_equation = input("PLEASE ENTER EQUATION IN FORMAT 'Y = KX + B' OR Y = KX:\n")
        for error in errors:
            if error in user_equation:
                user_equation = user_equation.replace(error, "")
        x_value = input("Please enter value for X ")
        if "*" not in user_equation:
            user_equation = user_equation.replace("x","*"+x_value)
            replace_1 = user_equation[2::]
            print(f"Your equation is {user_equation}\nx is {x_value}\nYour result of equation is:{eval(replace_1)}")
        else:
            user_equation = user_equation.replace("x",x_value)
            replace_1 = user_equation[2::]
            print(f"Your equation is: {user_equation}\nx is: {x_value}\nYour result of equation is:{eval(replace_1)}")
    except Exception:
        print("SOMETHING WENT WRONG PLEASE TRY AGAIN")
    else:
        break






# "TRY THIS ONE:" 
#      "IT'S HAS 3 VALUES TO INPUT AND MORE PRECISE FOR ERRORS"

 

# alf_err = 'qwertyuiopasdfghjklzxcvbnméàòì'
# errors = ["!", "'", '"', "£", "$", "%", "&", " ", "?", "^", "°", "_", ",", ";", ":"]
# alfabet = "qwertyuiopasdfghjklzxcvbnméàòì"
# 
# 
# def iteral_act(itera):
#     it = ["*", "+", "/", "-"]
#     for i in it:
#         if i == itera:
#             return itera
# 
# 
# def restart():
#     print("too bad equation,please enter again ")
#     ent_equation()
# 
# 
# def ent_equation():
#     user_equation = input("PLEASE ENTER EQUATION IN FORMAT 'Y = KX + B' OR 'Y = KX' ONLY ALFABET LETTERS:\n")
#     if len(user_equation) >= 4:
#         control(user_equation)
#     else:
#         restart()
# 
# 
# def control(equation):
#     count = 0
#     for i in errors:
#         if i in equation:
#             equation = equation.replace(i, "")
#     for g in equation:
#         if g.lower() in alfabet:
#             count += 1
#             if count > 4:
#                 equation = equation.replace(g, "")
#     control_2(equation)
# 
# 
# def control_2(equation):
#     if len(equation) == 4:
#         if equation[0].lower() in alfabet and equation[1] == "=" and equation[2].lower() in alfabet and equation[
#             3].lower() in alfabet:
#             if equation[0] != equation[2] and equation[2] != equation[3] and equation[0] != equation[3]:
# 
#                 new_equation = equation.replace(equation[-1], "*" + equation[-1])
#                 values(new_equation)
# 
#             else:
#                 restart()
#         else:
#             restart()
#     if len(equation) == 5:
#         if equation[0].lower() in alfabet and equation[1] == "=" and equation[2].lower() in alfabet and equation[
#             3] == iteral_act(
#             equation[3]) and equation[4].lower() in alfabet:
#             if equation[0] != equation[2] and equation[2] != equation[4] and equation[0] != equation[4]:
#                 new_equation = equation
#                 values(new_equation)
# 
#             else:
#                 restart()
#         else:
#             restart()
#     if len(equation) == 6:
#         if equation[0].lower() in alfabet and equation[1] == "=" and equation[2].lower() in alfabet and equation[
#             3].lower() in alfabet and equation[4] == iteral_act(equation[4]) and equation[5].lower() in alfabet:
#             if equation[0] != equation[2] and equation[2] != equation[3] and equation[0] != equation[3] and \
#                     equation[0] != equation[5] and equation[2] != equation[5] and equation[3] != equation[5]:
#                 new_equation = equation.replace(equation[3], "*" + equation[3])
#                 values(new_equation)
# 
#             else:
#                
#                 restart()
#         else:
#             
#             restart()
#     if len(equation) == 7:
#         if equation[0].lower() in alfabet and equation[1] == "=" and equation[2].lower() in alfabet and equation[
#             3] == iteral_act(
#             equation[3]) and equation[4].lower() in alfabet and equation[5] == iteral_act(equation[5]) and equation[
#             6].lower() in alfabet:
#             if equation[0] != equation[2] and equation[2] != equation[4] and equation[0] != equation[4] and equation[
#                 0] != equation[6] \
#                     and equation[2] != equation[6] and equation[4] != equation[6]:
#                 new_equation = equation
#                 values(new_equation)
# 
#             else:
#                 restart()
#         else:
#             restart()
# 
# 
# def values(values_equ):
#     while True:
#         if len(values_equ) == 5:
#             user_values = input(f"Please enter numeric values divided by  ',' for "
#                                 f"{values_equ[2]} and {values_equ[4]}:\n")
#             if len(user_values.split(",")) == 2:
#                 list_values = user_values.split(",")
#                 is_it_numeric(list_values, values_equ)
#                 break
#             else:
#                 print("missing values please enter again")
# 
#         elif len(values_equ) == 7:
#             user_values = input(
#                 f"Please enter numeric values divided by ',' for "
#                 f"{values_equ[2]},{values_equ[4]} and {values_equ[6]}:\n")
#             if len(user_values.split(",")) == 3:
#                 list_values = user_values.split(",")
#                 is_it_numeric(list_values, values_equ)
#                 break
#             else:
#                 print("missing values please enter again")
# 
# 
# def is_it_numeric(l_t, values_equ):
#     values_equ_1 = values_equ
#     list_num = []
#     for i in l_t:
#         if "(" == i[0] and ")" == i[-1] and i[1] == "-" and i[2].isnumeric():
#             list_num.append(i)
#         elif i[0].isnumeric():
#             list_num.append(i)
#         elif i[0] == "-" and i[1].isnumeric():
#             list_num.append("(" + i + ")")
#         else:
#             print("Expecting numbers,Please try again")
#             list_num.clear()
#             values(values_equ_1)
# 
#   
#     try:
#         def sum_coun(list_num, val_equ):
#             true_count = 0
#             val_equ_1 = val_equ
#             for i in list_num:
#                 for g in val_equ_1[2 + true_count]:
#                     val_equ_1 = val_equ_1.replace(g, i)
#                 true_count += 2 + len(i) - 1
# 
#             calculation = eval(val_equ_1[2::])
#             result = f"Your equation is :{val_equ}\nYour equation is replaced with numbers is:{val_equ_1}" \
#                     f"\nYour result is :{val_equ_1[0:2]} {calculation} "
#             print(result)
#         sum_coun(list_num, values_equ)
#     except Exception:None
# ent_equation()
