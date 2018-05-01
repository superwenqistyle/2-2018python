class huluwa():
	def sing(self):
		print("葫芦娃,葫芦娃,一棵藤上七个娃")
	def count(self):
		print("我们有都是好兄弟")
	def introduce(self):
		print("名字:%s\t年龄:%d\t颜色:%s"%(self.name,self.age,self.color))


dawa=huluwa()
dawa.sing()
dawa.count()
dawa.name="大娃"
dawa.age=23
dawa.color="蓝色"
dawa.introduce()
