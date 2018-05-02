class Person():
	def __init__(self,name):
		self.name=name
		self.gun=None
		self.hp=100
	def loadbullet(self,clip,bullet):
		clip.addbullet(bullet)
	def loadclip(self,gun,clip):
		gun.addclip(clip)
	def usegun(self,gun):
		self.gun=gun
	def shot(self,item):
		newbullet=self.gun.popclipbullet(clip)
		newbullet.kill(item)
class Gun():
	def __init__(self,name):
		self.name=name
		self.bullets=None
	def addclip(self,bullet):
		self.bullets=clip
	def popclipbullet(self,clip):
		return self.bullets.popbullet()
class Clip():
	def __init__(self,library):
		self.library=library
		self.listbullet=[]
	def addbullet(self,bullet):
		self.listbullet.append(bullet)
	def popbullet(self):
		return self.listbullet.pop()
class Bullet():
	def __init__(self):
		self.power=5
	def kill(self,item):
		item.hp-=self.power
		print("剩余血量%d"%item.hp)
laowang=Person("老王")
ak47=Gun("ak47")
clip=Clip(20)
for temp in range(20):
	bullet=Bullet()
	laowang.loadbullet(clip,bullet)
laowang.loadclip(ak47,clip)
laosong=Person("老宋")
laowang.usegun(ak47)
laowang.shot(laowang)
laowang.shot(laowang)
laowang.shot(laowang)
laowang.shot(laowang)
laowang.shot(laowang)
laowang.shot(laowang)
laowang.shot(laowang)

