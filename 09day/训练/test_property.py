class Laowang(object):
	def __init__(self):
		self.__money=0
	@property
	def money(self):
		return self.__money
	@money.setter
	def money(self,money):
		if isinstance(money,int):
			self.__money=money
	#money=property(getmoney,setmoney)
laowang=Laowang()
laowang.money=100
print(laowang.money)
