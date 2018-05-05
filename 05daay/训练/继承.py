class Animal():
	def __init__(self,name):
		self.name=name
		print("%s喜欢散步"%self.name)
class Dog(Animal):
	def __init__(self,name):
		self.name=name
		print("%s喜欢python"%self.name)

taidi=Dog("泰迪")
