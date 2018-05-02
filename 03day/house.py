class house():
	def __init__(self,area,address):
		self.area=area
		self.address=address
		self.furniture=[]
		self.light=[]
	def __str__(self):
		msg="房子的面积是%d\t房子的地址是%s\t"%(self.area,self.address)
		return msg
	def addfurniture(self,bed):
		if self.area >= bed.getarea():
			self.furniture.append(bed)
			self.area-=bed.getarea()
			print("房间剩余空间:%d"%self.area)
			print("家具安放成功")
		
		else:
			print("家具安放失败")
	def addlight(self,light):
		self.light.append(light)
	def switchlight(self,):
		if self.light[0].switch():
			print("灯亮了")
		else:
			print("灯灭了")
		
class light():
	def __init__(self,brand):
		self.brand=brand
		self.defaultswitch=False  #默认灯灭
	def __str__(self):
		if self.defaultswitch == True:
			msg="灯开了"
		else:
			msg="灯关了"
		return msg
	def switch(self):
		return self.dafaultswith
		
		
class BedFurniture():
	def __init__(self,area,brand):
		self.area=area
		self.brand=brand
	def __str__(self):
		msg="床的面积是%d\t床的品牌是%s"%(self.area,self.brand)
		return msg
	def getarea(self):
		return self.area

		


myhouse=house(120,"朝阳区88号")
print(myhouse)
bed=BedFurniture(40,"席梦思")
print(bed)
newlight=light("阿拉灯")
print(newlight)
myhouse.switchlight()
myhouse.addfurniture(bed)
myhouse.addfurniture(bed)
myhouse.addfurniture(bed)
myhouse.addfurniture(bed)
myhouse.addfurniture(bed)
myhouse.addfurniture(bed)
