class Person():
	def __init__(self,name):
		self.name=name
		self.gun=None
		self.hp=100
	def loadbullet(self,clip,bullet):
		clip.loadclipbullet(bullet)
	def loadclip(self,gun,clip):
		gun.loadgunbullet(clip)
	def usegun(self,gun):
		self.gun=gun
	def shot(self,item):
		bullet=self.gun.popclip()
		bullet.kill(item)
class Gun():
	def __init__(self,name):
		self.name=name
		self.gunclip=None
	def loadgunbullet(self,clip):
		self.gunclip=clip
	def popclip(self):
		return self.gunclip.popbullet()
class Clip():
	def __init__(self,library):
		self.library=library
		self.listbullet=[]
	def loadclipbullet(self,bullet):
		self.listbullet.append(bullet)
		print(len(self.listbullet))
	def popbullet(self):
		return self.listbullet.pop()
class Bullet():
	def __init__(self,power):
		self.power=power
	def kill(self,item):
		item.hp-=self.power
		print("剩余血量为%d"%item.hp)
specialstroop=Person("特种兵")
gun=Gun("巴雷特")
clip=Clip(10)
#bullet=Bullet(30)
for temp in range(20):
	bullet=Bullet(30)
	specialstroop.loadbullet(clip,bullet)
specialstroop.loadclip(gun,clip)
laowang=Person("老王")
specialstroop.usegun(gun)
specialstroop.shot(laowang)
specialstroop.shot(laowang)
specialstroop.shot(laowang)
specialstroop.shot(laowang)
specialstroop.shot(laowang)
specialstroop.shot(laowang)
specialstroop.shot(laowang)

