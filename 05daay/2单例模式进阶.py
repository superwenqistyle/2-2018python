class Dog():
	flag = None
	flag1 = 0
	def __new__(cls,name):
		if cls.flag == None:
			cls.flag = object.__new__(cls)
			return cls.flag
		else:
			return cls.flag
	def __init__(self,name):
		if Dog.flag1 == 0:
			self.name = name
			Dog.flag1 = 1


dog1 = Dog('asdasd')
dog2 = Dog('asd')
dog3 = Dog('sdasd')
print(id(dog1))
print(id(dog2))
print(id(dog3))
print(dog1.name)
print(dog2.name)
print(dog3.name)
