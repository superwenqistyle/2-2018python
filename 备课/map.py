list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5,6]
list3=[1,2,3,4]
result=map(lambda x,y,z:x+y+z,list1,list2,list3)
print(result)
print(type(result))
for temp in result:
	print(temp)
