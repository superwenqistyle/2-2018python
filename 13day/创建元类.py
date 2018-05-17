class Bar(object):
	def info(self):
		print("Tom是什么")
def show(self):
	print("the life is short ,wo need python")
Dog=type("Dog",(Bar,),{"name":"Tom","show":show})
dog=Dog()
print(dog.name)
dog.info()
dog.show()
