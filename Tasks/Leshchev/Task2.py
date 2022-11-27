
symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "-", "x", "y", "=" ]
formula_new = []


def define_formula(a, b) :                          #function delete unnecessary symbols
	b.clear()
	string_formula = input("Please, enter the formula y = kx + b  :").lower()
	list_formula = list(string_formula)
	for i in list_formula :
		for k in a :
			if i == k :
				b.append(i)
	define_xy(b)	
	
			
def define_xy(a) :	                                   #function_xy	
	if "y" in formula_new and "=" in formula_new and "x" in formula_new :
		y_index = formula_new.index("y")
		eq_index = formula_new.index("=")
		x_index = formula_new.index("x")
		en = 0
		for i in a :
			if i == "y" or i == "=" or i == "x" :
				en+=1
		if en == 3 :
			if y_index+1 == eq_index  and eq_index < x_index :
				define_variable(formula_new)
			else :
				print("You have done mistake. Please, try again")
				define_formula(symbols, formula_new)			
		else :
			print("You have done mistake. Please, try again")
			define_formula(symbols, formula_new)			
	else :
		print("You have done mistakes. Please, try again")
		define_formula(symbols, formula_new)
					
	
def define_variable(a) :                             #function define some situations
	y_index = a.index("y")
	x_index = a.index("x")
	if y_index > 0 :                                      #value_1
		variable_1 = a[ 0 : y_index ]
		clear_variable(variable_1)
		clear_minus(variable_1)
		if len(variable_1) == 1 and variable_1[ 0 ] == "0" :
			variable_1 = [ "1" ]
		elif len(variable_1) == 1 and variable_1[ 0 ] == "-" :
			variable_1 = [ "-1" ]
		elif variable_1 == [] :
			variable_1 = [ "1" ]	
		elif y_index == 2 and a[ 0 ] == "-" and a[ 1 ] == "0" :
			variable_1 = [ "1" ]
	else:
		variable_1 = [ "1" ]
	if y_index+2 != x_index :           #value_2
		variable_2 = a[ y_index+2 : x_index ]
		clear_variable(variable_2)
		clear_minus(variable_2)
		if len(variable_2) == 1 and variable_2[ 0 ] == "0" :
			variable_2 = [ "1" ]
		elif len(variable_2) == 1 and variable_2[ 0 ] == "-" :
			variable_2 = [ "-1" ]
		elif variable_2 == [ ] :
			variable_2 = [ "1" ]
		elif len(variable_2) == 2 and variable_2[ 0 ] == "-" and variable_2[ 1 ] == "0" :
			variable_2 = [ "1" ]
	else:
		variable_2 = [ "1" ]
	if x_index < len(a)-1 :                                  #value_3
		variable_3 = a[ x_index+1 : ]
		clear_variable(variable_3)
		clear_minus(variable_3)
		if len(variable_3) == 1 and variable_3[ 0 ] == "-" :  
			variable_3 = [ "0" ]
		elif variable_3 == [ ] :
			variable_3 = [ "0" ]	
		elif len(variable_3) == 2 and variable_3[ 0 ] == "-" and variable_3[ 1 ] == "0" :
			variable_3 = [ "0" ]	
	else:
		 variable_3 = [ "0" ]

	v_1 = "".join(variable_1) 

	v_2 = "".join(variable_2)

	v_3 = "".join(variable_3)
	
	print(f" k = {v_2} and b = {v_3}")
	print(f"Your function : y = ({v_2} x + {v_3})")
	enter(v_1, v_2, v_3, symbols)
	
def enter(a, b, c, e):                  #function enter   
	user = [ ]                                 
	enter_user = list(input("Please, enter x :"))	
	for i in enter_user:
		if i in symbols[0 : 12] :
			user.append(i)
	if user == [ ]:
		print("You have done mistakes")
		enter(a, b, c, e)		
			
	clear_variable(user)
	clear_minus(user)
		
	
	print("You entered " ,user)
	user = "".join(user)
	y = (float(b) * float(user) + float(c))/float(a)
	if y == "-0.0":
		y *= -1   
	print(f"answer, y =  {y : .2f}")	
	
def clear_variable(a, line = 0):                   #function_3 | delete unnecessary point in variable
	if "." in a:
		for i in a:
			if i == ".":
				line+=1
		if line == 1:
			point_index = a.index(".")
			if point_index == 0 or point_index == len(a)-1 :
				a.remove(".") 
			if a[point_index-1].isdigit() == True and a[point_index+1].isdigit() == True :
				pass			
			else:
				a.remove(".")
		else:
			for i in a[ : ] :
				if i == ".":
					a.remove(".")

def clear_minus(a, line = 0) :                       #clear_minus								
	if "-" in a :                
		for i in a :		
			if i == "-":
				line +=1
		if line == 1:
			if a[0] == "-" :
				pass			
			else:
				for i in a[ : ] :
					if i == "-":
						a.remove("-")
		else:
			for i in a[ : ] :
				if i == "-":
					a.remove("-")			
								
#start:
define_formula(symbols, formula_new)
