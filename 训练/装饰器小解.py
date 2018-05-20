def w1(fun):
	def w2():
		fun()
	return w2
@w1
def test():
	print("封装的功能")
test()
