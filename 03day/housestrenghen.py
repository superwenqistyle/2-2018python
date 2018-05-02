class house():
	def __init__(self,area,brand,name):
		self.area=area
		self.brand=brand
		self.name=name
		self.furniture=[]
	def __str__(self):
		msg="房子的面积是%d%s新增的家具:"%(self.area,self.name)+"("
		if len(self.furniture) > 0:
			for temp in self.furniture:
				msg+=str(temp.getarea())+","
			msg=msg.strip(",")
		msg+=")"
		return msg
	def addfurniture(self,item):
		if self.area > item.getarea():
			self.area-=item.getarea()
			self.furniture.append(item.getname())
			print(myhouse)
			print("%s添加成功"%item)
		else:
			print("添加失败")
class bedfurniture():
	def __init__(self,name,area):
		self.name=name
		self.area=area
	def __str__(self):
		msg="%s的面积是%d"%(self.name,self.area)
		return msg
	def getarea(self):
		return self.area
	def getname(self):
		return self.name
myhouse=house(120,"恒大华府","三室两厅")
print(myhouse)
newbed=bedfurniture("席梦思",10)
print(newbed)
myhouse.addfurniture(newbed)
myhouse.addfurniture(newbed)
myhouse.addfurniture(newbed)
myhouse.addfurniture(newbed)
myhouse.addfurniture(newbed)

