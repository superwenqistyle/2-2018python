class person():
	def __init__(self,name):
		self.name=name
		self.gun=None
		self.hp=100
	def load_bullet(self,clip,bullet):
		clip.loadbullet(bullet)
	def load_clip(self,gun,clip):
		gun.loadclip(clip)
	def usegun(self,gun):
		self.gun=gun
	def shot(self,item):
		bullet=self.gun.popbullet()
		bullet.kill(item)
class gun():
	def __init__(self,name):
		self.name=name
		self.clip=None
	def loadclip(self,clip):
		self.clip=clip
	def popbullet(self):
		return self.bullet.pop()

		
		
#弹夹
class clip():
	def __init__(self,capacity):
		self.capacity=capacity
		self.listbullet=[]
	def loadbullet(self,bullet):
		self.listbullet.append(bullet)
		print("正在装弹")
	def pop(self):
		return self.listbullet.pop()
#子弹
class bullet():
	def __init__(self):
		self.power=5
	def kill(self,item):
		item.hp-=self.power
		print("剩余血量%d"%items.hp)
laowang=person("老王")
ak47=gun("ak47")
clip=clip(20)
for i in range(20):
	newbullet=bullet()
	laowang.load_bullet(clip,newbullet)
laowang.load_clip(ak47,clip)
laosong=person("老宋")
laowang.usegun(ak47)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)
laowang.shot(laosong)


