class Father(object):
	def __init__(self):
		print("Father的方法")
class Son(Father):
	def __init__(self):
		super().__init__()
		Father.__init__(self)
		print("*"*10)
		object.__init__(self)   #系统没有作出反应
		print("*"*10)	
xiaoming=Son()
