#人类
class Person():
	def __init__(self,name):
		self.name = name

	def zhuangzidan(self,danjia,bullet):
		danjia.addBullet(bullet)

#枪类
class Gun():
	def __init__(self,name):
		self.name = name
#弹夹
class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	
	def addBullet(self,bullet):
		self.bullet_list.append(bullet)
		print(len(self.bullet_list))	
#子弹
class Bullet():
	pass



laowang = Person("老王")
ak47 = Gun("ak47")
danjia = DanJia(20)#可以放20颗子弹
for i in range(20):
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)

