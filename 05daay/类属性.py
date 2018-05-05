class Dog():
	count=1
	def __init__(self,name):
		self.name=name
	#	Dog.count+=1
	def wark(self):
		print("汪汪汪")
	@classmethod
	def age(cls):
		print("我还年轻")
	@classmethod
	def changecount(cls):
		#cls.count+=1
		Dog.count+=1
		return cls.count

taidi=Dog("泰迪")
taidi.wark()
taidi.age()
Dog.age()
#Dog.wark(self)
print(taidi.count)
print(Dog.count)

print(taidi.changecount())
print(Dog.changecount())
print(taidi.changecount())
