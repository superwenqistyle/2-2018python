class pig():
	def eat(self):
		print("吃猪饲")
	def sleep(self):
		print("哼哼哼")
	def introduce(self):
		print("名字:%s\t颜色:%s\t年龄:%d"%(self.name,self.color,self.age))
peiqi=pig()
peiqi.eat()
peiqi.sleep()
peiqi.name="佩琪"
peiqi.color="red"
peiqi.age=12
peiqi.introduce()


qz=pig()
qz.eat()
qz.sleep()
qz.age=34
qz.name="敲诈"
qz.color="blue"
qz.introduce()
