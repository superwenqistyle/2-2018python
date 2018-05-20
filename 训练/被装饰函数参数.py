def w1(fun):
	def w2(a,b):
		print("验证模块")
		print(a,b)
		t=fun(a,b)
		return t
	return w2
@w1
def test(a,b):
	print("封装模块")
	print(a+b)

test(3,2)

		
