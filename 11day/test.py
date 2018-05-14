def fig(times):
	i=0
	a,b=0,1
	while i <= times:
		a,b=b,a+b
		temp=yield b
		print(temp)
		i+=1

	
