from functools import reduce

def multiply(a,b):
	return a*b
t=reduce(multiply,[1,2,3,4,5,6])
print(t)
