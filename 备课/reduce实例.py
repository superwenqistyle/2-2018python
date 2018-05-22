from functools import reduce
def add(a,b):
	return a+b
t=reduce(add,range(1,6))
print(t)
