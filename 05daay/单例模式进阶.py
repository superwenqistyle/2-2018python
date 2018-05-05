class Dog(object):
	__flag1 = None
	__flag = False
	def __new__(cls,name):
		if cls.__flag1 == None:
			cls.__flag1 = object.__new__(cls)
			return cls.__flag1
		else:
			return cls.__flag1
	def __init__(self,name):
		if Dog.__flag == False:
			self.name = name
			Dog.__flag=True
dog1 = Dog("dgeg")
dog2 = Dog("faewrg")
dog3 = Dog("grege")
dog4 = Dog("greg")
dog5 = Dog("grer")
print(id(dog1))
print(id(dog2))
print(id(dog3))
print(id(dog4))
print(id(dog5))

print(dog1.name)
print(dog2.name)
print(dog3.name)

