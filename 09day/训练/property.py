class Laowang(object):
	def __init__(self):
		self.__money=0
	def setmoney(self,money):
		if isinstance(money,int):
			self.__money=money
	def getmoney(self):
		return self.__money
	money=property(getmoney,setmoney)
laowang=Laowang()
laowang.money=100
print(laowang.money)
