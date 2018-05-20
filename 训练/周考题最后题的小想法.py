def im_port():
	ID=int(input("请输入id 1或2:"))
	money=int(input("请输入要去存的钱数"))
	return ID,money
ID,money = im_port()

def w1(ID,money):
	def w2(fun):
		def w3():
			print("开启验证功能")
			t = fun()
			if ID == 1:
				print("验证成功")
				print("取出的钱数是%d"%t.getMoney())
				t.setMoney(money)
			else:
				print("验证失败")
				print("要取的钱数是%d"%t.otherGetMoney())
		return w3
	return w2

@w1(ID,money)
class Function():
	def getMoney(self):  #id=1
		return 500000
	def setMoney(self,money):  #id=1
		print("要存%f"%money)	
	def otherGetMoney(self):  #id=2
		return 500000

Function()
