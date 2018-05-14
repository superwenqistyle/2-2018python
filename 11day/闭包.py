def test(a):
	def test1(b):
		print(a+b)
	return test1
f=test(1)
f(2)
