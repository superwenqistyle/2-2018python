class Dog():
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return self.name
	def __del__(self):
		print("删除实例......")
dog1=Dog("阿财")
dog2=Dog("阿旺")
print(dog1)
print(dog2)
del dog1
print("*"*10)
del dog2
print("hahfahfa")
