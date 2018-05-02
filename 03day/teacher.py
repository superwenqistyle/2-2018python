#人类
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None #默认没有枪
		self.hp  =  100 #默认有100滴血

	def zhuangzidan(self,danjia,bullet):#装子弹
		danjia.addBullet(bullet)

	def zhuangdanjia(self,gun,danjia):#装弹夹
		gun.addDanJia(danjia)

	def takeGun(self,gun):#老王拿枪
		self.gun = gun

	def openGun(self,diren):#老王开枪
		#拿到一发子弹
		zidan = self.gun.popGunBullet()#告诉枪给我一发子弹
		zidan.kill(diren)#子弹杀人
#枪类
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	#装弹夹
	def addDanJia(self,danjia):
		self.danjia = danjia

	def popGunBullet(self):
		return self.danjia.popBullet()	
#弹夹
class DanJia():
	def __init__(self,size):
		self.size = size
		self.bullet_list = []
	
	def addBullet(self,bullet):
		self.bullet_list.append(bullet)#加子弹
	

	def popBullet(self):
		return self.bullet_list.pop()#弹出子弹		
#子弹
class Bullet():

	def __init__(self):
		self.weili = 5
	#子弹杀人
	def kill(self,diren):
		diren.hp -= self.weili#减去子弹的威力
		print("剩余血量%d"%diren.hp)


laowang = Person("老王")#创建老王对象
ak47 = Gun("ak47")#创建一把枪
danjia = DanJia(20)#可以放20颗子弹
for i in range(20):#创建20发子弹
	bullet = Bullet()
	laowang.zhuangzidan(danjia,bullet)#装子弹
laowang.zhuangdanjia(ak47,danjia)#装弹夹

laosong = Person("老宋")#创建一个人
laowang.takeGun(ak47)#老王拿枪
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)
laowang.openGun(laosong)

