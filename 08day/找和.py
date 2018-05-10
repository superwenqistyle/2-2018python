number1=[1,2,3,4,6,8,9]
#number2=[1,2,3,4,6,8,9]
for temp in number1:
	#number1.remove(temp)
	for i in number1:
		if temp+i == 10:
			x=number1.index(temp)
			y=number1.index(i)
			print("索引:%d,%d"%(x,y))
			print("数据:%d,%d"%(temp,i))

	
