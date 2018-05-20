class w1():
	def __init__(self,fun):
		print("初始化")
		self.fun=fun
	def __call__(self):
		self.fun()
		print("进程结束")
@w1
def test():
	print("封装功能实现")

test()
