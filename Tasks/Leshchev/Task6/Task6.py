
x = [1, 2, [2, 4, [[7, 8], 4, 6]]]             #Task 6.1  
s = 0

def summ(x, i):        #Without the cycle for
    global s
    if i <= len(x)-1 and isinstance(x[i], int):
        s += x[i]
        i += 1
        summ(x, i)
        return s
    elif i <= len(x)-1 and isinstance(x[i], list):
        summ(x[i], 0)
        i +=1
        summ(x, i)
        return s
    elif i > len(x):
        return s
        
print(summ(x, 0))

s = 0     
def summ_2(x):                               #With the cycle for
	global s
	for i in x:
		if isinstance(i, int):
			s += i
		if isinstance(i, list):
			summ_2(i)
	return s

print(summ_2(x))        

        
a = [0, 1]                                   #Task 6.2
def fibonachi(n):
	if n > 2:
		a.append(a[-1]+a[-2])
		n-=1
		fibonachi(n)
	elif n < 3 and n > 0 :
		print(a[:n]) 
		
fibonachi(15)

def konkot(a, n = 0, b=""):          #Task 6.3
	if n < len(a):
		n +=1
		b += a[-n]
		konkot(a, n, b)
		return 
	elif n >= len(a) :
		a = b
		print(a)
		return a

konkot("hello")

def quick_sort(s):                      #Task 6.4
	if len(s) <= 1:
		return s	
	elem = s[(len(s))//2]
	left = [i for i in s if i < elem]
	center = [i for i in s if i == elem]
	right = [i for i in s if i > elem]
	
	return quick_sort(left) + center + quick_sort(right)
	
print(quick_sort([7, 6, 10, 5, 9, 8, 3, 4, 11, 4,5]))
