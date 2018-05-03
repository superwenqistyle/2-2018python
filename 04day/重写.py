class Person(object):
	def __init__(self):
		self.skill=88
		print("技能有%d"%self.skill)
class xiaoming(Person):
	def __init__(self):
		self.count=99
		print("数量有%d"%self.count)
		Person.__init__(self)
		super().__init__()
xiang=xiaoming()
#xiang.__init__()
