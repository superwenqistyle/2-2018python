class Person():
	def __init__(self,name):
		self.name=name
		self.gun=None
		self.hp=100
	def loadGunbullet(self,clip,bullet):
		clip.loadbullet(bullet)
	def loadGunclip(self,gun,clip):
		gun.loadclip(clip)
	def usegun(self,gun):
		self.gun=gun
	def shot(self,item):
		newbullet=self.gun.popgunbullet()
		newbullet.kill(item)
class Gun():
	def __init__(self,name):
		self.name=name
		self.gun=None
	def loadclip(self,clip):
		self.gun=clip
	def popgunbullet(self):
		return self.gun.popbullet()
class Clip():
	def __init__(self,library):
		self.library=library
		self.list_bullet=[]
	def loadbullet(self,bullet):
		self.list_bullet.append(bullet)
	def popbullet(self):
		return self.list_bullet.pop()
class Bullet():
	def __init__(self):
		self.power=5
	def kill(self,item):
		item.hp-=self.power	
laowang=Person("老王")
ak47=Gun("ak47")
clip=Clip(20)
for temp in range(20):
	bullet=Bullet()
	laowang.loadGunbullet(clip,bullet)
laowang.loadGunclip(ak47,clip)
laosong=Person("老宋")
laowang.usegun(ak47)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)


