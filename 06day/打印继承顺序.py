class Father():
	def init(self):
		print("爸爸是伟大的")
class Mother():
	def init(self):
		print("妈妈是慈祥的")
class Son(Father,Mother):
	def __init__(self):
		print("开始继承了")
son=Son()
son.init()
print(Son.__mro__)
		
