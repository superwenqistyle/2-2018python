class Dog(object):
	instance = None
	flag=0
	def __new__(cls,name):
		if cls.instance == None:
			print(cls.instance)
			cls.instance=object.__new__(cls)
			print(cls.instance)
			return cls.instance
		else:
			return cls.instance
	def __init__(self,name):
		if Dog.flag == 0:	
			self.name=name
			Dog.flag=1
		else:
			pass


	def __str__(self):
		return "str方法" 
	def __del__(self):
		print("删除初始化")
dog1=Dog("阿财")
dog2=Dog("阿旺")
print(id(dog1))	
print(id(dog2))
print(dog1.name)
print(dog2.name)
print(dog1)
print(dog2)

