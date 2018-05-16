class Dog(object):
	__instance=None
	__flag=0
	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance=super().__new__(cls)
			return cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		if Dog.__flag == 0:
			self.name=name
			Dog.__flag=1
		else:
			pass
dog1=Dog("name1")
dog2=Dog("name2")
print(id(dog1))
print(id(dog2))
print(dog1.name)
print(dog2.name)
