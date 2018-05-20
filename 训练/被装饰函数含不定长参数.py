def w1(fun):
	def w2(*args,**kwargs):
		print("验证功能模块")
		t = fun(*args,**kwargs)
		return t
	return w2
@w1
def test(a,b,c):
	print(a*b-c)

test(2,3,1)
