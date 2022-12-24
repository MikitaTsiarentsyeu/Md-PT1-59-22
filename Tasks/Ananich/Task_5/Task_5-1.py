string = input("Please enter a line\n")
if string == (""):
   print("The string is empty")
if string != (""):
  def check_str (upper_case = [] , lower_case = []):
    upper_case = [i for i in string if i.isupper()]
    lower_case = [i  for i in string if i.islower()]	
    print(f"In your line: {len(upper_case)} upper case, {len(lower_case)} lower case")
check_str()


  
          

