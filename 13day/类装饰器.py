class Dog(object):
	def __init__(self,fun):
		print("初始化")
		self.__fun=fun
	def __call__(self):
		print("类对象装饰器")
		self.__fun
@Dog
def test():
	print("hshshs")
test()
