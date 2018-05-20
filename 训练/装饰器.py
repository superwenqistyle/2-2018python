def w1(fun):
	print("w1开始执行")
	def w2():
		print("验证功能")
		t = fun()
		return t
	return w2
@w1
def test():
	print("fun功能功能被调用")
	return "将要被封装的功能"
print(test)
print(test())
test()
print(w1)
print(test)
print(id(w1))
print(id(test))

