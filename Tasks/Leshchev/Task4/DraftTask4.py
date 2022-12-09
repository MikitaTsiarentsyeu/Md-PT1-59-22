line = ""
variable = []
num = 0
v = []
user_enter = int(input("Pleace, enter width the line (>=35) : "))
simbols = user_enter

with open("text.txt", "r") as file:
	for i in file:
		line = line + i
a = line.split()

def space(variable):
	simbols = user_enter
	sum = 0
	spaces = len(variable)-1
	for i in variable:
		sum += len(i)
	n = simbols - sum - spaces
	while n > 0 :
		for m, k in enumerate(variable[:-1]):
			if n > 0:
				variable[m] = k + " "
				n -=1						 				

for k, i in enumerate(a):
	if simbols - num - 1 > len(i) :
		simbols = simbols - num - 1		
		if len(a)-1 != k :
			num = len(i)
			variable.append(i)
		elif len(a)-1 == k:
			variable.append(i)
			space(variable)
			variable.append(variable.pop() + "\n")
			v.append(" ".join(variable))
			last = "".join(v)
	elif simbols - num - 1 < len(i):
		space(variable)
		if len(a)-1 !=k:
			variable.append(variable.pop() + "\n")
			v.append(" ".join(variable))
			last = "".join(v)
			num = len(i)
			variable = [i]
			simbols = user_enter
		elif len(a)-1 == k:
			variable.append(variable.pop() + "\n")
			v.append(" ".join(variable))
			variable = [i]
			variable.append(variable.pop() + "\n")
			v.append(" ".join(variable))
			last = "".join(v)		
	
with open("textTask4.txt", "w") as donor:
	for i in last:
		donor.write(i)
print(last)
