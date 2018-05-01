class boy():
	def __init__(self,age,height):
		self.game=[]
		self.age=age
		self.height=height
		game=input("输入要玩的游戏:")
		#self.game=[game]
		self.game.append(game)
	def study(self,test):
		print("学习:%s"%test)
	def sing(self,test):
		print("唱歌:%s"%test)
	def introduce(self):
		print("年龄:%d\t身高:%d\t"%(self.age,self.height))
		for temp in self.game:
			print("玩游戏:%s"%temp)
liangwenqi=boy(26,178)
liangwenqi.study("math")
liangwenqi.sing("东方红")
liangwenqi.introduce()
