class Person():
	def __init__(self):
		self.__money=100
	def getmoney(self):
		return self.__money
	def setmoney(self,money):
		if money < 0:
			print("传入金额非法")
		else:
			self.__money=money
laowang=Person()
laowang.setmoney(100)
print(laowang)
print(laowang.getmoney())
