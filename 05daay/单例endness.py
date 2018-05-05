class Dog(object):
	__instance=None
	__flag=False
	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance=object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		if self.__flag == False:
			self.name = name
			self.__flag=True

dog1=Dog("1")
dog2=Dog("2")
dog3=Dog("3")
dog4=Dog("4")
dog5=Dog("5")

print(id(dog1))
print(id(dog2))
print(id(dog3))
print(id(dog4))
print(id(dog5))

print(dog1.name)
print(dog2.name)
print(dog3.name)
