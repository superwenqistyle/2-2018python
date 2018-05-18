def w1(id,money):
	def w2(fun1,fun2):
	
	def w3(*args,**kwargs):
		if id == 1:
			get_money=fun1()
			set_money=fun2(money)
			return get_money,set_money()
	return w2



def getMoney():
	return 50000
def setmoney(money):
	print("要存去的是%d"%money)






id=int(input("请输入id:"))
money=int(input("请输入要存的钱数:"))
user=w1(id,money)
