class message():
	def __usemessage(self,money):
		i=1
		while True:
			money-=30
			if money > 0:
				print("第%d次扣费成功余额%d"%(i,money))
			else:
				print("第%s次扣费失败余额为%d"%(i,(money+30)))
				break
		
			print("第%d次扣费操作"%i)
			i+=1
	def publicmessage(self,money):
		if money < 0:
			print("输入不合法")
		else:
			self.__usemessage(money)

mes=message()
mes.publicmessage(10)

mes.publicmessage(100)

