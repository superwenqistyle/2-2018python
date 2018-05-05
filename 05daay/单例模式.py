class Dog(object):
	__instance=None
	__name=None
	def __init__(self,name):
		if self.__name == None:
			Dog.__name=name
			#return self.__name
		else:
			#return self.__name
			#Dog.__name=name
			pass
		print("名字是%s"%Dog.__name)

	def __new__(cls,name):
		if cls.__instance == None:
			cls.instance = object.__new__(cls)
			return cls.__instance
		else:
			return cls.__instance

'''
	def __init__(self,name):
	#	print("名字是%s"%self.name)
		if self.__name == None:
			self.name=name
			return self.__name
		else:
			return self.__name
'''
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
print(dog1.__name)
