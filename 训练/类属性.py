class Father(object):
	__instance=8
	def __init__(self,name):
		self.name=name
		self.skills=5
	def __str__(self):
		return "%s说的the life is short, wo need python"%self.name+"数据的种类是%d"%Father.__instance+"数据的类型是%d"%self.__instance
class Son(Father):
	def __init__(self,name):
		super().__init__(name)
		object.__init__(name) #没有反应
		Father.__init__(self,name)
xiaoming=Son("小明")
print(xiaoming)
