class Father(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return "you are %s"%self.name
class Son(Father):
	def __init__(self,name):
		super().__init__(name)
	#	Father.__init__(self,name)
xiaoming=Son("小明")
print(xiaoming)
