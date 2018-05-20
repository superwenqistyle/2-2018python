def w1(id):
	def w2(fun):
	
		def w3(*args,**kwargs):
			if id == 1:
				ret = fun(*args,**kwargs)
				return ret
			else:
				print("验证失败")
				ret = fun()
				print(ret)
		return w3
	return w2


@w1(id=1)
def getMoney():
	return 50000
@w1(id=1)
def setmoney(money):
	print("要存去的是%d"%money)
@w1(id=2)
def OtherGetMoney():
	return 500000

t=getMoney()
print("取得钱数:%d"%t)

setmoney(50000)

OtherGetMoney()




